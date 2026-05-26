---
name: exercise-solver
description: Orchestrator skill that reads exercise images, solves them, and generates a LaTeX document. Use when user asks to "resuelve los ejercicios en", "desarrolla las soluciones de las imágenes", "escribe la solución en LaTeX para los ejercicios de", or "procesar imágenes de certámenes".
---

# Exercise Solver

## When to use this skill
**ALWAYS** use this skill when the user says things like:
- "resuelve los ejercicios en `{directorio}/`"
- "desarrolla las soluciones de las imágenes"
- "escribe la solución en LaTeX para los ejercicios de `{dir}/imagenes/`"
- Any request that combines: reading exercise images + producing a LaTeX solution document.

---

## Directory Convention

```
{root}/
├── imagenes/        ← exercise images (input)
│   ├── 01.png
│   ├── 02.png
│   └── ...
└── output/          ← LaTeX solution document (output)
    └── solution.tex
```

**Inferring the root directory:**
- If the user specifies a path explicitly, use it.
- Otherwise look for an `imagenes/` folder relative to the current working directory or the most recently mentioned directory.
- If ambiguous, ask: "¿En qué directorio están las imágenes?"

Create `output/` if missing: `mkdir -p {root}/output`.

---

## Tutor Skills — Canonical Paths

| Subject detected | File to read |
|---|---|
| Cálculo I / límites / derivadas | [[tutor-calculus-1]](../tutor-calculus-1/SKILL.md) |
| Cálculo II / integración / series | [[tutor-calculus-2]](../tutor-calculus-2/SKILL.md) |
| Cálculo III / multivariable | [[tutor-calculus-3]](../tutor-calculus-3/SKILL.md) |
| EDO / ecuaciones diferenciales | [[tutor-ode]](../tutor-ode/SKILL.md) |
| Probabilidad / Estadística | [[tutor-prob-stats]](../tutor-prob-stats/SKILL.md) |

If exercises span multiple subjects, read all relevant skill files.

---

## Execution Protocol

### Step 1 — Discover Images

```bash
ls -1 {root}/imagenes/ | sort
```

Supported formats: `.png`, `.jpg`, `.jpeg`, `.pdf`, `.webp`.
If the folder is empty or missing, stop and tell the user.

### Step 2 — Read and Understand Each Exercise

For each image, in sorted order:
1. Read the image with the vision tool.
2. Transcribe the exercise statement as written.
3. Identify:
   - **Subject area** (see tutor table above).
   - **Exercise type**: cálculo, estadística descriptiva, probabilidad, etc.
   - **Label**: filename stem as exercise number (`01.png` → Ejercicio 1).

### Step 3 — Load Relevant Tutor Skill

Read the corresponding SKILL.md (and relevant `syllabus/` topic files) for the detected subject.

### Step 4 — Solve Each Exercise

Apply the **Voz del Estudiante** rules below at every step of the solution. Solve step by step, state the final answer clearly, and flag exercises that need the source image embedded.

Collect results:
```
Exercise N:
  statement:      "..."
  solution_steps: ["...", "...", ...]
  final_answer:   "..."
  needs_image:    true | false
  image_path:     "imagenes/0N.png"
```

### Step 5 — Delegate to `latex-writer`

Call **`latex-writer`** with:
- Ordered list of solved exercises.
- Subject/course name if known.
- Output path: `{root}/output/solution.tex`.
- `needs_image` flag per exercise.

`latex-writer` owns all LaTeX formatting decisions. Do not write raw LaTeX here.

### Step 6 — Self-Review del .tex generado (OBLIGATORIO)

Después de que `latex-writer` escriba el archivo, **leerlo completo** y verificar cada ítem de esta lista antes de llamar a `latex-render`:

