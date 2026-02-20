import os
import re
import shutil
import glob

# Configuration
SOURCE_DIR = "/home/fabian/src/fundamentals/respositorio-fundamentals/otro repo/docs/science/thermodynamics/exercises"
TARGET_DIR = "/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia termodinamica"
IMAGES_DIR = os.path.join(TARGET_DIR, "images")
OUTPUT_FILE = os.path.join(TARGET_DIR, "guia_termodinamica_enunciados.tex")

# Template parts
HEADER = r"""\documentclass{article}
\usepackage{fullpage}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage[spanish]{babel}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{cancel}
\usepackage{booktabs} 
\usepackage{tikz}
\usepackage{float}


%%%%% Comandos Personalizados %%%%%
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\la}{\leftarrow}
\newcommand{\ra}{\rightarrow}
\newcommand{\lra}{\leftrightarrow}
\newcommand{\Ra}{\Rightarrow}
\newcommand{\La}{\Leftarrow}
\newcommand{\LRa}{\Leftrightarrow}
\newcommand{\sub}{\subseteq}
\newcommand{\matro}{\mathcal{M}}

\newcommand{\twopartdef}[4]
{
	\left\{
		\begin{array}{ll}
			#1 &  \text{#2} \\
			#3 &  \text{#4}
		\end{array}
	\right.
}

%%%%%  Fin Comandos Personalizados %%%%%

 %%%%%%%%%% MODIFICAR %%%%%%%%%%
\newcommand{\alumnos}{Antigravity Agent}
\newcommand{\departamento}{Departamento de Ingenieria Industrial y de Sistemas}
\newcommand{\ramo}{Termodinamica}
\newcommand{\sigla}{ICS2123}
\newcommand{\titulo}{Guia de Ejercicios}
\newcommand{\semestre}{01}
\newcommand{\anio}{2026}
\newcommand{\med}{\frac{1}{2}}
\newcommand{\indep}{\mathcal{I}}
%%%%%%%%%% FIN MODIFICAR %%%%%%%%%%

\renewcommand{\thesubsection}{\alph{subsection}}


\usepackage{tikz}
\usetikzlibrary{arrows.meta}


\begin{document}
\title{Guía de Ejercicios Termodinámica}
\maketitle
"""

FOOTER = r"""
\end{document}
"""

def clean_latex_text(text):
    # Removing MDX/HTML tags
    text = re.sub(r'<div className="exercise">', '', text)
    text = re.sub(r'</div>', '', text)
    text = re.sub(r'<MDXDetails>.*?</MDXDetails>', '', text, flags=re.DOTALL)
    text = re.sub(r'<Disqus.*?>', '', text, flags=re.DOTALL)
    text = re.sub(r':::info.*?:::', '', text, flags=re.DOTALL)
    
    # Fix common LaTeX issues from MDX
    # Replace <br> with newline
    text = text.replace('<br>', '\\\\')
    text = text.replace('<br/>', '\\\\')
    
    return text.strip()

