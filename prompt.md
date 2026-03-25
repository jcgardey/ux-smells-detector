Necesito que actues como un modelo de prediccion. Te voy a indicar (en un archivo separado) una serie de issues reportados por otros usuarios (separados por title y body) en un repositorio de código de github y necesito que me indiques si cada uno corresponde a un UX smell o no. Para determinar si es un UX smell, tene en cuenta las siguientes definiciones:

"Un UX Smell indica deficiencias en la experiencia de los usuarios provista por un sistema que pueden mejorarse sin modificar la funcionalidad de la aplicacion. No son bugs ni feature requests."

Un Bug se identifica porque describe un comportamiento incorrecto o la descripción incluye los términos  "error" o "bug" explícitamente.

Un Feature request es una solicitud de introducción de una funcionalidad que no está disponible actualmente. Puede incluir el texto "feature request", "request" o  descripciones como: "Pasos: * Instalar la extensión de RemoteHub en el escritorio * Abrir un repositorio desde el escritorio * Realizar un cambio * Descartar el cambio => 🐛 Obtienes un cuadro de diálogo personalizado, aunque esperaba uno nativo." o "We plan to update user profiles to support AI-first workflows (profile contents for chat configurations, profile descriptions, layouts that center AI) with the goal of providing AI-first profile templates. Current templates are not optimized for AI-first scenarios"

Si el issue no se relaciona con aspectos de la experiencia de usuario, la categoria es "No UX".

Si consideras que es un UX smell indicame a cual de los smells definidos en el archivo smells.md corresponde.

Dame los resultados en un archivo csv con los datos de cada issue y las columnas 'ux_smell' (uno de los valores anteriores o None si no aplica) y'reasoning' (string) explicando brevemente el razonamiento con no más de 25 palabras. Si el issue cumple con la definicion general de UX smell pero no se ajusta a ninguno de los tipos anteriores, agrega el tipo que consideres en 'ux_smell' y explicalo en 'reasoning'. Los tipos que agregues deben representar patrones recurrentes, aplicables en diferentes contextos.  