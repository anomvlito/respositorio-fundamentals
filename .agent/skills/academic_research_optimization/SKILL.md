---
name: academic_research_optimization
description: Global skill for standardizing academic paper structures, detecting semantic redundancies, and optimizing visual readability for scholarly documents.
---

# Academic Research & Paper Optimization

This skill provides a framework for transforming raw research data into high-quality, professional academic papers. It focuses on structural integrity, semantic precision, and visual ergonomics.

## 1. Standard Paper Architecture
When drafting or reviewing an academic document, ensure the following flow:
1.  **Title:** Descriptive, concise, and professional.
2.  **Abstract:** A single paragraph (200-300 words) summarizing the background, method, key findings, and implications.
3.  **Introduction:** Establish the problem, context, and the research objective.
4.  **Methodology:** Transparent description of data collection and analysis (e.g., Grounded Theory, Talanoa).
5.  **Results/Analysis:** Presentation of findings, often structured by categories or themes.
6.  **Discussion:** Interpretation of findings, connection to existing literature, and theory building.
7.  **Conclusion:** Final summary, limitations, and future research directions.

## 2. Semantic Analysis & Redundancy Detection
Use this protocol to prune and refine text:
- **Redundancy Filter:** Identify phrases that repeat the same information (e.g., "The findings showed results that indicate..."). 
- **Circular Reasoning:** Check if the analysis simply restates the raw data without adding interpretive value.
- **Clarity vs. Complexity:** Replace "academic jargon" with precise terminology if the jargon doesn't add technical value.
- **Evidence Coupling:** Ensure every interpretive claim is immediately supported by evidence (quotes or data points).

## 3. Visual Readability & Ergonomics
Optimizing how the reader "consumes" the document:
- **Header Hierarchy:** Ensure sections, subsections, and paragraphs follow a logical nesting order.
- **Density Control:** Avoid "walls of text." Break paragraphs longer than 10-12 lines.
- **List Usage:** Use `itemize` or `enumerate` for multi-point findings, but keep items concise.
- **Information Scannability:** Use bold terms or custom macros (like `\hallazgo`) for key concepts so a reader can grasp the core idea by skimming.

## 4. Academic Tone Principles
- **Objectivity:** Use neutral, analytical language rather than emotional or biased phrasing.
- **Precision:** Use specific terms (e.g., "marginalized" instead of "small") and quantify whenever possible.
- **Hedge Language:** Use terms like "suggests," "indicates," or "potential" for findings that are not definitive.

## 5. LaTeX Best Practices for Papers
- **Class:** Use `article` with `twocolumn` for paper formats.
- **Packages:** Always include `xurl` for bibliography URLs and `abstract` for proper summary formatting.
- **Macros:** Define semantic commands (e.g., `\concept{...}`, `\tension{...}{...}`) to maintain a consistent visual language across the document.
