# Resumen de Distribución de Muestra de Issues (Evaluación de 10%)

Como parte de la validación cruzada y evaluación de la calidad de clasificación del modelo de IA, se ha extraído de manera aleatoria una muestra del 10% equivalente de los issues para el equipo de revisión.

## 📊 Estadísticas Generales del Dataset Original
Del dataset inicial clasificado (`issues_only_predicted.csv`) se detectaron en total **1,273 issues con clasificación válida**:
* **Total de issues SIN Smell (No-Smells):** 1,036 issues
  * Categorizados como: `Bug`, `No UX`, o `Feature request`.
* **Total de issues CON Smell (Smells):** 237 issues
  * Categorizados con cualquier etiqueta restante (ej. `Inconsistent Theming`, `Poor discoverability`, etc).

## 🧑‍🤝‍🧑 Asignación para el Equipo
De acuerdo con las previsiones, cada miembro del equipo debe revisar la parte proporcional de ese 10%, conformada equitativamente en tipos. A cada usuario se le construyó un subset de **127 issues en total**.

Las proporciones elegidas para equilibrar la métrica fueron las siguientes:
* **64 Issues tipo Smell**
* **63 Issues tipo No-smell**

### Miembros y sus Archivos
A cada miembro se le ha asignado un archivo CSV único e independiente. Los issues de cada persona **son únicos y no se solapan con los de los demás**.

1. **Alejandra** -> `issues_sample_Alejandra.csv` (127 revisiones)
2. **Carlos** -> `issues_sample_Carlos.csv` (127 revisiones)
3. **Juan** -> `issues_sample_Juan.csv` (127 revisiones)

---

## ⚙️ Metodología Aplicada
1. Se dividieron los datos en los dos conjuntos base (`smells` y `no-smells`).
2. Se **mezcló aleatoriamente** todo el dataset usando una semilla fija (seed: 42) para asegurar total imparcialidad y mantener la transparencia (se puede regenerar produciendo exactamente las mismas muestras).
3. Se seleccionaron las cuotas descritas sin reemplazo (es decir, cada issue pertenece solo a un usuario).
4. Dentro del archivo de cada usuario, **los registros se barajaron de nuevo aleatoriamente**. Esto evita que el usuario sepa de antemano si el registro que evalúa fue clasificado como "smell" o "no-smell", reduciendo cualquier posible sesgo por orden en la revisión manual.
