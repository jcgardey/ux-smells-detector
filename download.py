#!/usr/bin/env python3
"""
GitHub Issues Downloader
Downloads all issues from a GitHub repository and saves them in CSV or plain text format.
"""

import requests
import csv
import json
import argparse
import sys
from datetime import datetime
from typing import List, Dict, Optional


class GitHubIssuesDownloader:
    def __init__(self, token: Optional[str] = None):
        """
        Initialize the GitHub Issues Downloader.
        
        Args:
            token (Optional[str]): GitHub personal access token for authenticated requests
        """
        self.base_url = "https://api.github.com"
        self.session = requests.Session()
        
        if token:
            self.session.headers.update({
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            })
        else:
            self.session.headers.update({
                'Accept': 'application/vnd.github.v3+json'
            })

    def get_all_issues(self, owner: str, repo: str, state: str = 'all') -> List[Dict]:
        """
        Fetch all issues from a GitHub repository.
        
        Args:
            owner (str): Repository owner (username or organization)
            repo (str): Repository name
            state (str): Issue state filter ('open', 'closed', 'all')
            
        Returns:
            List[Dict]: List of issue dictionaries
        """
        issues = []
        page = 1
        per_page = 100  # Maximum allowed by GitHub API
        
        print(f"Fetching issues from {owner}/{repo}...")
        
        while True:
            url = f"{self.base_url}/repos/{owner}/{repo}/issues"
            params = {
                'state': state,
                'page': page,
                'per_page': per_page,
                'sort': 'created',
                'direction': 'asc'
            }
            
            print(f"Fetching page {page}...", end=' ')
            
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                
                page_issues = response.json()
                
                if not page_issues:
                    print("Done!")
                    break
                
                # Filter out pull requests (they appear as issues in GitHub API)
                actual_issues = [issue for issue in page_issues if 'pull_request' not in issue]
                issues.extend(actual_issues)
                
                print(f"Got {len(actual_issues)} issues")
                page += 1
                
            except requests.exceptions.RequestException as e:
                print(f"\nError fetching issues: {e}")
                if hasattr(e.response, 'status_code') and e.response.status_code == 403:
                    print("Rate limit exceeded or authentication failed. Consider using a GitHub token.")
                sys.exit(1)
        
        print(f"\nTotal issues downloaded: {len(issues)}")
        return issues

    def extract_issue_data(self, issue: Dict) -> Dict:
        """
        Extract relevant fields from a GitHub issue.
        
        Args:
            issue (Dict): GitHub issue dictionary
            
        Returns:
            Dict: Extracted issue data
        """
        def parse_date(date_str: Optional[str]) -> Optional[str]:
            """Parse ISO date string to readable format."""
            if not date_str:
                return None
            try:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                return dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                return date_str

        return {
            'id': issue.get('number'),
            'title': issue.get('title', '').strip(),
            'body': issue.get('body', '').strip() if issue.get('body') else '',
            'opened': parse_date(issue.get('created_at')),
            'closed': parse_date(issue.get('closed_at')),
            'state': issue.get('state'),
            'url': issue.get('html_url'),
            'labels': ', '.join([label['name'] for label in issue.get('labels', [])])
        }

    def save_to_csv(self, issues_data: List[Dict], filename: str):
        """
        Save issues to CSV format.
        
        Args:
            issues_data (List[Dict]): List of extracted issue data
            filename (str): Output CSV filename
        """
        if not issues_data:
            print("No issues to save.")
            return

        fieldnames = ['id', 'title', 'body', 'opened', 'closed', 'state', 'url', 'labels']
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(issues_data)
            
            print(f"Issues saved to: {filename}")
        except IOError as e:
            print(f"Error saving CSV file: {e}")
            sys.exit(1)

    def save_to_text(self, issues_data: List[Dict], filename: str):
        """
        Save issues to plain text format with specific formatting.
        
        Args:
            issues_data (List[Dict]): List of extracted issue data
            filename (str): Output text filename
        """
        if not issues_data:
            print("No issues to save.")
            return

        try:
            with open(filename, 'w', encoding='utf-8') as textfile:
                for i, issue in enumerate(issues_data):
                    # Format: title, body, opened, closed with --- separators
                    textfile.write("---\n")
                    textfile.write(f"title: {issue['title']}\n")
                    textfile.write(f"body: {issue['body']}\n")
                    textfile.write(f"opened: {issue['opened']}\n")
                    textfile.write(f"closed: {issue['closed'] or 'Not closed'}\n")
                    textfile.write("---\n")
                    
                    # Add extra newline between issues for readability
                    if i < len(issues_data) - 1:
                        textfile.write("\n")
            
            print(f"Issues saved to: {filename}")
        except IOError as e:
            print(f"Error saving text file: {e}")
            sys.exit(1)

    def download_and_save(self, owner: str, repo: str, output_format: str, 
                         output_file: Optional[str] = None, state: str = 'all'):
        """
        Download issues and save them in the specified format.
        
        Args:
            owner (str): Repository owner
            repo (str): Repository name
            output_format (str): Output format ('csv' or 'text')
            output_file (Optional[str]): Output filename
            state (str): Issue state filter
        """
        # Fetch all issues
        issues = self.get_all_issues(owner, repo, state)
        
        if not issues:
            print("No issues found.")
            return
        
        # Extract relevant data
        issues_data = [self.extract_issue_data(issue) for issue in issues]
        
        # Generate filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            extension = 'csv' if output_format == 'csv' else 'txt'
            output_file = f"{owner}_{repo}_issues_{timestamp}.{extension}"
        
        # Save in the requested format
        if output_format == 'csv':
            self.save_to_csv(issues_data, output_file)
        else:
            self.save_to_text(issues_data, output_file)


def main():
    parser = argparse.ArgumentParser(
        description='Download all issues from a GitHub repository',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s microsoft/vscode --format csv
  %(prog)s facebook/react --format text --output react_issues.txt
  %(prog)s --token YOUR_TOKEN torvalds/linux --format csv --state closed
        """
    )
    
    parser.add_argument('repository', 
                       help='Repository in format "owner/repo" (e.g., "microsoft/vscode")')
    
    parser.add_argument('--format', '-f', 
                       choices=['csv', 'text'], 
                       default='csv',
                       help='Output format (default: csv)')
    
    parser.add_argument('--output', '-o', 
                       help='Output filename (default: auto-generated)')
    
    parser.add_argument('--state', '-s', 
                       choices=['open', 'closed', 'all'], 
                       default='all',
                       help='Issue state to download (default: all)')
    
    parser.add_argument('--token', '-t', 
                       help='GitHub personal access token (optional, increases rate limits)')
    
    args = parser.parse_args()
    
    # Parse repository argument
    try:
        owner, repo = args.repository.split('/')
    except ValueError:
        parser.error('Repository must be in format "owner/repo"')
    
    # Initialize downloader
    downloader = GitHubIssuesDownloader(token=args.token)
    
    # Download and save issues
    try:
        downloader.download_and_save(
            owner=owner,
            repo=repo,
            output_format=args.format,
            output_file=args.output,
            state=args.state
        )
    except KeyboardInterrupt:
        print("\nDownload cancelled by user.")
        sys.exit(0)


if __name__ == '__main__':
    main()