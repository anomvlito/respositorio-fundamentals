---
name: math-solver-style
description: Estándar rector de estilo, flujo semántico en español y desarrollo continuo para todos los resolvedores. Use when user asks to "verificar estilo de las soluciones", "aplicar el estilo matemático", "auditar conectores en español", "revisar formato de resolución", or "validar flujo semántico de matemáticas".
---

# Math Solver Style Guide (Mathematics)

Esta skill es la **piedra angular** del estilo y formato de redacción de soluciones para cualquier evaluación de matemáticas. Es imperativo que toda respuesta matemática o código fuente LaTeX generado siga de forma estricta las pautas aquí establecidas.

---

## 1. El Flujo Semántico del Lenguaje (Estilo Explicativo)

Las transiciones entre pasos de cálculo matemático no deben ser mudas (solo fórmulas) ni pedagógicas (explicaciones teóricas extensas). Deben presentarse como una secuencia explicativa manuscrita por un estudiante brillante utilizando **conectores algebraicos breves en español** que indiquen de forma precisa la operación realizada.

### Conectores Algebraicos Autorizados (Lista Imperativa):
Toda transición debe apoyarse de manera natural en expresiones de este grupo:
* **Sustitución/Evaluación:** *"Reemplazando en..."*, *"Sustituyendo..."*, *"Evaluando en..."*
* **Integración:** *"Integrando a ambos lados..."*, *"Integrando respecto a..."*
* **Álgebra/Despeje:** *"Despejando..."*, *"Volviendo a la variable original..."*, *"Redefiniendo la constante..."*, *"Simplificando..."*
* **Cálculo de Derivadas:** *"Derivando respecto a..."*, *"Diferenciando a ambos lados..."*, *"Derivando usando la regla de..."*
* **EDO Homogénea:** *"Para resolver la homogénea asociada..."*, *"Proponiendo la solución..."*, *"La ecuación característica es..."*
* **Condiciones:** *"Aplicando la condición inicial..."*, *"Por condición de borde..."*, *"Como la coordenada está en el primer cuadrante..."*

---

## 2. Desarrollo Continuo y Fluidez

* **Prohibición de Títulos Artificiales:** Queda terminantemente prohibido subdividir el desarrollo de una pregunta usando títulos artificiales, viñetas de fases o enumeraciones estructurales internas (e.g., *"Paso 1: Separar variables"*, *"Sección B: Reducción"*).
* **Formato Continuo:** El desarrollo debe fluir como una única secuencia matemática continua. Los saltos de línea deben emplearse exclusivamente para separar los bloques de cálculo, y cada bloque debe estar precedido por el breve conector en español correspondiente.
* **Proscripción de Fluff Pedagógico:** Evitar introducciones conversacionales (e.g., *"¡Claro! Vamos a resolver paso a paso este ejercicio..."*), comentarios sobre el nivel de dificultad o explicaciones cualitativas que no aporten directamente a la obtención del puntaje del certamen.

---

## 3. Protocolo de Auditoría y Homologación de Skills

Siempre que se lea, modifique o invoque una skill resolvedora de matemáticas en el directorio de trabajo (como [[tutor-calculus-1]](../tutor-calculus-1/SKILL.md), [[tutor-calculus-2]](../tutor-calculus-2/SKILL.md), [[tutor-calculus-3]](../tutor-calculus-3/SKILL.md), [[tutor-ode]](../tutor-ode/SKILL.md), [[tutor-prob-stats]](../tutor-prob-stats/SKILL.md) o el orquestador [[exercise-solver]](../exercise-solver/SKILL.md)), se debe:

1. **Auditar la sección de Estilo (Exam Resolution Style):** Verificar si incluye directrices explícitas sobre el flujo semántico, conectores en español y formato de desarrollo continuo.
2. **Inyectar la referencia imperativa:** Si la skill no incluye estas reglas, se debe modificar su archivo `SKILL.md` para incluir el siguiente bloque de alineación imperativa:

```markdown
## Exam Resolution Style & Semantic Flow
- **Estilo de Resolución:** Toda solución debe cumplir rigurosamente con las directrices de flujo semántico del lenguaje definidas en la skill rectora [[math-solver-style]](../math-solver-style/SKILL.md).
- **Conectores obligatorios:** Es imperativo usar exclusivamente conectores algebraicos breves en español (e.g., *"reemplazando en"*, *"integrando"*, *"volviendo a la variable original"*) para conectar los pasos del desarrollo.
- **Sin subtítulos:** Presentar el desarrollo en formato continuo, libre de títulos artificiales o explicaciones pedagógicas ajenas al certamen.
```

3. **Verificar consistencia:** Modificar la skill auditada de inmediato y asegurar que ningún desarrollo matemático generado por ella se desvíe de este estándar.
