# Fundamentals Repository

Este repositorio contiene los resúmenes y apuntes fundamentales de ingeniería, organizados por módulos.

## 📂 Estructura del Proyecto

Aquí encontrarás los documentos principales compilados (PDF) y su código fuente en LaTeX:

- **Módulo 1:** [Matemáticas y Probabilidades](modulo%201/modulo_1.pdf)
- **Módulo 2:** [Ciencias Naturales (Física y Química)](modulo%202/modulo_2.pdf)
- **Módulo 3:** [Ingeniería (Economía, Programación, Ética)](modulo%203/modulo_3.pdf)


---

## 📚 Material Recopilado

Este repositorio incluye una extensa colección de recursos adicionales en la carpeta `material-recopilado`. Aquí encontrarás guías, ejercicios resueltos y material de apoyo.

### 🌟 Recurso Destacado
Recomendamos especialmente estudiar la siguiente guía completa:
- 📖 **[Tom Trivino Fundamentals v2.3](material-recopilado/tom%20trivino%20Fundamentals%20v2.3.pdf)**: Guía esencial para el estudio de los fundamentos. ¡Altamente recomendada!

### Directorios Principales
Accede rápidamente a los recursos organizados:

- 📂 **[Guías de Ejercicios](material-recopilado/Guías%20de%20Ejercicios)**
- 📂 **[Prototipos de Exámenes](material-recopilado/prototipo%20Examen%20pasado%20(SIN%20SOLUCIÓN))**
- 📂 **[Red de Apoyo Solidaria](material-recopilado/🚩Red%20de%20Apoyo%20Fundamentals%20Solidaria%20🚩)**
- 📂 **[Material Separado](material-recopilado/SEPARADO)**

### 🧠 Skills de Antigravity (Agentes Inteligentes)
Este repositorio incluye una carpeta oculta `.agent/skills` con capacidades avanzadas para asistentes de IA. Para usarlos, asegúrate de que tu agente tenga acceso a esta carpeta.

Skills destacadas:
- 🧮 **[Cálculo I](.agent/skills/tutor-calculus-1)**
- 📈 **[Cálculo II](.agent/skills/tutor-calculus-2)**
- 📉 **[Cálculo III](.agent/skills/tutor-calculus-3)**
- 📝 **[Gestión de Word](.agent/skills/gestionar-word)**
- 🔬 **[Investigación Cualitativa](.agent/skills/recoleccion_cualitativa)**

_Consulta la carpeta `.agent` para ver la lista completa._

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

---

## 🤝 Cómo Contribuir

¡Toda ayuda es bienvenida! Si tienes apuntes, correcciones o ejercicios nuevos, sigue estos pasos sencillos para colaborar:

1.  **Haz un Fork** del repositorio (usa el botón "Fork" arriba a la derecha en GitHub).
2.  **Clona tu repositorio** a tu computador:
    ```bash
    git clone https://github.com/TU_USUARIO/respositorio-fundamentals.git
    ```
3.  **Crea una nueva rama** para tus cambios:
    ```bash
    git checkout -b mi-aporte
    ```
4.  **Agrega tu material** o realiza las correcciones necesarias.
5.  **Sube tus cambios** (Commit & Push):
    ```bash
    git add .
    git commit -m "Agregando nuevos apuntes de X materia"
    git push origin mi-aporte
    ```
6.  **Abre un Pull Request** en GitHub:
    - Ve a la pestaña "Pull Requests" y haz clic en "New Pull Request".
    - Explica brevemente qué agregaste y envíalo.

¡Revisaremos tu aporte para integrarlo lo antes posible! 🚀
