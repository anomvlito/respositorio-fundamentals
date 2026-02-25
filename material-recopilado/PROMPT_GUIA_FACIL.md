# PROMPT REUTILIZABLE: Crear Guía de Victorias Rápidas

## Cómo usar este prompt

Adapta los campos marcados con `[...]` según la materia que necesitas. Luego pásalo directamente al agente.

---

## PROMPT BASE

```
Necesito que crees una "Guía de Victorias Rápidas" (preguntas fáciles) para [NOMBRE MATERIA].

## Paso 1: Lee el solucionario fuente
Lee el archivo:
[RUTA DEL SOLUCIONARIO]

Selecciona las 10-15 preguntas MÁS FÁCILES según estos criterios:
- Conceptuales (verdadero/falso entre alternativas, sin cálculo)
- Cálculo en 1-2 pasos con UNA fórmula directa del Handbook
- Conversión de unidades directa
- Preguntas que dependen de definiciones que están literalmente en el Handbook

EXCLUYE:
- Balanceo de ecuaciones redox complejo (>3 pasos de semirreacciones)
- Cálculos con reactivo limitante en múltiples pasos
- Problemas de equilibrio que requieren tabla ICE compleja

## Paso 2: Busca las páginas del FE Handbook
Usa el skill fe-handbook-ref disponible en:
@[/wsl+ubuntu/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/SKILL.md]
@[/wsl+ubuntu/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/resources/handbook_map.json]

Para cada pregunta seleccionada, busca:
```bash
grep -i "[CONCEPTO CLAVE]" /ruta/handbook_map.json
```
Y anota la página real del Handbook donde aparece la fórmula o definición relevante.

## Paso 3: Inspírate en este modelo
Lee el archivo de referencia:
/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda1.tex

El espíritu de la guía es:
- Cada ejercicio tiene: Fuente (examen-año), Enunciado, Solución PASO A PASO (no solo el resultado), y una caja \fbox{} con "¡Lo que dice el Handbook FE!" indicando la página exacta
- En los pasos de la solución: explica el PORQUÉ de cada paso, no solo el cálculo
- La caja del Handbook debe ser honesta: si algo NO está en el Handbook, decirlo claramente y qué hay que memorizar en cambio

## Paso 4: Crea el archivo LaTeX
Guarda el archivo en:
[RUTA DESTINO]/preguntas faciles/guia_[SIGLA]_facil_tanda1.tex

Estructura del documento:
1. Preamble idéntico al de referencia (usar también \usepackage{tcolorbox})
2. Título: "Guía de Victorias Rápidas -- [Nombre Materia]\\[0.3cm]\large Tanda 1: [Subtítulo descriptivo]"
3. tcolorbox verde al inicio con: Objetivo, Nivel, Temas cubiertos (lista numerada)
4. Un \section*{} por ejercicio con el patrón: Enunciado → Solución paso a paso → \fbox{Handbook}
5. tcolorbox verde al final: "Resumen de Conceptos Clave" con (a) qué está en el Handbook y en qué página, (b) qué hay que memorizar

## Paso 5: Compila y verifica
```bash
cd "[RUTA DESTINO]/preguntas faciles"
pdflatex -interaction=nonstopmode guia_[SIGLA]_facil_tanda1.tex
```
Verifica que el PDF compile sin errores.
```

---

## Instancias por materia

### Guía Dinámica
```
Solucionario: /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia dinamica/guia_dinamica_soluciones.tex
Destino:      /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia dinamica/preguntas faciles/
Sigla:        dinamica
Conceptos clave para buscar en handbook: kinematics, newton, momentum, energy, work, projectile
Páginas handbook estimadas: 114-129 (Dynamics)
```

### Guía Matemáticas
```
Solucionario: /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/guia_matematicas_soluciones.tex
Destino:      /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/preguntas faciles/
Sigla:        matematicas
Conceptos clave para buscar en handbook: derivative, integral, matrix, probability, laplace, statistics
Páginas handbook estimadas: 34-84 (Mathematics, Probability & Statistics)
```

### Guía Termodinámica
```
Solucionario: /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/guia_termodinamica_soluciones.tex
Destino:      /home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles/
Sigla:        termodinamica
Conceptos clave para buscar en handbook: ideal gas, entropy, enthalpy, rankine, celsius, Carnot, heat transfer
Páginas handbook estimadas: 143-176 (Thermodynamics)
```

---

## Notas para el agente

1. **Criterio de "fácil"**: Una pregunta es fácil si un estudiante puede resolverla en menos de 3 minutos con el Handbook abierto en la página correcta. Si requiere >3 fórmulas o >4 pasos algebraicos, NO es fácil.

2. **El fbox del Handbook es lo más importante**: Cita la página EXACTA usando `handbook_page` del json (número impreso, no el índice PDF). Busca con grep en `content_raw` del `handbook_map.json`.

3. **Sé honesto sobre qué NO está en el Handbook**: Si un concepto requiere memorización, dilo explícitamente en la caja del Handbook. Es más valioso que fingir que todo está ahí.

4. **Mantén el estilo pedagógico**: Usa \textbf{Paso 1}, \textbf{Paso 2}, etc. Explica el razonamiento, no solo el cálculo.

5. **El archivo de referencia para el estilo**: guia_electro_facil_tanda1.tex (ver arriba).
