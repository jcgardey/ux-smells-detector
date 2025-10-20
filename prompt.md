Necesito que actues como un modelo de prediccion. Te voy a indicar una serie de issues reportados por otros usuarios (separados por titulo y descripcion) en un repositorio de código de github y necesito que me indiques si cada uno corresponde a un UX smell o no. Los UX smells indican deficiencias en la experiencia de los usuarios, no son bugs ni feature requests. Reportan problemas de UX que pueden mejorarse sin modificar la funcionalidad de la aplicacion. Si consideras que es un UX smell indicame a cual de los siguientes corresponde:

- Undescriptive Element: El componente no comunica claramente su función; el usuario no entiende qué acción realiza.
- Misleading Link: Un enlace confunde sobre su destino o propósito, provocando navegación innecesaria.
- No Processing Page: Falta retroalimentación visual durante procesos largos, generando incertidumbre.
- Free Input for Limited Values:** Se usa un campo de texto libre cuando las opciones posibles son limitadas.
- Unformatted Input: El campo no guía al usuario sobre el formato esperado (ej. fecha, teléfono).- Unmatched Input Size: El tamaño del campo no corresponde a la longitud del dato esperado.
- Forced Bulk Action: Se obliga a usar acciones en lote aunque el usuario quiera actuar sobre un solo ítem.
- Overlooked Content: Contenido importante pasa inadvertido porque los usuarios lo saltan al hacer scroll.
- Distant Content: El contenido relevante está demasiado lejos en la estructura de navegación.
- No Client Validation: Los errores se detectan solo en el servidor, tras enviar el formulario.
- Late Validation: La validación ocurre recién al enviar el formulario, no mientras se completa.
- Abandoned Form: Los usuarios abandonan formularios por su complejidad o extensión excesiva.
- Scarce Search Results: Las búsquedas devuelven pocos o ningún resultado útil.
- Useless Search Results: Las búsquedas arrojan resultados irrelevantes que los usuarios no seleccionan.
- Wrong Default Value: El valor por defecto no coincide con la opción más común o esperada.
- Unresponsive Element: Un elemento parece interactivo, pero no responde al clic del usuario.

Responde en formato json (sin texto adicional) con un objeto por cada issue las siguientes claves: 'ux_smell' (uno de los valores anteriores o None si no aplica), 'reasoning' (string) explicando brevemente el razonamiento con no más de 25 palabras. Si el issue cumple con la definicion general de UX smell pero no se ajusta a ninguno de los tipos anteriores, agrega el tipo que consideres en 'ux_smell' y explicalo en 'reasoning'.  