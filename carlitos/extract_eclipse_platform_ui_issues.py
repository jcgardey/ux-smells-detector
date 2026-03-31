#!/usr/bin/env python3
"""Extract all issues from a public GitHub repository and write CSV/JSON outputs.

Features
- Exhaustive pagination through the REST API.
- Filters out pull requests from the /issues endpoint.
- Adds issue_number and issue_identifier columns.
- Optionally merges an existing classification CSV (e.g. title/body/ux_smell/reasoning).
- Validates counts and writes a small QC report.

Usage examples
  python extract_eclipse_platform_ui_issues.py \
      --repo eclipse-platform/eclipse.platform.ui \
      --out-csv eclipse_platform_ui_issues_full.csv \
      --out-json eclipse_platform_ui_issues_full.json

  GITHUB_TOKEN=ghp_xxx python extract_eclipse_platform_ui_issues.py \
      --repo eclipse-platform/eclipse.platform.ui \
      --existing-classifications eclipse_platform_ui_ux_smells_complete.csv \
      --out-csv eclipse_platform_ui_issues_with_ux.csv \
      --out-json eclipse_platform_ui_issues_with_ux.json
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import requests
except ImportError as exc:  # pragma: no cover
    raise SystemExit("This script requires 'requests'. Install it with: pip install requests") from exc


API_BASE = "https://api.github.com"
DEFAULT_TIMEOUT = 30


@dataclass
class RepoCounts:
    open_issues_count_field: Optional[int]
    fetched_total_issues: int
    fetched_open_issues: int
    fetched_closed_issues: int


class GitHubClient:
    def __init__(self, token: Optional[str] = None, timeout: int = DEFAULT_TIMEOUT, verbose: bool = False):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "User-Agent": "issue-extractor/1.0",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        self.timeout = timeout
        self.verbose = verbose

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            raise RuntimeError(
                "GitHub API rate limit reached. Set GITHUB_TOKEN to increase the limit and retry."
            )
        resp.raise_for_status()
        return resp

    def get_repo_metadata(self, repo: str) -> Dict[str, Any]:
        url = f"{API_BASE}/repos/{repo}"
        return self._request("GET", url).json()

    def iter_all_issues(self, repo: str, per_page: int = 100, pause_seconds: float = 0.0) -> Iterable[Dict[str, Any]]:
        url = f"{API_BASE}/repos/{repo}/issues?state=all&per_page={per_page}"
        page_num = 1
        while url:
            if self.verbose:
                print(f"Fetching page {page_num}...", file=sys.stderr)
            resp = self._request("GET", url)
            data = resp.json()
            if not data:
                break
            for item in data:
                if "pull_request" in item:
                    continue
                yield item
            
            url = None
            if "Link" in resp.headers:
                links = resp.headers["Link"].split(",")
                for link in links:
                    if 'rel="next"' in link:
                        url = link[link.find("<")+1:link.find(">")]
                        break
            page_num += 1
            if pause_seconds > 0:
                time.sleep(pause_seconds)


def normalize_issue(repo: str, issue: Dict[str, Any]) -> Dict[str, Any]:
    labels = issue.get("labels") or []
    assignees = issue.get("assignees") or []
    milestone = issue.get("milestone")
    issue_number = int(issue["number"])
    return {
        "ID": issue_number,
        "Title": issue.get("title") or "",
        "State": issue.get("state"),
        "URL": issue.get("html_url") or "",
        "Labels": ", ".join(label.get("name", "") for label in labels),
        "Created At": issue.get("created_at"),
        "issue_number": issue_number,
        "issue_identifier": f"{repo}#{issue_number}",
        "repo": repo,
        "state_reason": issue.get("state_reason"),
        "body": issue.get("body") or "",
        "api_url": issue.get("url") or "",
        "author_login": (issue.get("user") or {}).get("login"),
        "updated_at": issue.get("updated_at"),
        "closed_at": issue.get("closed_at"),
        "comments": issue.get("comments"),
        "locked": issue.get("locked"),
        "assignees": "|".join(a.get("login", "") for a in assignees),
        "milestone": milestone.get("title") if milestone else None,
    }


def load_existing_classifications(path: Path) -> Dict[Tuple[str, str], Dict[str, str]]:
    import pandas as pd

    df = pd.read_csv(path)
    required = {"title", "body", "ux_smell", "reasoning"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Existing classifications file is missing columns: {sorted(missing)}")

    mapping: Dict[Tuple[str, str], Dict[str, str]] = {}
    for _, row in df.iterrows():
        title = "" if pd.isna(row.get("title")) else str(row.get("title"))
        body = "" if pd.isna(row.get("body")) else str(row.get("body"))
        mapping[(title, body)] = {
            "ux_smell": None if pd.isna(row.get("ux_smell")) else str(row.get("ux_smell")),
            "reasoning": "" if pd.isna(row.get("reasoning")) else str(row.get("reasoning")),
        }
    return mapping


def merge_classifications(rows: List[Dict[str, Any]], existing_map: Dict[Tuple[str, str], Dict[str, str]]) -> None:
    # First try exact (title, body), then fallback to title-only if unique.
    title_only: Dict[str, List[Dict[str, str]]] = {}
    for (title, _body), payload in existing_map.items():
        title_only.setdefault(title, []).append(payload)

    for row in rows:
        exact = existing_map.get((row["title"], row["body"]))
        if exact is not None:
            row["ux_smell"] = exact["ux_smell"]
            row["reasoning"] = exact["reasoning"]
            continue

        candidates = title_only.get(row["title"], [])
        if len(candidates) == 1:
            row["ux_smell"] = candidates[0]["ux_smell"]
            row["reasoning"] = candidates[0]["reasoning"]
        else:
            row.setdefault("ux_smell", None)
            row.setdefault("reasoning", "")


def write_csv(rows: List[Dict[str, Any]], path: Path) -> None:
    if not rows:
        raise ValueError("No rows to write")
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(rows: List[Dict[str, Any]], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


def build_qc_report(repo: str, repo_meta: Dict[str, Any], rows: List[Dict[str, Any]]) -> str:
    fetched_total = len(rows)
    fetched_open = sum(1 for r in rows if r.get("state") == "open")
    fetched_closed = sum(1 for r in rows if r.get("state") == "closed")
    open_issues_count_field = repo_meta.get("open_issues_count")

    lines = [
        f"repo={repo}",
        f"open_issues_count_field={open_issues_count_field}",
        f"fetched_total_issues={fetched_total}",
        f"fetched_open_issues={fetched_open}",
        f"fetched_closed_issues={fetched_closed}",
        "notes=GitHub's repository open_issues_count field may include pull requests on some endpoints; the extractor filters PRs out from /issues results.",
    ]
    return "\n".join(lines) + "\n"


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract all GitHub issues from a repository.")
    parser.add_argument("--repo", default="eclipse-platform/eclipse.platform.ui", help="owner/repo")
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"), help="GitHub token, or set GITHUB_TOKEN")
    parser.add_argument("--out-csv", default="eclipse_platform_ui_issues_full.csv", help="Output CSV path")
    parser.add_argument("--out-json", default="eclipse_platform_ui_issues_full.json", help="Output JSON path")
    parser.add_argument("--out-qc", default="eclipse_platform_ui_issues_qc.txt", help="Output QC report path")
    parser.add_argument(
        "--existing-classifications",
        default=None,
        help="Optional CSV with title/body/ux_smell/reasoning to merge into the extracted dataset",
    )
    parser.add_argument("--pause-seconds", type=float, default=0.0, help="Optional pause between pages")
    parser.add_argument("--verbose", action="store_true", help="Verbose progress logs to stderr")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    client = GitHubClient(token=args.token, verbose=args.verbose)

    repo_meta = client.get_repo_metadata(args.repo)
    issues_raw = list(client.iter_all_issues(args.repo, pause_seconds=args.pause_seconds))
    rows = [normalize_issue(args.repo, issue) for issue in issues_raw]

    # Stable sort by issue number ascending.
    rows.sort(key=lambda r: int(r["issue_number"]))

    if args.existing_classifications:
        existing_map = load_existing_classifications(Path(args.existing_classifications))
        merge_classifications(rows, existing_map)
    else:
        for row in rows:
            row.setdefault("ux_smell", None)
            row.setdefault("reasoning", "")

    write_csv(rows, Path(args.out_csv))
    write_json(rows, Path(args.out_json))
    Path(args.out_qc).write_text(build_qc_report(args.repo, repo_meta, rows), encoding="utf-8")

    print(f"Wrote {len(rows)} issues to {args.out_csv} and {args.out_json}")
    print(f"QC report: {args.out_qc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