def process_images(content, year, question_num):
    # Find images in markdown format ![alt](path) or <img src="path" ... />
    # We assume images are relative to the MDX file.
    # We need to copy them to TARGET_DIR/images and update the path in content.
    
    # Pattern for markdown images: ![alt](url)
    def repl_md(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        
        # Resolve absolute path of the image source
        # The MDX files often use relative paths like ./images/fig.png or just plain filename if in same dir
        # But looking at file listings, it seems there is no strictly 'images' folder in every 20xx-x folder?
        # Let's check if the path is relative or absolute.
        
        # Construct source path.
        # Check if it starts with @site indicating project root
        if img_path.startswith("@site"):
             # Need to map @site to actual path.
             # Assuming @site is /home/fabian/src/fundamentals/respositorio-fundamentals/otro repo
             real_path = img_path.replace("@site", "/home/fabian/src/fundamentals/respositorio-fundamentals/otro repo")
        elif img_path.startswith("http"):
             return match.group(0) # Logic for remote images not implemented, keep as is
        else:
             # Relative path
             # The source MDX is in SOURCE_DIR/year/pXX.mdx
             # So image is relative to SOURCE_DIR/year
             real_path = os.path.join(SOURCE_DIR, year, img_path)

        if not os.path.exists(real_path):
             # Try finding it in a generic images folder if not found?
             print(f"Warning: Image not found at {real_path}")
             return match.group(0)
             
        # Define new filename to avoid collisions
        ext = os.path.splitext(real_path)[1]
        new_filename = f"{year}_{question_num}_{os.path.basename(real_path)}"
        target_path = os.path.join(IMAGES_DIR, new_filename)
        
        # Copy file
        shutil.copy2(real_path, target_path)
        
        # Return LaTeX includegraphics
        return f"\\begin{{center}}\n    \\includegraphics[width=0.6\\textwidth]{{images/{new_filename}}}\n\\end{{center}}"

    # Pattern for HTML images: <img src="..." />
    # Not implementing fully for now unless we see them, focusing on standard markdown/mdx patterns likely used.
    # The view_file output showed `import Image from "@site/src/components/Image";` but didn't show actual usage in p34.mdx.
    # Looking at p18_2019_2.png in the chemical guide log, suggests `images/` relative path in latex.
    
    # Text replacement
    # Regex for standard markdown image
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', repl_md, content)
    
    # If there are specific Image components like <Image ... />, we need to handle them.
    # Example: <Image src="..." />
    # For now let's assume standard markdown or compatible.
    
    return content

def extract_questions():
    years = sorted([d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))])
    
    latex_content = ""
    answer_key = []

    for year in years:
        if year.startswith('.'): continue
        if year == "images": continue # Skip images dir if present
        
        latex_content += f"\\section{{{year}}}\n"
        
        year_path = os.path.join(SOURCE_DIR, year)
        files = sorted(glob.glob(os.path.join(year_path, "*.mdx")))
        
        for file_path in files:
            filename = os.path.basename(file_path)
            # define question number from filename i.e. p26.mdx -> 26
            match = re.search(r'p(\d+)', filename)
            if match:
                q_num = match.group(1)
            else:
                q_num = "00" # fallback

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic parsing
            # Remove frontmatter
            content = re.sub(r'^---[\s\S]*?---', '', content).strip()
            
            # Extract content until "Solución propuesta" or similar
            # The structure seems to be:
            # # Pregunta XX
            # <div className="exercise">
            # ... text ...
            # </div>
            # <MDXDetails> ...
            
            # Let's extract the text inside <div className="exercise">...</div> closest to top
            exercise_match = re.search(r'<div className="exercise">(.*?)</div>', content, re.DOTALL)
            if exercise_match:
                exercise_text = exercise_match.group(1)
            else:
                # Fallback: extract everything before MDXDetails
                exercise_text = content.split('<MDXDetails>')[0]
            
            # Clean up content
            exercise_text = clean_latex_text(exercise_text)
            
            # Process images
            exercise_text = process_images(exercise_text, year, q_num)
            
            # Format alternatives for LaTeX usually are just text in the MDX
            # e.g a) ..
            # We want to ensure they look good.
            # Convert $$ ... $$ to \[ ... \] or keep as is? Latex supports $$ usually but \[ is better.
            # The template uses $$ so we keep it.
            
            latex_content += f"\\subsection*{{Pregunta {q_num} - {year}}}\n"
            latex_content += exercise_text + "\n"
            latex_content += "\\vspace{0.5cm}\n"
            
            # Store for answer key (empty for now)
            answer_key.append({'year': year, 'q': q_num, 'a': ''})

    return latex_content, answer_key

def generate_answer_table(answer_key):
    # Split into two columns logic
    # We want a table with Year | Pre | Res || Year | Pre | Res
    
    rows = []
    mid = (len(answer_key) + 1) // 2
    
    col1 = answer_key[:mid]
    col2 = answer_key[mid:]
    
    # Pad col2 if necessary
    while len(col2) < len(col1):
        col2.append(None)
        
    table_latex = "\\newpage\n\\section*{Tabla de Respuestas}\n\\begin{center}\n"
    table_latex += "\\begin{tabular}{|c|c|c||c|c|c|}\n\\hline\n"
    table_latex += "\\textbf{Año} & \textbf{Pre.} & \textbf{Res.} & \textbf{Año} & \textbf{Pre.} & \textbf{Res.} \\\\\n\\hline\n"
    
    for c1, c2 in zip(col1, col2):
        row_str = f"{c1['year']} & {c1['q']} & {c1['a']} & "
        if c2:
            row_str += f"{c2['year']} & {c2['q']} & {c2['a']} \\\\"
        else:
            row_str += " & & \\\\"
        table_latex += row_str + "\n"
        
    table_latex += "\\hline\n\\end{tabular}\n\\end{center}\n"
    return table_latex

def main():
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    content, keys = extract_questions()
    table = generate_answer_table(keys)
    
    full_latex = HEADER + content + table + FOOTER
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_latex)
    
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
