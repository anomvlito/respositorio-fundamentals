---
name: latex-writer
description: LaTeX document generator called by exercise-solver and other skills. Receives structured content and writes a clean, simple .tex file that looks like a student solution, not a typeset textbook. Delegates image embedding to latex-illustrator.
---

# LaTeX Writer

## When to use this skill
Called **by other skills**, not directly by the user. Activates when:
- `exercise-solver` has finished solving exercises and needs a `.tex` document.
- Any other skill needs to produce a formatted LaTeX output file.

---

## Inputs Expected

- `exercises[]`: Ordered list of solved exercises (see structure below)
- `output_path`: Absolute path for the `.tex` file

Each exercise in `exercises[]`:
```
{
  number:       "1",
  statement:    "Texto del enunciado...",
  steps:        ["...", "...", ...],
  final_answer: "...",
  needs_image:  true | false,
  image_path:   "imagenes/01.png"
}
```

---

## Filosofía del Documento

El documento debe verse como una solución escrita por un estudiante competente, no como un paper o un libro de texto. Esto significa:

- **Sin cajas decorativas** alrededor de las soluciones. Sin `tcolorbox`, sin `solbox`, sin `mdframed`.
- **Sin reglas de tabla fancy** (`\toprule`, `\midrule`, `\bottomrule`). Usar `\hline` simple.
- **Sin encabezados de paso formales** (`\textbf{Paso 1.}` en negrita separado). Los pasos fluyen como texto o directamente como matemática.
- **Sin secciones de verificación** a menos que el contenido las incluya explícitamente.
- **Sin `\newtheorem`** — no se citan teoremas formalmente.
- **Sin códigos de ramo** en el encabezado del documento. Nunca imprimir identificadores del tipo `MAT1640`, `MAT1610`, `MAT1620`, etc. en el PDF generado — ni en el título, ni en el encabezado, ni en ningún otro lugar visible. Esa información es solo interna del sistema de skills.
- **Preamble mínimo**: solo los paquetes que realmente se usan.

---

## Document Structure

```latex
\documentclass[12pt,letterpaper]{article}

\usepackage{mathpazo}
\usepackage{fontspec}
\setmainfont{PatrickHand-Regular.ttf}[Path=./]
\usepackage[spanish,es-noshorthands]{babel}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{eso-pic}

% Color de fondo estilo GoodNotes
\definecolor{gnbg}{HTML}{FDFDFD}
\pagecolor{gnbg}

% Color de "tinta"
\definecolor{ink}{HTML}{2C3E50}
\color{ink}

% Cuadrícula estilo GoodNotes
\AddToShipoutPictureBG{%
  \begin{tikzpicture}[remember picture, overlay]
    \draw[step=6mm, color=gray!20, thin] (current page.south west) grid (current page.north east);
  \end{tikzpicture}
}

\geometry{margin=2.5cm}

\begin{document}

% exercises go here

\end{document}
```

**Nota:** Es necesario copiar el archivo `PatrickHand-Regular.ttf` al directorio donde se generará el archivo para que compile correctamente. El documento debe ser compilado con `lualatex` o `xelatex`. Agregar `\usepackage{booktabs}` **nunca** — usar `\hline` simple.

---

## Exercise Block Template

```latex
\textbf{Ejercicio {N}.}

{statement — plain text, one or two lines}

% If needs_image == true: call latex-illustrator here, insert figure
% before the solution.

\medskip
{solution — flowing text + math, no box around it}

\[
  {final answer}
\]

\bigskip
```

Notar:
- El enunciado va en texto plano o en una línea de `\textit{}` si tiene énfasis.
- La solución es texto corrido con `align*` para las cadenas de igualdades. **Sin caja**.
- La respuesta final va en `\[ \]` display math o inline si es breve.
- Entre ejercicios va `\bigskip`, no `\hrule` ni `\newpage`.

---

## LaTeX Writing Rules

