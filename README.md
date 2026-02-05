# Fundamentals Repository

Este repositorio contiene los resúmenes y apuntes fundamentales de ingeniería, organizados por módulos.

## 📂 Estructura del Proyecto

Aquí encontrarás los documentos principales compilados (PDF) y su código fuente en LaTeX:

- **Módulo 1:** [Matemáticas y Probabilidades](modulo%201/modulo_1.pdf)
- **Módulo 2:** [Ciencias Naturales (Física y Química)](modulo%202/modulo_2.pdf)
- **Módulo 3:** [Ingeniería (Economía, Programación, Ética)](modulo%203/modulo_3.pdf)

> **Nota:** Si los PDFs no se visualizan directamente, asegúrate de estar en la rama correcta o de haber compilado el proyecto localmente.

---

## 🚀 Guía de Instalación y Uso

### Prerrequisitos
Se recomienda encarecidamente trabajar en un entorno **Linux** o usar **WSL (Windows Subsystem for Linux)** si estás en Windows. Esto facilita la gestión de paquetes de LaTeX y herramientas de compilación.

### 1. Clonar el Repositorio

Abre tu terminal (o terminal de WSL) y ejecuta:

```bash
git clone git@github.com:anomvlito/respositorio-fundamentals.git
cd respositorio-fundamentals
```

### 2. Compilar los Documentos

Tienes dos opciones principales para compilar los archivos `.tex` a PDF:

#### Opción A: Usando VS Code (Recomendado)
1. Instala la extensión **LaTeX Workshop** en VS Code.
2. Abre cualquiera de los archivos principales (ej: `modulo 3/modulo_3.tex`).
3. La extensión detectará el archivo y podrás compilar guardar (`Ctrl+S`) o usando el panel de comandos de LaTeX.

#### Opción B: Usando la Terminal
Si prefieres la línea de comandos, asegúrate de tener instalado `texlive-full` o una distribución similar.

Navega a la carpeta del módulo y usa `pdflatex` (o `latexmk` para automagicalidad):

```bash
cd "modulo 3"
pdflatex modulo_3.tex
# o si usas bibtex/referencias cruzadas, ejecuta pdflatex dos veces
```

## 🛠 Estado del Proyecto
Actualmente se están realizando ajustes en la compilación de los módulos. Si encuentras errores al compilar, revisa Issues o contacta al mantenedor.
