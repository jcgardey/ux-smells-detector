# Resumen de issues y nuevos UX smells detectados en Eclipse Platform UI

Este documento resume el resultado del archivo `issues_only_predicted.csv`, generado a partir de 1273 issues del repositorio `eclipse-platform/eclipse.platform.ui`.

## 1. Panorama general del dataset

- **Total de issues analizados:** 1273
- **Clasificados como UX smell:** 237 (18.6%)
- **Clasificados como Bug:** 621 (48.8%)
- **Clasificados como Feature request:** 130 (10.2%)
- **Clasificados como No UX:** 285 (22.4%)

Interpretación rápida: la mayoría de los issues del repositorio no describen smells de UX sino bugs, pedidos de funcionalidad o temas internos. Sin embargo, el volumen de smells UX no es menor y muestra patrones bastante consistentes.

## 2. Distribución de UX smells detectados

| UX smell | Cantidad | % del total | % dentro de UX smells |
|---|---:|---:|---:|
| Poor discoverability | 51 | 4.0% | 21.5% |
| General UI Inconsistency | 33 | 2.6% | 13.9% |
| Poor accessibility | 29 | 2.3% | 12.2% |
| Inconsistent placement | 24 | 1.9% | 10.1% |
| Inconsistent Theming | 21 | 1.6% | 8.9% |
| Clipped/Overlapping UI | 18 | 1.4% | 7.6% |
| Inconsistent Spacing/Alignment | 17 | 1.3% | 7.2% |
| Visual Noise | 13 | 1.0% | 5.5% |
| Wrong Default Value | 8 | 0.6% | 3.4% |
| Undescriptive Element | 7 | 0.5% | 3.0% |
| Unresponsive Element | 5 | 0.4% | 2.1% |
| Forced Bulk Action | 4 | 0.3% | 1.7% |
| No Processing Page | 3 | 0.2% | 1.3% |
| Useless Search Results | 3 | 0.2% | 1.3% |
| Distant Content | 1 | 0.1% | 0.4% |

## 3. Qué entiendo aquí por “nuevos smells detectados”

Tomo como **nuevos smells detectados** a los que no pertenecen al núcleo clásico del catálogo base (por ejemplo: `Undescriptive Element`, `No Processing Page`, `Wrong Default Value`, etc.) y que, aun así, aparecieron con fuerza en el dataset.

En esta corrida se detectaron **8 smells nuevos** con ocurrencias efectivas:

- **Poor discoverability** — 51 issues
- **General UI Inconsistency** — 33 issues
- **Poor accessibility** — 29 issues
- **Inconsistent placement** — 24 issues
- **Inconsistent Theming** — 21 issues
- **Clipped/Overlapping UI** — 18 issues
- **Inconsistent Spacing/Alignment** — 17 issues
- **Visual Noise** — 13 issues

Además, en `smells.md` existían dos smells extendidos que **no aparecieron** en esta clasificación: `Overloaded Menus` e `Inconsistent feedback`.

## 4. Detalle de los nuevos smells detectados

### Poor discoverability

**Qué describe:** La interfaz no ofrece señales visuales suficientes para que el usuario encuentre una función, acción o recorrido disponible.

**Por qué importa:** Es el smell más frecuente del dataset y sugiere que muchas capacidades existen, pero no se descubren fácilmente.

**Cómo suele detectarse en los issues:** Suele aparecer en issues que hablan de acciones difíciles de encontrar, menús esperados que no están visibles o atajos poco evidentes.

**Presencia en este dataset:** 51 issues (21.5% de los UX smells; 4.0% del total).

**Ejemplos representativos:**
- #10 — Add an e4 way to register a command/handler as an "open action"
- #91 — Allow to configure UI defaults for new workspaces
- #248 — Switching Perspective should close hidden Perspective

### General UI Inconsistency

**Qué describe:** Hay incoherencias visuales o de comportamiento entre componentes similares que no encajan mejor en theming, placement o spacing.

**Por qué importa:** Indica deuda UX transversal: la experiencia se siente desigual según la vista, diálogo o plataforma.

**Cómo suele detectarse en los issues:** Aparece en reportes sobre comportamientos visuales raros, estilos distintos entre contextos o diferencias difíciles de justificar.

**Presencia en este dataset:** 33 issues (13.9% de los UX smells; 2.6% del total).

**Ejemplos representativos:**
- #289 — ArrayIndexOutOfBoundsException in org.eclipse.ui.internal.SaveablesList in Eclipse 4.25 M2
- #443 — [Only for Windows] ToolBar gets resized when mixing ToolItems with text(no icon) and with items with icons
- #617 — Improvement for the WizardProjectsImportPage

### Poor accessibility

**Qué describe:** La UI presenta problemas de contraste, visibilidad o compatibilidad con lectores de pantalla y navegación asistiva.

**Por qué importa:** Impacta directamente la inclusión y la posibilidad de uso para personas con necesidades de accesibilidad.

**Cómo suele detectarse en los issues:** Suele detectarse en issues que mencionan JAWS, screen readers, contraste insuficiente, texto ilegible o estados visuales poco perceptibles.

**Presencia en este dataset:** 29 issues (12.2% de los UX smells; 2.3% del total).

**Ejemplos representativos:**
- #26 — Tab text in classic theme not readable 
- #64 — IconAndMessageDialog / TitleAreaDialog: Improve accessibility of info/warning/error icon
- #170 — Exceptions when refreshing virtual tree after updating model

### Inconsistent placement

**Qué describe:** La ubicación de una acción, control o elemento entra en conflicto con lo que el usuario espera según la convención o el contexto.

**Por qué importa:** Aumenta el costo de aprendizaje y hace que acciones comunes parezcan “escondidas” o mal ubicadas.

