---
name: coherencia_investigacion_cualitativa
description: Skill for ensuring structural coherence, logical flow, and academic precision in qualitative research reports, bridging raw findings with substantive theory.
---

# Coherencia y Escritura en Investigación Cualitativa

Esta habilidad se enfoca en elevar la calidad narrativa de los informes de investigación, asegurando que la transición entre la "data cruda" (citas) y la "teoría sustantiva" sea fluida, lógica y consistente.

## Cuándo usar esta habilidad
- Al redactar informes finales basados en análisis de Grounded Theory o Etnografía.
- Cuando el texto se siente fragmentado o como una simple lista de hallazgos.
- Para verificar que cada afirmación interpretativa esté respaldada por evidencia.
- Al transformar borradores informales en documentos académicos profesionales (ej. en LaTeX).

## 1. Estructura de Coherencia (El Hilo Conductor)
Un informe coherente no solo lista categorías, sino que cuenta una historia sobre el fenómeno:
1.  **Contexto/Anclaje:** Iniciar con la base histórica o cultural del fenómeno (ej. "La categoría Salud se ancla en el trauma colonial...").
2.  **Tensión/Conflicto:** Identificar la contradicción central en los datos (ej. "Existe una tensión entre el potencial deportivo y la fragilidad institucional").
3.  **Mecanismos de Resolución:** Explicar cómo los sujetos navegan esa tensión.
4.  **Teoría Sustantiva:** Concluir integrando los hallazgos en un modelo explicativo (ej. "El potencial al proyecto").

## 2. Principios de Escritura Semántica
- **Uso de Evidencia:** Toda afirmación debe ir seguida o precedida por una cita (`quote`) o una referencia a una nota de campo.
- **Transiciones Lógicas:** Usar conectores que reflejen la relación entre categorías (ej. "En paralelo a esta fragilidad, emergen estrategias de resiliencia...").
- **Evitar el "Silencio Analítico":** No dejar citas "huérfanas". Cada cita debe ser comentada y analizada bajo el lente del marco teórico.

## 3. Detección de Inconsistencias (Checklist para el AI)
Al revisar un texto, busca:
- `[ ]` **Saltos Lógicos:** ¿Pasamos de hablar de 'Migración' a 'Salud' sin una transición que explique la relación (ej. el impacto del desarraigo en el bienestar)?
- `[ ]` **Inconsistencia de Formato:** ¿Estamos usando estilos diferentes para hallazgos de similar jerarquía?
- `[ ]` **Falta de Voz:** ¿Se pierde la voz de la comunidad entre tecnicismos académicos?
- `[ ]` **Ambigüedad de Sujetos:** ¿Está claro quién dice qué? (Diferenciar entre investigadores, participantes y literatura).

## 4. Guía de Formato en LaTeX
Para mantener la coherencia visual:
- **Catetgorías Mayores:** Usar `\chapter` o `\section` según la profundidad.
- **Hallazgos Semánticos:** Usar el macro `\hallazgo{...}` para destacar el nombre de la categoría.
- **Testimonios:** Envolver en entornos `\begin{quote} ... \end{quote}` para distinguir la voz del participante de la del investigador.
