import json
import os
import re

def sanitize_latex(text):
    if not text:
        return ""
    # Escaping special LaTeX characters in text mode
    replacements = {
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
        "~": "\\textasciitilde{}",
        "^": "\\textasciicircum{}"
    }
    # Use regex to replace only if not already escaped (simplistic approach, be careful)
    # For this script, we assume input 'content' is raw text unless specified as latex
    escaped = ""
    for char in text:
        escaped += replacements.get(char, char)
    return escaped

def generate_latex():
    # Paths
    json_path = ".agent/skills/fe-handbook-ref/resources/handbook_map.json"
    output_path = "handbook_verification.tex"
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    latex_content = [
        "\\documentclass[10pt]{article}",
        "\\input{estilos.tex}",
        "\\title{Manual de Referencia FE - Verificación de Transcripción}",
        "\\author{UC Fundamentals Premium}",
        "\\date{\\today}",
        "\\begin{document}",
        "\\maketitle",
        "\\tableofcontents",
        "\\newpage"
    ]

    for page in data.get("pages", []):
        hp = page.get("handbook_page")
        pdf = page.get("pdf_index")
        raw_title = page.get("title", f"Página {hp}")
        title = sanitize_latex(raw_title)
        
        latex_content.append(f"\\section{{{title}}}")
        latex_content.append(f"\\textbf{{Mapeo:}} Handbook P{hp} $\\rightarrow$ PDF Index {pdf}\\\\")
        latex_content.append("\\rule{\\linewidth}{0.5pt}\\\\")

        for block in page.get("blocks", []):
            btype = block.get("type")
            raw_heading = block.get("heading", "")
            heading = sanitize_latex(raw_heading)
            
            if heading:
                latex_content.append(f"\\subsection*{{{heading}}}")
            
            if btype == "text":
                content = block.get("content", "")
                latex_content.append(sanitize_latex(content) + "\\\\")
            
            elif btype == "formulas":
                intro = block.get("content", "")
                if intro:
                    latex_content.append(sanitize_latex(intro) + "\\\\")
                
                latex_content.append("\\begin{itemize}")
                for item in block.get("items", []):
                    name = item.get("name", "")
                    latex = item.get("latex", "")
                    # Ensure latex content is valid math mode content
                    if name:
                        latex_content.append(f"  \\item \\textbf{{{sanitize_latex(name)}}}: ${latex}$")
                    else:
                        latex_content.append(f"  \\item ${latex}$")
                latex_content.append("\\end{itemize}")
            
            elif btype == "table":
                latex_tbl = block.get("latex", "")
                latex_content.append("\\begin{center}")
                latex_content.append(latex_tbl)
                latex_content.append("\\end{center}")
            
            elif btype == "image":
                img_path = block.get("path", "")
                caption = sanitize_latex(block.get("caption", ""))
                
                # Adjust relative path for compilation from root
                # If path starts with .agent, keep it (running from root)
                if not os.path.exists(img_path):
                     latex_content.append(f"\\textbf{{[MISSING IMAGE: {sanitize_latex(img_path)}]}}\\\\")
                else:
                    latex_content.append("\\begin{figure}[H]")
                    latex_content.append("  \\centering")
                    latex_content.append(f"  \\includegraphics[width=0.8\\linewidth]{{{img_path}}}")
                    if caption:
                        latex_content.append(f"  \\caption{{{caption}}}")
                    latex_content.append("\\end{figure}")
            
            elif btype == "symbols":
                latex_content.append("\\begin{itemize}")
                for item in block.get("items", []):
                    sym = item.get("symbol", "")
                    desc = item.get("description", "")
                    latex_content.append(f"  \\item ${sym}$ : {sanitize_latex(desc)}")
                latex_content.append("\\end{itemize}")

        latex_content.append("\\newpage")

    latex_content.append("\\end{document}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_content))
    
    print(f"Success: {output_path} generated.")

if __name__ == "__main__":
    generate_latex()