**Cómo suele detectarse en los issues:** Aparece en reportes donde algo debería estar en otro lugar: botones, ítems de menú, secciones o entradas del wizard.

**Presencia en este dataset:** 24 issues (10.1% de los UX smells; 1.9% del total).

**Ejemplos representativos:**
- #13 — Add support for "Icon Packs" 
- #85 — The default button in FiltersConfigurationDialog is in the wrong section
- #426 — Provide missing Databinding methods for the generified variants of the now deleted non-generic variants

### Inconsistent Theming

**Qué describe:** Tokens, colores o estilos de tema se aplican de manera desigual entre componentes o vistas.

**Por qué importa:** Es una señal clara de deuda visual, especialmente en dark mode y configuraciones cross-platform.

**Cómo suele detectarse en los issues:** Se observa en issues sobre fondos incorrectos, colores inesperados, widgets que no respetan el tema o diferencias entre light/dark mode.

**Presencia en este dataset:** 21 issues (8.9% de los UX smells; 1.6% del total).

**Ejemplos representativos:**
- #3 — Disable or fix System theme on Windows
- #176 — Ugly source code colorscheme after change theme to "System theme"
- #188 — Remove gray line on top of forms

### Clipped/Overlapping UI

**Qué describe:** Elementos de la interfaz aparecen recortados, superpuestos o sin espacio suficiente para mostrarse correctamente.

**Por qué importa:** Afecta legibilidad, percepción de calidad y, en algunos casos, uso efectivo de la UI.

**Cómo suele detectarse en los issues:** Suele aparecer cuando se mencionan labels cortados, elipsis persistentes, textos truncados o elementos superpuestos.

**Presencia en este dataset:** 18 issues (7.6% de los UX smells; 1.4% del total).

**Ejemplos representativos:**
- #388 — Bad first impression (HiDPI, dark mode, …)
- #636 — Preferences: ellipsis stays after maximizing the window
- #1185 — Possible problem in file org/eclipse/jface/text/contentassist/CompletionProposalPopup.java#L1248

### Inconsistent Spacing/Alignment

**Qué describe:** El espaciado, padding, orden o alineación entre elementos no es consistente y reduce la claridad visual.

**Por qué importa:** Aunque parece menor, este smell aumenta la carga cognitiva y la sensación de interfaz poco pulida.

**Cómo suele detectarse en los issues:** Aparece en issues sobre mala alineación, centrados incorrectos, listas desordenadas o layouts difíciles de escanear.

**Presencia en este dataset:** 17 issues (7.2% de los UX smells; 1.3% del total).

**Ejemplos representativos:**
- #404 — JFace RowLayoutFactory does not copy center option
- #753 — Alignment in Onboarding should be improved
- #788 — Align suggested Keybindings

### Visual Noise

**Qué describe:** La UI contiene elementos decorativos, redundantes o repetitivos que agregan ruido sin aportar comprensión.

**Por qué importa:** Suele asociarse a gradientes innecesarios, duplicación de información o detalles visuales que distraen.

**Cómo suele detectarse en los issues:** Se detecta en reportes sobre información duplicada, gradientes molestos, líneas innecesarias o elementos que “ensucian” la interfaz.

**Presencia en este dataset:** 13 issues (5.5% de los UX smells; 1.0% del total).

**Ejemplos representativos:**
- #114 — Remove forms default gradient and use a SWT color constant
- #173 — ISaveablePart2.promptToSaveOnClose() invoke on "Save All"
- #336 — Reduce double information in Import Wizard

## 5. Hallazgos interpretativos

### 5.1 El problema dominante es la descubrilidad

`Poor discoverability` es el smell más frecuente. Esto sugiere que en Eclipse muchas capacidades existen, pero los usuarios no reciben señales claras para encontrarlas o entender cómo acceder a ellas.

### 5.2 La deuda UX es fuertemente visual y transversal

La combinación de `General UI Inconsistency`, `Inconsistent Theming`, `Inconsistent placement`, `Clipped/Overlapping UI` e `Inconsistent Spacing/Alignment` muestra que una parte importante de la deuda UX está en la **coherencia visual y estructural** de la interfaz.

### 5.3 La accesibilidad aparece como un eje relevante

`Poor accessibility` aparece con bastante peso. Esto es importante porque no se trata solo de una mejora estética: afecta legibilidad, visibilidad y compatibilidad con tecnologías asistivas.

### 5.4 Los smells clásicos existen, pero con menor peso

Smells como `Wrong Default Value`, `Undescriptive Element`, `Unresponsive Element`, `Forced Bulk Action` o `No Processing Page` aparecen, pero en menor cantidad que los problemas de coherencia visual y descubrilidad.

## 6. Qué conviene tener en cuenta al interpretar estos resultados

- Esta clasificación es **predictiva**: resume patrones plausibles a partir del texto de los issues.
- Algunos issues pueden mezclar varias cosas a la vez (bug + problema UX + pedido de mejora), por lo que el label final simplifica un caso más rico.
- En varios repositorios maduros, la frontera entre **bug visual**, **issue de theming** y **UX smell** no siempre es completamente nítida.
- Aun con esa limitación, la distribución observada es útil para detectar **zonas de deuda UX**: discoverability, consistencia visual, accesibilidad y layout.

## 7. Conclusión breve

Los issues clasificados sugieren que la deuda UX de Eclipse Platform UI no está concentrada solo en errores funcionales visibles, sino también en patrones de interacción y presentación que degradan la experiencia sin requerir cambios funcionales profundos. Entre los smells nuevos detectados, dominan los relacionados con **descubrilidad**, **consistencia visual**, **accesibilidad** y **estructura del layout**, lo que ofrece una base clara para discutir UX debt en IDEs maduros y comparar estos patrones con otros entornos como Visual Studio Code.
