---
name: fe-handbook-ref
description: Expert skill for retrieving and integrating formulas from the NCEES FE Reference Handbook (10.1) into LaTeX documents. Provides full-text search via content_raw and image references for every page. Maps printed pages to PDF indices across three offset zones.
---

# FE Handbook Reference Skill

## When to use this skill
**ALWAYS** use this skill when you need:
- To find a formula, constant, or table from the FE Handbook.
- To cite a specific page of the handbook in a solution (e.g., MAT16xx courses).
- To ensure LaTeX formulas exactly match the "official" version provided by UC engineering fundamentals.

## 1. Interaction Protocol

1.  **Identify the need**: "I need the formula for [Concept] from the handbook."
2.  **Search by keyword**: Use `grep` on the `content_raw` field in `resources/handbook_map.json`:
    ```bash
    grep -i "laplace" resources/handbook_map.json | head -5
    ```
    Or use a Python one-liner for structured results:
    ```bash
    python3 -c "
    import json
    d = json.load(open('resources/handbook_map.json'))
    for p in d['pages']:
        if 'laplace' in p.get('content_raw','').lower() or 'laplace' in p.get('title','').lower():
            print(f'Page {p[\"handbook_page\"]} (pdf {p[\"pdf_index\"]}): {p[\"title\"]}')
    "
    ```
3.  **Locate the page**: Note the `handbook_page` (printed number for citation) and `pdf_index` (for image extraction).
4.  **Show the image**: Reference the page image at `resources/images/p{handbook_page}_content.png`.
5.  **Integrate**: Use `latex-illustrator` to insert the LaTeX snippet or image into the document.

## 2. Handbook Organization (Mapped)

> [!IMPORTANT]
> The handbook has **non-contiguous page numbering** with three offset zones.
> Pages 4-33 do NOT exist in the printed handbook (the numbering jumps from 3 to 34).

| Section | Printed Pages | PDF Pages | Offset |
|---------|--------------|-----------|--------|
| **Units & Conversion Factors** | 1–3 | 7–9 | +6 |
| **Mathematics** | 34–62 | 10–38 | −24 |
| **Probability & Statistics** | 63–84 | 39–60 | −24 |
| **Chemistry & Biology** | 85–93 | 61–69 | −24 |
| **Materials Science** | 94–106 | 70–82 | −24 |
| **Statics** | 107–113 | 83–89 | −24 |
| **Dynamics** | 114–129 | 90–105 | −24 |
| **Mechanics of Materials** | 130–142 | 106–118 | −24 |
| **Thermodynamics** | 143–176 | 119–152 | −24 |
| **Fluid Mechanics** | 177–203 | 153–179 | −24 |
| **Heat Transfer** | 204–219 | 180–195 | −24 |
| **Instrumentation & Controls** | 220–229 | 196–205 | −24 |
| **Engineering Economics** | 230–237 | 206–213 | −24 |
| **Electrical & Computer Eng.** | 355–416 | 214–275 | −141 |

> [!NOTE]
> Use `handbook_page` (printed number) when citing in LaTeX. Use `pdf_index` for image extraction from the PDF.

## 3. Usage Examples

### Example: Keyword Search → LaTeX Citation
"I need the Laplace transform table."
1.  Search: `grep -i "laplace" handbook_map.json` → finds page 56 (Laplace Transforms).
2.  Show image: `resources/images/p56_content.png`.
3.  Cite in LaTeX:
    ```latex
    Según el Manual de Referencia FE (pág. 56):
    \[ \mathcal{L}\{e^{at}\} = \frac{1}{s-a} \]
    ```

### Example: Image Reference
"Show me the Interest Factor table for 10%."
1. Search: `grep -i "interest" handbook_map.json` → finds pages 230-237.
2. Show the relevant page image from `resources/images/`.

### Example: Proactive Reverse Lookup
When solving an exercise about integration by parts:
1.  Search: `grep -i "integration.*parts\|parts.*integration" handbook_map.json`.
2.  Find page 47 → cite: `...usando la fórmula (Manual FE, pág. 47)...`

## 4. Best Practices
- **No Hallucinations**: Only use formulas present in the Handbook. If it's not there, state it clearly.
- **Page Citing**: Always use the `handbook_page` (printed number) in citations.
- **LaTeX Accuracy**: Ensure exponents, subscripts, and square roots are rendered precisely.
- **Visuals First**: For complex diagrams (Mollier charts, psychrometric graphs, circuit diagrams), prefer using the **extracted page image** (`pX_content.png`) over attempting to recreate them in LaTeX.
- **Silent Omission**: If a concept is not in the Handbook (e.g., named theorems like Wald's Identity), do *not* add a citation. Just omit it to keep the solution clean.

## 5. Image Resources (Full Coverage)
- **269 entries** covering printed pages 1–3 and 34–237 and 355–416 (all PDF pages 7–275).
- Each entry in `resources/handbook_map.json` has:
  - `title`: descriptive section/topic name
  - `content_raw`: full extracted text (searchable)
  - `blocks[].type: "image"` → path to `resources/images/p{handbook_page}_content.png`
- Use these images to provide ground-truth visual context for any query.

## 6. Proactive Solving Strategy
When solving exercises:
1.  **Analyze**: Identify key concepts (e.g., "Integration by Parts", "Series Convergence", "Cramer's Rule").
2.  **Search**: Use `grep -i` on `handbook_map.json` to find relevant pages via `content_raw` or `title`.
3.  **Cite**: Mention the Handbook page and formula in the LaTeX solution.
4.  **Verify**: Ensure variable names and conventions match the Handbook.
5.  **Omit silently**: For fundamental/absent concepts, do not force a citation.
