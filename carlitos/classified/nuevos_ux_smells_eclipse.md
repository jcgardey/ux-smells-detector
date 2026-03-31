# Nuevos UX smells agregados al catálogo
Este documento resume los nuevos smells identificados en la clasificación de issues del repositorio `eclipse-platform/eclipse.platform.ui`.
Se detectaron **17 nuevos smells** fuera del catálogo original.
Para cada smell se incluye: qué describe, cómo detectarlo y una referencia rápida a su aparición en el dataset clasificado.
## Resumen rápido
- **Accessibility Barrier** — 6 issues clasificados.
- **Hard-to-Scan Layout** — 2 issues clasificados.
- **Hidden Relevant Action** — 1 issues clasificados.
- **Interaction Friction** — 3 issues clasificados.
- **Interaction Inconsistency** — 5 issues clasificados.
- **Layout Instability** — 3 issues clasificados.
- **Low Contrast** — 10 issues clasificados.
- **Low Visibility State** — 4 issues clasificados.
- **Misleading Confirmation** — 1 issues clasificados.
- **Misleading Preview** — 1 issues clasificados.
- **Misleading Status Message** — 1 issues clasificados.
- **Misplaced Feedback** — 4 issues clasificados.
- **Overly Intrusive Feedback** — 7 issues clasificados.
- **Unmatched Container Size** — 6 issues clasificados.
- **Visual Imbalance** — 1 issues clasificados.
- **Visual Inconsistency** — 57 issues clasificados.
- **Visual Noise** — 6 issues clasificados.

## Accessibility Barrier
**Qué es:** Problemas de interacción o presentación que obstaculizan el uso con lectores de pantalla, navegación por teclado, focos, autoscroll inesperado o textos no leídos correctamente. No implica una falla funcional general, sino una barrera de accesibilidad.
**Cómo detectarlo:**
- Buscar reportes sobre JAWS, screen readers, Tab, foco, lectura duplicada o contenido que no se anuncia.
- Detectar frases como 'cannot be read', 'doesn't read', 'keyboard navigation', 'focus', 'accessible'.
- Clasificar aquí cuando el problema principal sea que una persona no puede percibir o recorrer la interfaz correctamente.
**Señal empírica en el dataset:** 6 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #272 [a11y] Accessibility - EnablementDialog Enable the required activity? cannot be read by JAWS; #343 JAWS 2022 reads a Control's Group names twice; #848 Inconsistent of accessibility in wizard (Back, Finish buttons).

## Hard-to-Scan Layout
**Qué es:** Distribución, orden o alineación que vuelve difícil recorrer visualmente la información, aunque los elementos estén presentes y funcionen.
**Cómo detectarlo:**
- Buscar reportes sobre desorden, listas sin ordenar, alineación extraña o agrupación confusa.
- Señales frecuentes: 'unsorted', 'align', 'hard to read', 'hard to scan'.
- Usarlo cuando el costo principal sea cognitivo por mala organización visual.
**Señal empírica en el dataset:** 2 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #201 Startup preference page is unsorted; #788 Align suggested Keybindings.

## Hidden Relevant Action
**Qué es:** Una acción útil para la tarea existe o debería estar disponible en contexto, pero está oculta, demasiado enterrada o cuesta descubrirla.
**Cómo detectarlo:**
- Buscar reportes sobre acciones difíciles de encontrar o ausentes en el lugar esperado.
- Palabras típicas: 'no menu item', 'missing in context menu', 'hard to discover', 'should be here'.
- Diferenciarlo de feature request: aquí la acción ya forma parte del flujo esperado y su ocultamiento degrada la UX.
**Señal empírica en el dataset:** 1 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #273 Cheat Sheets - No menu item for reattaching a detached cheat sheet.

## Interaction Friction
**Qué es:** La manipulación directa resulta torpe, incómoda o innecesariamente costosa, aunque técnicamente sea posible completar la tarea.
**Cómo detectarlo:**
- Buscar reportes sobre drag and drop incómodo, cierres lentos o gestos que 'se sienten más difíciles'.
- Claves comunes: 'harder', 'awkward', 'not working correctly', 'difficult to drag/drop'.
- Aplicarlo cuando el problema central sea el esfuerzo físico o operativo extra.
**Señal empírica en el dataset:** 3 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #156 Close Tabs with the middle button within chevron; #855 Drag and Drop for Eclipse not Working Correctly in Gnome (Ubuntu 22.04); #3135 Drag and drop of views to other stacks is "harder".