### Matemática
- Inline math: `$...$`
- Display math standalone: `\[ ... \]`
- Cadena de igualdades (desarrollo): `\begin{align*} ... \end{align*}`
- Fracciones: `\frac{num}{den}`
- Integrales: `\int_a^b f(x)\,dx` (con `\,` antes de `dx`)
- Multiplicación explícita: `\cdot`
- Probabilidad condicional: `P(A \mid B)` — usar `\mid`, no `|`
- Media: `\bar{x}`, mediana: `\tilde{x}`, desviación: `S` o `\sigma` según lo que use el contenido

### Tablas
Usar siempre `tabular` simple con `\hline`. Ejemplo:

```latex
\begin{center}
\begin{tabular}{lccc}
\hline
Categoría & $f_i$ & $f_{r,i}$ (\%) & $F_i$ \\
\hline
Muy Baja  & 18 & 36 & 18 \\
Baja      &  9 & 18 & 27 \\
\hline
Total     & 50 & 100 & \\
\hline
\end{tabular}
\end{center}
```

### Enumeraciones en el enunciado

```latex
\begin{enumerate}[label=\alph*)]
  \item ...
\end{enumerate}
```

### Soluciones con sub-items (a, b, c...)

Fluir dentro del mismo bloque de solución:

```latex
\textbf{a)} Calculamos $Q_1$, $Q_2$, $Q_3$:
\begin{align*}
Q_1 &= \ldots \\
Q_2 &= \ldots
\end{align*}

\textbf{b)} La media aritmética es $\bar{x} = \ldots$
```

No crear `\section*{}` por cada sub-item.

### Diagramas de Venn — Regiones con letras

Cuando el contenido de la solución usa el método de regiones con letras, representarlo así:

```latex
Sea $a$ = solo $A$, $b$ = $A \cap B$, $c$ = solo $B$.

De los datos:
\begin{align*}
b &= 10 \\
a + b &= 40 \implies a = 30 \\
b + c &= 30 \implies c = 20
\end{align*}

Total en $A \cup B = a + b + c = 60$, ninguno $= 100 - 60 = 40$.
```

No usar `|A \cap B|` ni notación de cardinalidad de conjuntos en el desarrollo. Solo las letras de las regiones.

### Boxplot con TikZ

Si el contenido requiere un boxplot, generarlo en TikZ de manera **simple**: caja, bigotes, puntos para outliers. Sin anotaciones de texto flotando encima de la caja. Sin colores de relleno intensos — usar `fill=gray!15` o sin relleno. Los valores clave ($Q_1$, $Q_2$, $Q_3$) van debajo del eje, no encima de la caja.

---

## Image Embedding Protocol

When `needs_image == true`:
1. Call `latex-illustrator` with the image path (relative to the `.tex` file), caption `"Enunciado — Ejercicio N"`, placement `[H]`, width `0.7\textwidth`.
2. Insert the returned `figure` environment right before the solution block.

---

## Writing Protocol

1. Build the full document string in memory.
2. Write atomically with the Write tool to `output_path`.
3. Verify the file exists and is non-empty:
   ```bash
   wc -l {output_path}
   ```
4. Call **`latex-render`** passing `tex_path = output_path`. This compiles the PDF and cleans all auxiliary files.
5. Report to the calling skill: output path, PDF path, and result of the render step.

---

## Constraints

- **No compilar con `pdflatex`**. Debido al uso de `fontspec` y la tipografía manuscrita, es obligatorio compilar con **`lualatex`** o **`xelatex`**.
- **No sobreescribir** un `solution.tex` existente sin avisar. Si ya existe, usar sufijo timestamp: `solution_YYYYMMDD_HHMM.tex`.
- **Encoding UTF-8** siempre.
- **Sin placeholders** (`% TODO`, `% completar aquí`) en el output final.
- **Sin `tcolorbox`**, sin `booktabs`, sin `\newtheorem`, sin `\checkmark` de verificación.
