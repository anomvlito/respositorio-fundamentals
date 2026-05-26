---
name: latex-render
description: Compiles a .tex file to PDF using latexmk, then deletes all auxiliary files (log, aux, out, fls, fdb_latexmk, synctex.gz). Called automatically after latex-writer finishes, or manually when the user asks to compile/render a LaTeX file.
---

# LaTeX Render

## When to use this skill
- **Automáticamente**: llamada por `latex-writer` o `exercise-solver` después de escribir un `.tex`.
- **Manualmente**: cuando el usuario dice "compila", "renderiza", "genera el PDF", "limpia los auxiliares".

---

## Input

| Campo | Descripción |
|---|---|
| `tex_path` | Ruta absoluta al archivo `.tex` a compilar |

Si no se entrega `tex_path`, buscar el `.tex` más reciente en el directorio de trabajo o en `output/` del directorio mencionado en la conversación.

---

## Execution Protocol

### Paso 1 — Verificar que el archivo existe

```bash
ls -lh {tex_path}
```

Si no existe, detener y avisar.

### Paso 2 — Compilar con latexmk

Usar `latexmk` con `-pdf` y `-interaction=nonstopmode` para no quedarse colgado ante warnings. Compilar **dos veces** implícitamente (latexmk lo maneja solo para referencias cruzadas).

```bash
latexmk -f -pdf -interaction=nonstopmode -output-directory={output_dir} {tex_path}
```

> `-f` fuerza la recompilación aunque latexmk crea que el output está actualizado. Sin este flag, cambios recientes en el `.tex` pueden no reflejarse en el PDF.

donde `{output_dir}` es el directorio que contiene el `.tex`.

Si `latexmk` no está disponible (verificar con `which latexmk`), usar `pdflatex` dos veces:

```bash
pdflatex -interaction=nonstopmode -output-directory={output_dir} {tex_path}
pdflatex -interaction=nonstopmode -output-directory={output_dir} {tex_path}
```

### Paso 3 — Verificar el PDF

```bash
ls -lh {output_dir}/{basename}.pdf
```

Si el PDF no fue generado, el archivo `.log` contiene el error. Leerlo y reportar las líneas relevantes al usuario (buscar líneas que empiecen con `!`):

```bash
grep "^!" {output_dir}/{basename}.log | head -20
```

### Paso 4 — Limpiar auxiliares

Solo si el PDF fue generado correctamente. Eliminar todos los archivos auxiliares dejando únicamente el `.tex` y el `.pdf`:

```bash
rm -f {output_dir}/{basename}.aux
rm -f {output_dir}/{basename}.log
rm -f {output_dir}/{basename}.out
rm -f {output_dir}/{basename}.fls
rm -f {output_dir}/{basename}.fdb_latexmk
rm -f {output_dir}/{basename}.synctex.gz
rm -f {output_dir}/{basename}.toc
rm -f {output_dir}/{basename}.lof
rm -f {output_dir}/{basename}.lot
rm -f {output_dir}/{basename}.bbl
rm -f {output_dir}/{basename}.blg
```

O en una sola línea usando la extensión glob:

```bash
latexmk -c -output-directory={output_dir} {tex_path}
```

> `latexmk -c` limpia todos los auxiliares generados en la última compilación sin tocar el `.pdf` ni el `.tex`.

### Paso 4.5 — Aplicar efecto de escaneo analógico (Por Defecto)

Para generar una versión realista que parezca un papel físico escaneado con imperfecciones de digitalización, ejecutar el script de escaneo:

```bash
/home/fabian/.gemini/antigravity/brain/64388d7a-2956-45a5-ad09-098974b25c84/scratch/scan_effect.py {output_dir}/{basename}.pdf {output_dir}/{basename}_scanned.pdf
```

Este script aplica:
- **Geometría asimétrica**: Rotación aleatoria a $\pm 1.0^\circ$, traslación y cizalladura (shear) aleatoria para simular el deslizamiento del rodillo sobre el papel.
- **Suciedad de cristal/sensor**: Probabilidad del 40% de dibujar una línea difusa vertical muy fina (típica línea de polvo en escáneres).
- **Iluminación desigual**: Un gradiente sutil de iluminación en los bordes simulando sombra de curvatura de papel.
- **Respuesta del sensor**: Curva de contraste más agresiva ($1.25$) y grano analógico más marcado (ruido monocromático más alto).

### Paso 5 — Confirmar

```bash
ls {output_dir}/
```

Reportar al usuario:
- Ruta del PDF generado.
- Tamaño del PDF.
- Lista de lo que quedó en el directorio (solo `.tex`, `.pdf` y opcionalmente los archivos escaneados deberían quedar).

---

## Integración con otras skills

`latex-writer` debe llamar esta skill **al final de su protocolo de escritura**, pasando la ruta del `.tex` recién creado. El flujo completo queda:

```
exercise-solver
  └─▶ latex-writer  (escribe solution.tex)
        └─▶ latex-render  (compila → PDF, limpia auxiliares, aplica scan_effect.py → solution_scanned.pdf)
```

---

## Error Handling

| Situación | Acción |
|---|---|
| Error de compilación (`!` en el log) | Mostrar el error, **no** borrar auxiliares (el log ayuda a depurar) |
| `pdflatex` y `latexmk` ausentes | Avisar al usuario que instale `texlive` |
| El `.tex` tiene `\input{}` o `\include{}` | Compilar desde el directorio del `.tex` para que las rutas relativas funcionen |
| PDF ya existe y la compilación falla | Conservar el PDF anterior, no sobreescribirlo con un archivo corrupto |

---

## Constraints

- **Solo limpiar si el PDF fue generado** con éxito. Nunca borrar auxiliares si la compilación falló.
- **Nunca borrar el `.tex`** ni el `.pdf`.
- **No modificar el `.tex`** antes de compilar — solo compilar lo que `latex-writer` entregó.