## Interaction Inconsistency
**Qué es:** La interfaz responde de una forma distinta a la convención esperada o a la conducta aprendida por el usuario, generando sorpresa o errores.
**Cómo detectarlo:**
- Buscar comparaciones con comportamientos esperados de teclado, edición, navegación o selección.
- Indicadores: 'should', 'expected', 'instead', 'common convention', 'breaks behavior'.
- Usarlo cuando el sistema hace algo funcional, pero en una forma inconsistente con patrones conocidos.
**Señal empírica en el dataset:** 5 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #46 JFace: Tab key after 2nd click in a cell editor skips a row; #205 project explorer tree view: make Left key jump to item parent; #233 Next Editor only cycles between two editors.

## Layout Instability
**Qué es:** La interfaz se mueve, salta o reacomoda durante la interacción, rompiendo la continuidad visual y la concentración.
**Cómo detectarlo:**
- Buscar reportes de 'jumping', 'shifts', 'moves', 'reflows', 'toolbar jumps'.
- Identificar inserciones tardías de contenido, placeholders ausentes o cambios de posición entre estados.
- Aplicarlo cuando el problema principal sea la inestabilidad espacial de la UI.
**Señal empírica en el dataset:** 3 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #889 Code Mining: Show empty pesudo-line before code mining is 'calculated'; #1691 Position toolbar navigation buttons on the left -> Stop them from jumping on navigating between different editor types (java, plugin.xml, ...); #3723 Prevent editor "jumping" by using placeholders for Code Minings.

## Low Contrast
**Qué es:** Texto, selección o estados visuales con contraste insuficiente para distinguir contenido o controles con comodidad.
**Cómo detectarlo:**
- Buscar reportes sobre texto ilegible, dark theme, contrast theme, barely visible o inactive/active indistinguishable.
- Palabras frecuentes: 'not readable', 'barely visible', 'contrast', 'indistinguishable'.
- Clasificar aquí cuando el problema principal sea perceptual y no un error de estado o funcionalidad.
**Señal empírica en el dataset:** 10 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #26 Tab text in classic theme not readable ; #786 Form editors with Windows 11 Contrast Theme "Aquatic" not correctly shown; #1123 [Eclipse 4.28.0] [Bug bounty US$50.00] Dark theme: inactive dialog buttons are indistinguishable from active ones.

## Low Visibility State
**Qué es:** El sistema tiene estados distintos, pero el cambio visual entre ellos es demasiado sutil para percibirse con fiabilidad.
**Cómo detectarlo:**
- Buscar reportes sobre botones seleccionados, toggles o estados activos que no se destacan.
- Claves: 'not highlighted', 'state not visible', 'selected looks the same', 'down state'.
- Diferenciarlo de Low Contrast cuando el problema sea la falta de diferenciación entre estados.
**Señal empírica en el dataset:** 4 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #94 Code Mining: code mining background should not remain unchanged when selected; #340 [Eclipse 4.25 Dark Theme] View action buttons are not highlighted; #467 SWT Dark Theme ToolItem Toggle Buttons not showing down state.

## Misleading Confirmation
**Qué es:** El mensaje de confirmación describe consecuencias distintas de las que realmente ejecuta el sistema.
**Cómo detectarlo:**
- Buscar reportes donde el texto de confirmación prometa seguridad o un resultado que luego no ocurre.
- Claves: 'pretending', 'says X but does Y', 'confirmation is misleading'.
- Aplicarlo cuando el daño UX provenga de una confirmación engañosa, no del bug aislado.
**Señal empírica en el dataset:** 1 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #3652 deletes original files when pretending to delete only linked files (APPALLING).

## Misleading Preview
**Qué es:** La vista previa no representa fielmente el resultado final, por lo que induce expectativas incorrectas.
**Cómo detectarlo:**
- Buscar reportes sobre previews 'useless', 'not representative', 'doesn't show actual result'.
- Comparar si la queja central es la discrepancia entre vista previa y resultado real.
- Usarlo cuando el preview comunica mal el efecto de una configuración o acción.
**Señal empírica en el dataset:** 1 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #247 "Colors and Fonts" Preview useless.

## Misleading Status Message
**Qué es:** El texto de estado, progreso o resumen describe incorrectamente lo que el sistema está mostrando o haciendo.
**Cómo detectarlo:**
- Buscar reportes sobre contadores, mensajes de progreso o resúmenes inconsistentes con el estado real.
- Palabras típicas: 'incorrectly reports', 'wrong count', 'message says'.
- Aplicarlo cuando la falla UX sea la interpretación errónea causada por el mensaje.
**Señal empírica en el dataset:** 1 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #3720 File search incorrectly reports shown matches (shown file count vs shown match count).

