

## Undescriptive Element 

Todo componente interactivo de una interfaz, ya sea un boton, un link u otro tipo de control, necesita de un significante claro, es decir alguna pista que muestre al usuario lo que se puede hacer con el. Cuando esto no sucede, los usuarios pueden no encontrar el control que necesitan para completar una tarea. A veces, sin embargo, puede suceder lo opuesto: un usuario puede encontrarse con un elemento que no puede comprender para que sirve en un primer vistazo. En estos casos, un comportamiento normal para investigar su proposito consiste posar el mouse sobre el control, dejarlo quieto unos instantes, y esperar que aparezca un tooltip.
Cuando muchos usuarios intentan obtener una ayuda tipo tooltip de un elemento de la interfaz, esto puede indicar que el elemento no es suficientemente auto-descriptivo. Segun las guias de diseño para desarrolladores de Windows 10: "Una ayuda valiosa ayudara a aclarar una accion poco clara".
Como ejemplo, se encontro que los usuarios posaban el mouse sobre sus nombres buscando una opcion de log out para salir del sistema. Los nombres de usuario fueron eliminados de este encabezado en versiones posteriores de Google Drive.

## Misleading Link

Ante la falta de descripcion de un link, los usuarios pueden buscar un tooltip que los ayude a aclarar adonde los llevaria, pero se ha observado otro comportamiento mas practico para averiguar esto: presionar el link. Los usuarios que optan por esta opcion generalmente dan un rapido vistazo y retornan a la pagina de origen.
El smell Misleading Link es similar a Undescriptive Element pero especifico para links. Se detecta cuando muchos usuarios buscan un tooltip del elemento o cuando existe una navegacion muy rapida de ida y vuelta, que, de reiterarse, puede interpretarse como un arrepentimiento al ver que el contenido buscado no esta presente.
Un ejemplo comun de un vinculo pobremente descripto es el usual "click aqui", que puede llevar a un contenido que el usuario no espera.

---

## No Processing Page

La falta de feedback produce incertidumbre en los usuarios, en particular la falta mensajes que informan sobre procesos largos. En el contexto de las aplicaciones web, cuando un usuario presiona un boton o un link, espera una respuesta con cierta inmediatez.
Existen tres niveles de demora caracteristicos:

* 0.1 segundo: el sistema parece instantaneo.
* 1 segundo: el retraso es perceptible pero no interrumpe el pensamiento.
* 10 segundos: se necesita indicar que el sistema sigue procesando.
  Este tipo de feedback evita confusion y mejora la percepcion del rendimiento.

---

## Free Input For Limited Values

Se detecta cuando un campo de texto libre se usa para ingresar datos de un rango limitado, como ciudades o paises. Los usuarios deben escribir valores completos cuando podrian elegir de una lista.
Si las opciones son pocas, un select o radio buttons son mas apropiados; si son muchas, un autocompletado mejora la experiencia.

---

## Unformatted Input

Campos que requieren un formato especifico (como fechas, telefonos o codigos postales) no ayudan al usuario a ingresarlo correctamente.
El formulario deberia guiar al formato correcto o aplicar formato automatico. Usar calendarios o mascaras de entrada mejora la satisfaccion y reduce errores.

---

## Unmatched Input Size

Ocurre cuando el tamaño del campo de texto no coincide con la longitud esperada del dato.
Un campo demasiado corto oculta texto; uno muy largo confunde sobre lo que se espera ingresar. Ajustar el tamaño ayuda al usuario a comprender el tipo de dato requerido.

---

## Forced Bulk Action

Las aplicaciones que requieren seleccionar multiples items y aplicar acciones en lote pueden ser ineficientes si el usuario solo desea actuar sobre un elemento.
Este smell aparece cuando no hay una forma rapida de aplicar acciones individuales.

---

## Overlooked Content

Contenido que los usuarios pasan por alto al hacer scroll rapidamente.
Si los usuarios siempre se detienen en una misma seccion, el contenido importante deberia ubicarse mas arriba. Este smell indica que informacion relevante puede estar siendo ignorada.

---

## Distant Content

Detecta patrones de navegacion en los que los usuarios deben atravesar demasiados pasos o paginas intermedias para llegar al contenido buscado.
Indica que el camino hacia el objetivo es demasiado largo y puede simplificarse.

---

## No Client Validation

Se produce cuando los errores en formularios se detectan solo del lado del servidor, luego de recargar la pagina.
Esto genera frustracion y dificulta entender los errores. La validacion deberia ocurrir en el cliente, en tiempo real.

---

## Late Validation 

Similar al anterior, pero ocurre cuando la validacion se hace del lado del cliente solo al presionar "Enviar".
Puede mejorarse aplicando validacion por campo, en el momento en que el usuario abandona cada campo (*inline validation*).

---

## Abandoned Form 

Formularios largos o complejos suelen ser abandonados por los usuarios antes de completarse.
Este smell se detecta cuando la tasa de abandono es alta, indicando problemas de diseno o exceso de campos.

---

## Scarce Search Results 

Ocurre cuando un formulario de busqueda devuelve pocos o ningun resultado util la mayoria de las veces.
Indica problemas en el motor de busqueda o en la forma en que los usuarios formulan sus consultas.

---

## Useless Search Results 

Se detecta cuando las busquedas arrojan resultados que los usuarios raramente seleccionan.
Aunque aparezcan resultados, pueden no coincidir con las expectativas del usuario o ser irrelevantes.

---

## Wrong Default Value 

El valor seleccionado por defecto en una lista o select no coincide con la opcion mas comun o esperada.
Elegir valores por defecto inteligentes (*smart defaults*) reduce tiempo de completado y mejora la satisfaccion.

---

## Unresponsive Element 

Se produce cuando un elemento parece interactivo pero no responde a los clics del usuario.
Ejemplos comunes incluyen imagenes, titulos o textos subrayados que no ejecutan ninguna accion al presionarse.

---
