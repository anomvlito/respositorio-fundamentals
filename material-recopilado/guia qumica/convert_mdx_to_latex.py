import os
import re

root_dir = "/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia qumica"
output_file = os.path.join(root_dir, "guia_quimica_enunciados.tex")
skeleton_file = os.path.join(root_dir, "esqueleto.tex")

def read_preamble(skeleton_path):
    preamble = ""
    with open(skeleton_path, 'r', encoding='utf-8') as f:
        for line in f:
            if "\\begin{document}" in line:
                break
            preamble += line
    # Inject encoding packages if not present
    if "inputenc" not in preamble:
        preamble = preamble.replace("\\usepackage{fullpage}", "\\usepackage{fullpage}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}")
    
    # Remove minted if present to avoid compilation errors
    preamble = re.sub(r'\\usepackage\{minted\}\n', '', preamble)
    preamble = re.sub(r'\\usepackage\[linesnumbered,ruled,lined\]\{algorithm2e\}\n', '', preamble)

    return preamble

def parse_mdx(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Frontmatter
    content = re.sub(r'^---[\s\S]*?---\s*', '', content)
    
    # Remove Imports
    content = re.sub(r'import .*?;\s*', '', content)
    
    # Remove Title
    content = re.sub(r'# Pregunta \d+\s*', '', content)
    
    # Remove MDXDetails (Solution)
    content = re.sub(r'<MDXDetails>[\s\S]*?</MDXDetails>', '', content)
    
    # Remove Disqus
    content = re.sub(r'<Disqus[\s\S]*?/>', '', content)
    
    # Remove Comentarios header
    content = re.sub(r'### Comentarios', '', content)

    # Remove :::info blocks
    content = re.sub(r':::info[\s\S]*?:::', '', content)
    
    # Remove div wrappers but keep content
    content = re.sub(r'<div className="exercise">', '', content)
    content = re.sub(r'</div>', '', content)

    # Sanitize Unicode - REMOVED TO FIX MISSING CHARACTERS
    # content = re.sub(r'[^\x00-\x7F]+', '', content)
    
    # Convert Bold
    content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
    
    # Convert Italics
    content = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'\\textit{\1}', content) # Better regex for single asterisks
    
    # Markdown Images to LaTeX
    content = re.sub(r'<Image[\s\S]*?/>', r'\\textit{[Imagen no disponible en LaTeX]}', content)
    
    # Clean up empty lines
    content = content.strip()
    
    return content

def get_answer_key_table():
    return r"""
\newpage
\section*{Tabla de Respuestas}
\begin{center}
\begin{tabular}{|c|c|c||c|c|c|}
\hline
\textbf{Año} & \textbf{Pre.} & \textbf{Res.} & \textbf{Año} & \textbf{Pre.} & \textbf{Res.} \\
\hline
2016-1 & 09 & c & 2019-1 & 18 & d \\
2016-1 & 10 & d & 2019-1 & 19 & b \\
2016-1 & 11 & c & 2019-1 & 20 & b \\
\cline{1-3}
2016-2 & 07 & d & 2019-1 & 21 & a \\
\cline{4-6}
2016-2 & 08 & d & 2019-2 & 18 & d \\
2016-2 & 09 & d & 2019-2 & 19 & d \\
2016-2 & 10 & b & 2019-2 & 20 & b \\
\cline{1-3}
2017-1 & 07 & c & 2019-2 & 21 & b \\
\cline{4-6}
2017-1 & 08 & d & 2023-2 & 28 & a \\
2017-1 & 09 & a & 2023-2 & 29 & d \\
2017-1 & 10 & b & 2023-2 & 30 & b \\
\cline{1-3}
2017-2 & 07 & c & 2023-2 & 31 & a \\
2017-2 & 08 & a & 2023-2 & 32 & c \\
2017-2 & 09 & a & 2023-2 & 33 & d \\
\cline{4-6}
2017-2 & 10 & c & 2024-2 & 28 & a \\
\cline{1-3}
2018-1 & 07 & c & 2024-2 & 29 & a \\
2018-1 & 08 & b & 2024-2 & 30 & a \\
2018-1 & 09 & c & 2024-2 & 31 & c \\
2018-1 & 10 & a & 2024-2 & 32 & a \\
\cline{1-3}
2018-2 & 07 & b & 2024-2 & 33 & a \\
2018-2 & 08 & d & & & \\
2018-2 & 09 & d & & & \\
2018-2 & 10 & d & & & \\
\hline
\end{tabular}
\end{center}
"""

def main():
    preamble = read_preamble(skeleton_file)
    
    latex_content = [preamble, "\\begin{document}", "\\title{Guía de Ejercicios Química}", "\\maketitle"]
    
    # Get years/semesters sorted
    subdirs = sorted([d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and re.match(r'\d{4}-\d', d)])
    
    for subdir in subdirs:
        year_path = os.path.join(root_dir, subdir)
        latex_content.append(f"\\section{{{subdir}}}")
        
        # Get problems sorted
        files = sorted([f for f in os.listdir(year_path) if f.endswith('.mdx')])
        
        for filename in files:
            file_path = os.path.join(year_path, filename)
            question_content = parse_mdx(file_path)
            
            if question_content:
                # Extract question number from filename (p09.mdx -> 9)
                q_num = re.sub(r'\D', '', filename)
                # Format: Pregunta 09 - 2016-1
                latex_content.append(f"\\subsection*{{Pregunta {q_num} - {subdir}}}")
                latex_content.append(question_content)
                
                latex_content.append("\\vspace{0.5cm}")

    # Append Answer Key
    latex_content.append(get_answer_key_table())

    latex_content.append("\\end{document}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_content))

    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    main()