## Misplaced Feedback
**Qué es:** Un control, popup, nodo expandible o feedback aparece en un lugar inesperado o fuera del foco de atención del usuario.
**Cómo detectarlo:**
- Buscar reportes sobre diálogos detrás de otras ventanas, popups en monitor incorrecto o controles en secciones equivocadas.
- Señales: 'wrong place', 'behind all windows', 'appears in the wrong place'.
- Usarlo cuando el problema principal sea la ubicación espacial del feedback o control.
**Señal empírica en el dataset:** 4 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #85 The default button in FiltersConfigurationDialog is in the wrong section; #752 Create New Source Folder dialog is behind all other windows and inaccessible; #1417 Expandable node is shown at wrong place, sorting broken after expand.

## Overly Intrusive Feedback
**Qué es:** Popups, overlays, prompts o bloqueos interrumpen demasiado la tarea, tapan contenido o exigen atención excesiva.
**Cómo detectarlo:**
- Buscar reportes sobre diálogos modales, prompts redundantes, overlays que tapan el cursor o bloquean el trabajo.
- Palabras comunes: 'blocking', 'modal', 'hides cursor', 'interrupts', 'reopens'.
- Diferenciarlo de No Processing Page: aquí sí hay feedback, pero es demasiado invasivo.
**Señal empírica en el dataset:** 7 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #48 The key binding shown hides cursor; #149 Remove or disable Workspace version check dialog; #173 ISaveablePart2.promptToSaveOnClose() invoke on "Save All".

## Unmatched Container Size
**Qué es:** El tamaño mínimo o comportamiento de redimensionado de un contenedor no acompaña el contenido: clippea información o desperdicia espacio.
**Cómo detectarlo:**
- Buscar reportes sobre diálogos demasiado pequeños, overlays que no se adaptan o ventanas que deberían redimensionarse.
- Claves: 'too small', 'resize', 'minimum size', 'clipped', 'wastes space'.
- Diferenciarlo de Unmatched Input Size: aquí el problema es del contenedor o diálogo, no de un campo puntual.
**Señal empírica en el dataset:** 6 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #165 Allow to resize launcher dialog; #1257 Poor resizing behavior for resource filters; #1511 Wizard is too small. Regression of https://github.com/eclipse-platform/eclipse.platform.ui/pull/1283.

## Visual Imbalance
**Qué es:** Un elemento visual domina desproporcionadamente la composición y rompe la jerarquía visual esperada.
**Cómo detectarlo:**
- Buscar reportes sobre íconos, botones o componentes 'too big' o visualmente desbalanceados.
- Indicadores: 'too big', 'dominates', 'out of proportion'.
- Aplicarlo cuando el problema central sea la jerarquía visual, no la inconsistencia entre temas.
**Señal empírica en el dataset:** 1 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #3793 Search icon to big.

## Visual Inconsistency
**Qué es:** Elementos equivalentes o estados comparables cambian de estilo, color, fondo o apariencia sin una lógica clara entre temas, vistas o contextos.
**Cómo detectarlo:**
- Buscar reportes sobre dark theme/light theme, fondos distintos, iconos desalineados o estilos que varían entre lugares similares.
- Claves: 'inconsistent', 'wrong background', 'theme', 'different color', 'misaligned'.
- Usarlo cuando la UI se perciba incoherente aunque cada parte individual pueda funcionar.
**Señal empírica en el dataset:** 57 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #3 Disable or fix System theme on Windows; #9 Workspace launcher theme.; #82 Add support to parameterize preference section of the theme css.

## Visual Noise
**Qué es:** Elementos decorativos, líneas, gradientes o información duplicada agregan ruido visual sin aportar comprensión ni acción.
**Cómo detectarlo:**
- Buscar reportes sobre duplicación de texto, gradientes innecesarios, líneas grises, información repetida o adornos molestos.
- Palabras típicas: 'duplicate', 'double information', 'remove line', 'gradient', 'clutter'.
- Aplicarlo cuando convenga simplificar la interfaz para reducir distracción.
**Señal empírica en el dataset:** 6 issues clasificados bajo este smell.
**Ejemplos en Eclipse:** #114 Remove forms default gradient and use a SWT color constant; #152 Quick access twice the same entry; #188 Remove gray line on top of forms.

## Diferencias útiles entre smells parecidos
- **Low Contrast** vs **Low Visibility State**: el primero afecta legibilidad/percepción general; el segundo afecta distinguir estados activos, seleccionados o presionados.
- **Visual Inconsistency** vs **Visual Noise**: inconsistency trata la incoherencia entre elementos/estados; noise trata decoración o repetición innecesaria.
- **Interaction Inconsistency** vs **Interaction Friction**: inconsistency rompe convenciones; friction mantiene el flujo posible pero lo vuelve torpe o costoso.
- **Misplaced Feedback** vs **Overly Intrusive Feedback**: misplaced trata ubicación incorrecta; intrusive trata interrupción excesiva.
- **Unmatched Input Size** vs **Unmatched Container Size**: input size afecta campos puntuales; container size afecta diálogos, overlays o paneles enteros.
