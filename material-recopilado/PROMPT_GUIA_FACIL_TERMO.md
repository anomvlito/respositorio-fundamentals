# PROMPT REUTILIZABLE: Crear Guía de Victorias Rápidas Termodinámica

## Cómo usar este prompt

Este prompt ha sido adaptado específicamente para generar la tanda de "victorias rápidas" de Termodinámica.

---

## PROMPT BASE

```
Necesito que crees una "Guía de Victorias Rápidas" (preguntas fáciles) para Termodinámica.

## Paso 1: Lee el solucionario fuente
Lee el archivo:
/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/guia_termodinamica_soluciones.tex

Selecciona las 10-15 preguntas MÁS FÁCILES según estos criterios:
- Conceptuales (verdadero/falso entre alternativas, sin cálculo)
- Cálculo en 1-2 pasos con UNA fórmula directa del Handbook (ej. conversiones)
- Conversión de unidades directa (Temp C a K o F)
- Preguntas que dependen de definiciones que están literalmente en el Handbook (Ley Cero, vapor sobrecalentado, etc.)

EXCLUYE:
- Cálculos muy enredados de entropía o ciclos con múltiples etapas
- Relaciones maxwell y ecuaciones pesadas.
- Rankine o Carnot de más de 3 pasos

## Paso 2: Busca las páginas del FE Handbook
Usa el skill fe-handbook-ref y las referencias para encontrar conceptos clave:
ideal gas, entropy, enthalpy, rankine, celsius, Carnot, heat transfer...
Las páginas esperadas en el Handbook de NCEES FE Reference Handbook 10.1 suelen estar en el rango [143-176] para Thermodynamics y en la 1 para Unit Conversions.

## Paso 3: Inspírate en este modelo
Lee el archivo de referencia (u observa su estilo):
/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda1.tex

El espíritu de la guía es:
- Cada ejercicio tiene: Fuente (examen-año), Enunciado, Solución PASO A PASO (no solo el resultado), y una caja \fbox{} con "¡Lo que dice el Handbook FE!" indicando la página exacta
- En los pasos de la solución: explica el PORQUÉ de cada paso, no solo el cálculo
- La caja del Handbook debe ser honesta: si algo NO está en el Handbook, decirlo claramente y qué hay que memorizar en cambio

## Paso 4: Crea el archivo LaTeX
Guarda el archivo en:
/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles/guia_termodinamica_facil_tanda1.tex

Estructura del documento:
1. Preamble idéntico al de referencia (usar también \usepackage{tcolorbox})
2. Título: "Guía de Victorias Rápidas -- Termodinámica\\[0.3cm]\large Tanda 1: Fundamentos y Conceptos Básicos"
3. tcolorbox azul al inicio con: Objetivo, Nivel, Temas cubiertos (lista numerada)
4. Un \section*{} por ejercicio con el patrón: Enunciado → Solución paso a paso → \fbox{Handbook}
5. tcolorbox verde al final: "Resumen de Conceptos Clave" con (a) qué está en el Handbook y en qué página, (b) qué hay que memorizar

## Paso 5: Compila y verifica
```bash
mkdir -p "/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles"
cd "/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica/preguntas faciles"
pdflatex -interaction=nonstopmode guia_termodinamica_facil_tanda1.tex
```
Verifica que el PDF compile sin errores y repara cualquier issue sintáctico de LaTeX que resulte.
```