**Blacklist — buscar y corregir si aparece:**
- [ ] `tcolorbox`, `solbox`, `mdframed` → eliminar, la solución va en texto plano
- [ ] `\toprule`, `\midrule`, `\bottomrule` → reemplazar con `\hline`
- [ ] `\checkmark` en verificaciones → eliminar la verificación
- [ ] "Cercas de Tukey" → reemplazar por "límites del bigote"
- [ ] "mutuamente excluyentes y exhaustivas" en sección de verificación → eliminar
- [ ] `|A \cap B|`, `|A \cup B|` en el desarrollo de Venn → reemplazar por las letras de región
- [ ] "vale destacar", "cabe mencionar", "es importante señalar" → eliminar
- [ ] "asimetría positiva/negativa" como término técnico aislado → reemplazar por descripción directa
- [ ] `\newtheorem`, `\begin{theorem}`, `\begin{lemma}` → eliminar
- [ ] Nombres de teoremas como `\textbf{Método: Teorema de ...}` → reescribir en lenguaje directo

**Diagramas — verificar que estén presentes:**
- [ ] Si el ejercicio involucra conjuntos/probabilidades con Venn: ¿hay un bloque TikZ con círculos y letras de región? Si no, agregarlo.
- [ ] Si el ejercicio pide **boxplot**: llamar a `r-plotter` para generarlo en R como PDF. No usar TikZ para boxplots.
- [ ] Si el ejercicio pide **árbol de probabilidad**: llamar a `mermaid-diagram` para generarlo como PNG. No usar TikZ para árboles.
- [ ] Si el ejercicio pide histograma: puede hacerse en TikZ (simple) o en R si necesita verse prolijo.

Si se encuentran violaciones, **corregir el archivo directamente** con Edit antes de continuar. No es necesario avisar al usuario de cada corrección menor — simplemente hacerla.

### Step 7 — Renderizar

Llamar a **`latex-render`** pasando la ruta del `.tex` corregido.
Si `latex-render` reporta errores de compilación, leer el log, corregir el `.tex`, y volver a llamar a `latex-render`. Iterar hasta que compile limpio.

### Step 8 — Confirm Output

Reportar al usuario:
- Cuántos ejercicios se resolvieron.
- Ruta del PDF generado.
- Cualquier ejercicio omitido y por qué.

---

## Voz del Estudiante — Reglas de Estilo

Este es el núcleo de la skill. Cada solución debe sonar como la escribió un estudiante capaz, no un asistente de IA ni un libro de texto.

### Lenguaje natural

- Escribir en español directo. "entonces", "por lo tanto", "como X tenemos que Y", "despejando", "reemplazando".
- No citar teoremas por su nombre formal salvo que el enunciado lo exija explícitamente.
  - MAL: "Por el Teorema de Probabilidad Total, podemos escribir que..."
  - BIEN: "Como A y B son los únicos casos posibles:"
  - MAL: "Aplicando el Criterio de la Razón de D'Alembert..."
  - BIEN: "Aplicamos el criterio de la razón:"
- No agregar secciones de "Verificación" o "Comprobación" salvo que el enunciado lo pida.
- No usar expresiones de relleno: "vale destacar que", "cabe mencionar", "es importante señalar", "en este contexto", "cabe notar".
- El nivel de detalle en los pasos debe ser el que pide el enunciado, ni más ni menos.

### Adaptación al historial del usuario

Antes de resolver, **escanear los mensajes del usuario en la conversación actual** para capturar:

| Señal | Qué capturar |
|---|---|
| Notación | ¿Escribe $P(\bar{A})$ o $P(A^c)$? ¿$\sigma$ o $S$? ¿$\bar{x}$ o $\mu$? |
| Granularidad | ¿Muestra pasos intermedios o va directo al resultado? |
| Idioma técnico | ¿Usa términos en inglés o siempre en español? |
| Estilo de enunciado | ¿Cómo están redactados los ejercicios — formal, informal? |

Aplicar esas preferencias al contenido que se pasa a `latex-writer`. Si no hay historial suficiente, usar español académico simple sin excesos.

---

## Protocolos por Tipo de Ejercicio

### Diagrama de Venn con datos numéricos

**Nunca** usar la fórmula de inclusión-exclusión como punto de partida. Siempre:

1. Dibujar el diagrama mentalmente y asignar **una letra a cada región separada** del diagrama.
   - Para dos conjuntos A y B: región solo-A = $a$, intersección A∩B = $b$, solo-B = $c$.
   - Para tres conjuntos A, B, C sin triple intersección: asignar $a, b, c, d, e, f, g$ a cada zona.
