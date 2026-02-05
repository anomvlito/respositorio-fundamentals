---
name: latex_premium_style
description: Generate premium-quality, visually appealing LaTeX documents using tcolorbox, custom color palettes, and semantic structure.
---

# Premium LaTeX Styling Guide

## When to use this skill
**ALWAYS** apply this skill when the user requests:
- A "premium", "modern", or "high-quality" LaTeX document.
- Study guides, summaries, cheat sheets, or textbooks.
- Visual enhancements like "boxes", "colors", or "better formatting".
- A "template" that looks professional (often paired with `latex_project_structure`).

This skill guides the creation of high-quality LaTeX documents...

## 1. Project Structure
Always organize the project to separate content from styling:
- **`main.tex`**: The orchestrator. Loads `estilos.tex` and includes content via `\input{}`.
- **`estilos.tex`**: Centralized configuration (packages, colors, box definitions).
- **`unidades/`**: Content files separated by topic (e.g., `01_calculo.tex`, `02_algebra.tex`).

## 2. Dependencies & Colors (`estilos.tex`)

Use `xcolor` with a curated palette and `tcolorbox` for visual elements.

```latex
\usepackage[table,xcdraw]{xcolor}
\usepackage[many]{tcolorbox}
\usepackage{geometry}
\geometry{a4paper, margin=2.5cm}

% Modern Palette
\definecolor{DeepBlue}{HTML}{003B5C}    % Azul corporativo
\definecolor{BrightBlue}{HTML}{007ACC}  % Azul brillante
\definecolor{Emerald}{HTML}{00A388}     % Verde para éxito/teoremas
\definecolor{WarningOrange}{HTML}{FF9F43} % Naranja para tips
\definecolor{LightGray}{HTML}{F8F9FA}   % Fondo suave
```

## 3. Custom Environments (The "Premium" Look)

Use `tcolorbox` to create semantic environments. Avoid plain text for important definitions or theorems.

### Definición (Blue)
Use for concepts, contents, or generic headers.
```latex
\newtcolorbox{definicion}[1][]{
    enhanced, breakable,
    colback=BrightBlue!5!white,
    colframe=DeepBlue,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title=Definición,
    borderline west={4pt}{0pt}{DeepBlue},
    sharp corners,
    boxrule=0.5pt,
    #1
}
```

### Teorema / Indicadores (Green)
Use for properties, theorems, answers, or evaluation criteria.
```latex
\newtcolorbox{teorema}[1][]{
    enhanced, breakable,
    colback=Emerald!5!white,
    colframe=Emerald,
    coltitle=white,
    fonttitle=\bfseries\sffamily,
    title=Teorema,
    borderline west={4pt}{0pt}{Emerald},
    sharp corners,
    boxrule=0.5pt,
    #1
}
```

### Ejercicio (Gray/Professional)
Use for problem statements or practice questions.
```latex
\newtcolorbox{ejercicio}[1][]{
    enhanced, breakable,
    colback=white,
    colframe=gray!50!black,
    coltitle=white,
    fonttitle=\bfseries,
    title=Ejercicio,
    boxrule=1pt,
    arc=4mm,
    shadow={2mm}{-2mm}{0mm}{black!20},
    #1
}
```

### Pasos / Algoritmos
Use a custom list environment for step-by-step solutions to ensure clarity.
```latex
\usepackage{enumitem}
\newenvironment{pasos}
    {\begin{enumerate}[label=\textbf{Paso \arabic*}:, leftmargin=*]}
    {\end{enumerate}}
```

## 4. Best Practices for Content

- **Separation of Concerns**: Never define colors or commands in `main.tex`. Keep `main.tex` clean.
- **Micro-Typography**: Use `\noindent`, `\centering`, and standard spacing (`\vspace`) sparingly; rely on the boxes for spacing.
- **Math Macros**: define shortcuts like `\newcommand{\R}{\mathbb{R}}` for cleaner code.
- **Figures**: Always use `\centering` and `[H]` (from `float` package) if exact placement is needed, though `tcolorbox` is preferred for wrapping text.

## 5. Usage Example

```latex
\begin{definicion}[title=Concepto Clave]
    Una función $f$ es continua si...
\end{definicion}

\begin{ejercicio}[title=Problema 1]
    Resuelva la ecuación...
\end{ejercicio}

\begin{pasos}
    \item \textbf{Derivar}: ...
    \item \textbf{Igualar a cero}: ...
\end{pasos}

\begin{teorema}[title=Respuesta]
    $x = 42$
\end{teorema}
```
