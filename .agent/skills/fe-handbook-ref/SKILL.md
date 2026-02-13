---
name: fe-handbook-ref
description: Expert skill for retrieving and integrating formulas from the NCEES FE Reference Handbook (10.1) into LaTeX documents. strictly following the UC Fundamentals context. Maps printed pages to PDF indices to handle custom versions.
---

# FE Handbook Reference Skill

## When to use this skill
**ALWAYS** use this skill when you need:
- To find a formula, constant, or table from the FE Handbook.
- To cite a specific page of the handbook in a solution (e.g., MAT16xx courses).
- To ensure LaTeX formulas exactly match the "official" version provided by UC engineering fundamentals.

## 1. Interaction Protocol

1.  **Identify the need**: "I need the formula for [Concept] from the handbook."
2.  **Query the mapping**: Check `resources/handbook_map.json` or use `scripts/query_handbook.py` (if keyword search is needed).
3.  **Coordinate with mapping**: Ensure the page number cited corresponds to the *printed* page in the metadata, while any image extraction uses the *PDF index*.
4.  **Integrate**: Use `latex-illustrator` to insert the LaTeX snippet or screenshot if requested.

## 2. Handbook Organization (Mapped)

| Section | Handbook Page (Printed) | PDF Page (Index) |
|---------|-------------------------|------------------|
| **Units & Conversion Factors** | 1-3 | 7-9 |
| (Gap / Ethics / Safety) | 4-33 | 10-39 |
| **Mathematics** | 34-62 | 40-68 |
| **Probability & Statistics** | 63-84 | 69-90 |
| **Chemistry & Biology** | 85-93 | 91-99 |
| **Materials Science** | 94-106 | 100-112 |
| **Statics** | 107-113 | 113-119 |
| **Dynamics** | 114-129 | 120-135 |
| **Mechanics of Materials** | 130-142 | 136-148 |
| **Thermodynamics** | 143-176 | 149-182 |
| **Fluid Mechanics** | 177-203 | 183-209 |
| **Heat Transfer** | 204-219 | 210-225 |
| **Instrumentation & Controls** | 220-229 | 226-235 |
| **Engineering Economics** | 230-237 | 236-243 |
| Chemical / Civil / Electrical (Images) | 238-269 | 244-275 |

> [!NOTE]
> The range 4-33 typically covers Ethics and Safety in other versions, but in this 10.1 mapping, it appears as a gap or general text. Pages 238-269 cover the remaining discipline-specific sections (Chemical, Civil, Electrical, etc.) which are currently mapped primarily via providing the page image.

## 3. Usage Examples

### Example: Quadratic Formula
"Look up the quadratic formula from the handbook."
1. Skill finds: `ax^2+bx+c=0 \Rightarrow x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}` (Handbook p. 35).
2. Agent provides:
   ```latex
   Según el Manual de Referencia FE (pág. 35), las raíces son:
   \[ x = \frac{-b \pm \sqrt{b^2-4ac}}{2a} \]
   ```

### Example: Image Reference
"Show me the Interest Factor table for 10%."
1. Skill maps to Economics section.
2. Agent extracts/screenshots the relevant section from the PDF index.

## 4. Best Practices
- **No Hallucinations**: Only use formulas present in the Handbook. If it's not there, state it clearly.
- **Page Citing**: Always include the printed page number in the final output to help the student find it in their physical/PDF copy.
- **LaTeX Accuracy**: Ensure exponents, subscripts, and square roots are rendered precisely.
- **Visuals First**: For complex diagrams (Mollier charts, psychrometric graphs, circuit diagrams), prefer using the **extracted page image** (`pX_content.png`) available in the JSON map over attempting to recreate them in LaTeX.

## 5. Image Resources (Full Coverage)
The skill now maintains a **complete visual map** of the Handbook:
- **Coverage:** Handbook Pages 1 to 269 (PDF Pages 7-275).
- **Access:** Each page entry in `resources/handbook_map.json` contains a block of type `image` pointing to `resources/images/p{page}_content.png`.
- **Usage:** Use these images to provide ground-truth visual context for any query.

## 6. Proactive Solving Strategy (Reverse Lookup)
When solving exercises, the skill should be used *proactively* to link concepts to the Handbook:
1.  **Analyze the Problem**: Identify key concepts (e.g., "Integration by Parts", "Series Convergence", "Cramer's Rule").
2.  **Search the Map**: Use `grep` or `search_exercises.py` on `handbook_map.json` to find relevant pages.
3.  **Cite in Solution**: Explicitly mention the Handbook page and formula in the LaTeX solution.
    - Example: `...usando la fórmula de integración por partes (Manual FE, pág. 47)...`
    - Example: `...según la tabla de transformadas de Laplace (Manual FE, pág. 54)...`
4.  **Verify Notation**: Ensure the solution uses the same variable names and conventions as the Handbook where possible.
5.  **Silent Omission**: If a concept is fundamental (e.g., basic algebra, graph of log x) or simply not present in the Handbook (e.g., specific named theorems like Wald's Identity), do *not* add a citation. Do not say "Not found". Just omit it to keep the solution clean.
    - However, for major engineering formulas that *should* be there but aren't, verify against the search script before omitting.