2. Escribir las ecuaciones que salen directamente de los datos del enunciado en función de esas letras.
3. Resolver el sistema algebraicamente para encontrar cada región.
4. Calcular las probabilidades pedidas dividiendo por el total.

Ejemplo con dos conjuntos, total = 100, $|A| = 40$, $|B| = 30$, $|A \cap B| = 10$:
```
Sea: a = solo A,  b = A ∩ B,  c = solo B

b = 10
a + b = 40  →  a = 30
b + c = 30  →  c = 20
Total en A∪B = a + b + c = 60
Ninguno = 100 - 60 = 40
```

### Diagrama de Caja y Bigote (Boxplot)

1. Ordenar los datos y calcular $Q_1$, $Q_2$, $Q_3$, RIC.
2. Calcular los límites del bigote:
   - Límite inferior = $Q_1 - 1.5 \times \text{RIC}$
   - Límite superior = $Q_3 + 1.5 \times \text{RIC}$
3. Identificar los datos atípicos (los que quedan fuera de esos límites).
4. **NUNCA** llamar a los límites "cercas de Tukey". Decir "límites del bigote" o simplemente calcularlos sin nombrarlos.

### Probabilidad Condicional / Probabilidad Total

No anunciar el teorema. Directamente:
```
MAL:  "Usando el Teorema de Bayes, la probabilidad es..."
BIEN: "Si queremos P(A|B), necesitamos P(B|A)·P(A) / P(B):"
```

### Tablas de Frecuencia

Construir la tabla directamente. No definir notación antes de la tabla — las columnas se explican solas o con una línea breve después.

---

## Blacklist — Prohibido en las Soluciones

Estas frases o patrones **nunca** deben aparecer en el contenido que se pasa a `latex-writer`:

| Prohibido | Alternativa |
|---|---|
| "Cercas de Tukey" | "límites del bigote" o simplemente calcularlos |
| "Sea $X$ una variable aleatoria tal que..." | directo al grano con los datos |
| "Demostración:" como encabezado formal | solo si el enunciado pide probar algo |
| "vale destacar que" / "cabe mencionar" | eliminar esa frase |
| "mutuamente excluyentes y exhaustivos" en la verificación | no hacer la verificación |
| `\checkmark` al final de una comprobación | eliminar la comprobación salvo que la pidan |
| "Se puede observar que..." | decirlo directamente |
| "La distribución presenta asimetría positiva" | "la distribución está sesgada a la derecha" o "hay más datos concentrados a la izquierda" |

---

## Error Handling

| Situación | Acción |
|---|---|
| Imagen ilegible / muy borrosa | Omitir; notar en el output "Ejercicio N: imagen ilegible." |
| Enunciado ambiguo | Indicar la interpretación tomada, resolverla. |
| Materia no identificada | Resolver con rigor general sin cargar skill de tutor. |
| Carpeta `output/` no existe | Crear con `mkdir -p`. |

---

## Constraints

- **Orden preservado**: los ejercicios aparecen en el output en el mismo orden que los archivos ordenados.
- **No inventar datos**: transcribir solo lo visible en la imagen. Si no se lee, decirlo.
- **No escribir LaTeX directamente**: delegar siempre a `latex-writer`.
- **No compilar a PDF**: solo generar `solution.tex`.

---

## Exam Resolution Style & Semantic Flow
- **Estilo de Resolución:** Toda solución debe cumplir rigurosamente con las directrices de flujo semántico del lenguaje definidas en la skill rectora [[math-solver-style]](../math-solver-style/SKILL.md).
- **Conectores obligatorios:** Es imperativo usar exclusivamente conectores algebraicos breves en español (e.g., *"reemplazando en"*, *"integrando"*, *"volviendo a la variable original"*) para conectar los pasos del desarrollo.
- **Sin subtítulos:** Presentar el desarrollo en formato continuo, libre de títulos artificiales o explicaciones pedagógicas ajenas al certamen.
