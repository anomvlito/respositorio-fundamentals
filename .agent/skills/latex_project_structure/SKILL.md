---
name: latex_project_structure
description: Scaffold a robust, modular LaTeX project structure for study guides or textbooks, separated from visual styling.
---

# LaTeX Project Scaffolding

## When to use this skill
**ALWAYS** utilize this skill when:
- Starting **ANY** new LaTeX project from scratch.
- The user asks for a "template", "skeleton", "base", or "setup".
- Refactoring a large, monolithic `.tex` file into a maintainable structure.
- The user complains about a "messy" project or compilation errors due to file organization.

This skill provides the blueprint for creating a maintainable...

## 1. Directory Hierarchy

Create a root directory and the following structure to ensure scalability:

```text
project_root/
├── main.tex                 # The orchestrator file (skeleton)
├── intro.tex                # Syllabus, intro, or course program
├── estilos.tex              # Style definitions (separated from logic)
├── Makefile                 # Automation for build process
└── unidades/                # Content directory
    ├── 01_topic_name.tex    # Wrapper for Unit 1
    ├── 02_topic_name.tex    # Wrapper for Unit 2
    ├── ...
    ├── practica.tex         # Practice questions wrapper
    ├── solucionario.tex     # Solutions wrapper
    ├── Unidad1/             # Source content for Unit 1
    │   └── content_topic.tex
    ├── Unidad2/
    │   └── content_topic.tex
    ├── Practica/            # Source content for practice
    │   └── preguntas.tex
    └── Solucionario/        # Source content for solutions
        └── respuestas.tex
```

## 2. File Roles & Best Practices

### The Orchestrator (`main.tex`)
Keep this file minimal. It should only load the class, import styles, title data, and include the unit wrappers.
**Avoid writing content here.**

```latex
\documentclass[12pt]{article}
\input{estilos.tex} % Link to the style skill

\title{\textbf{Project Title}}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

\input{intro.tex}
\newpage

% Include Units sequentially
\input{unidades/01_topic_name.tex}
\input{unidades/02_topic_name.tex}
% ...
\input{unidades/practica.tex}
\input{unidades/solucionario.tex}

\end{document}
```

### Modular Units (`unidades/XX_topic.tex`)
Use numbered wrappers to control the order and ease of compilation debugging.
```latex
% unidades/01_calculo.tex
\section{Unidad 1: Cálculo}
\input{unidades/Unidad1/calculo_content.tex}
\newpage
```

### Automation (`Makefile`)
Always include a Makefile to simplify the build process (PDF generation and cleanup).

```makefile
all:
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
```

## 3. Usage Strategy
1.  **Initialize**: Run `mkdir -p unidades/Unidad1` etc.
2.  **Scaffold**: Create the `main.tex` and `Makefile` first.
3.  **Content**: Create empty content files in specific folders (`unidades/Unidad1/`).
4.  **Style**: Apply the separate `latex_premium_style` skill to `estilos.tex`.

This structure ensures that as the project grows (to hundreds of pages), it remains navigable and compiles cleanly without one massive file.
