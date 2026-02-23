import re
import sys

def parse_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'\\subsection\*\{Pregunta\s+(\d+)\s+-\s+([0-9]{4}-[12])\s*\((.*?)\)\}(.*?)(?=\\subsection\*\{Pregunta|\Z)', re.DOTALL)
    matches = pattern.findall(content)
    
    parsed = []
    for m in matches:
        num = int(m[0])
        year = m[1]
        topic = m[2].strip()
        body = m[3]
        
        if r'\newpage' in body:
            body = body.split(r'\newpage')[0]
        elif r'\vfill' in body:
            body = body.split(r'\vfill')[0]
            
        if r'\section*{Tabla de Respuestas}' in body:
            body = body.split(r'\section*{Tabla de Respuestas}')[0]
            
        # extract res if present
        res_match = re.search(r'Respuesta Correcta:\s*([a-eA-E])', body)
        res = res_match.group(1).lower() if res_match else "-"
        
        parsed.append({
            'num': num,
            'year': year,
            'topic': topic,
            'body': body.strip(),
            'res': res
        })
        
    return parsed

def generate_grouped(parsed, header_type, is_sol):
    # Enforce stable ordering
    topics = ['Cálculo I, II y III', 'Ecuaciones Diferenciales', 'Álgebra Lineal', 'Probabilidad y Estadística']
    
    output = []
    
    titulo = "Guía de Ejercicios Matemáticas"
    if is_sol:
        titulo = "Solucionario " + titulo
        
    header = f"""\\documentclass{{article}}
\\usepackage{{fullpage}}
\\usepackage{{graphicx}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[spanish]{{babel}}
\\usepackage{{amssymb}}
\\usepackage{{amsmath}}
\\usepackage{{cancel}}
\\usepackage{{booktabs}} 
\\usepackage{{tikz}}
\\usepackage{{float}}
\\usepackage{{url}}
\\usepackage{{hyperref}}
\\hypersetup{{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=blue,
    pdftitle={{Guía de Matemáticas}},
    pdfpagemode=FullScreen,
}}
\\usetikzlibrary{{arrows.meta}}

%%%%% Comandos Personalizados %%%%%
\\newcommand{{\\N}}{{\\mathbb{{N}}}}
\\newcommand{{\\R}}{{\\mathbb{{R}}}}
\\newcommand{{\\Q}}{{\\mathbb{{Q}}}}
\\newcommand{{\\E}}{{\\mathbb{{E}}}}
\\newcommand{{\\PP}}{{\\mathbb{{P}}}}
\\newcommand{{\\la}}{{\\leftarrow}}
\\newcommand{{\\ra}}{{\\rightarrow}}
\\newcommand{{\\lra}}{{\\leftrightarrow}}
\\newcommand{{\\Ra}}{{\\Rightarrow}}
\\newcommand{{\\La}}{{\\Leftarrow}}
\\newcommand{{\\LRa}}{{\\Leftrightarrow}}
\\newcommand{{\\sub}}{{\\subseteq}}
\\newcommand{{\\matro}}{{\\mathcal{{M}}}}

\\newcommand{{\\twopartdef}}[4]
{{
        \\left\\{{
                \\begin{{array}}{{ll}}
                        #1 &  \\text{{#2}} \\\\
                        #3 &  \\text{{#4}}
                \\end{{array}}
        \\right.
}}

%%%%%  Fin Comandos Personalizados %%%%%

%%%%%%%%%% MODIFICAR %%%%%%%%%%
\\newcommand{{\\alumnos}}{{Solucionario Generado}}
\\newcommand{{\\departamento}}{{Departamento de Ingeniería Mecánica y Metalúrgica}}
\\newcommand{{\\ramo}}{{Matemáticas}}
\\newcommand{{\\sigla}}{{DIM100}}
\\newcommand{{\\titulo}}{{{titulo}}}
\\newcommand{{\\semestre}}{{Recopilación}}
\\newcommand{{\\anio}}{{2025}}
\\newcommand{{\\med}}{{\\frac{{1}}{{2}}}}
\\newcommand{{\\indep}}{{\\mathcal{{I}}}}
%%%%%%%%%% FIN MODIFICAR %%%%%%%%%%

\\renewcommand{{\\thesubsection}}{{\\alph{{subsection}}}}

\\begin{{document}}

\\title{{{titulo}}}
\\maketitle

\\tableofcontents
\\newpage

"""
    output.append(header)
    
    respuestas_tabla = []
    
    for t in topics:
        topic_qs = [q for q in parsed if q['topic'] == t]
        if not topic_qs: continue
        
        output.append(f"\\section{{{t}}}\n\n")
        
        years = sorted(list(set(q['year'] for q in topic_qs)))
        for y in years:
            output.append(f"\\subsection{{{y}}}\n\n")
            y_qs = [q for q in topic_qs if q['year'] == y]
            y_qs.sort(key=lambda x: x['num'])
            
            for q in y_qs:
                output.append(f"\\subsubsection*{{Pregunta {q['num']} - {q['year']}}}\n")
                # Add body
                output.append(q['body'].replace("{images/", "{../images/") + "\n\n\\vspace{0.5cm}\n\n")
                
                respuestas_tabla.append({
                    'ano': q['year'],
                    'pre': q['num'],
                    'res': q['res']
                })
                
    if not is_sol:
        output.append("\\newpage\n\\begingroup\n\\let\\clearpage\\relax\n\\vspace*{1cm}\n\\section*{Tabla de Respuestas}\n\\begin{center}\n\\begin{tabular}{|c|c|c||c|c|c|}\n\\hline\n")
        output.append("\\textbf{Año} & \\textbf{Pre.} & \\textbf{Res.} & \\textbf{Año} & \\textbf{Pre.} & \\textbf{Res.} \\\\ \\hline\n")
        
        n_resp = len(respuestas_tabla)
        mitad = (n_resp + 1) // 2
        for i in range(mitad):
            izq = respuestas_tabla[i]
            fila = f"{izq['ano']} & {izq['pre']} & {izq['res']}"
            der_idx = i + mitad
            if der_idx < n_resp:
                der = respuestas_tabla[der_idx]
                fila += f" & {der['ano']} & {der['pre']} & {der['res']} \\\\"
            else:
                fila += " & & & \\\\"
            output.append(fila + "\n")
        output.append("\\hline\n\\end{tabular}\n\\end{center}\n\\endgroup\n")

    footer = r"""
\vfill
\begin{center}
    \small Puedes ver este repositorio en \url{https://github.com/anomvlito/respositorio-fundamentals}
\end{center}

\end{document}
"""
    output.append(footer)
    
    return "".join(output)

print("Parsing enunciados...")
parsed_en = parse_file('../guia_matematicas_enunciados.tex')

print("Parsing soluciones...")
parsed_sol = parse_file('../guia_matematicas_soluciones.tex')

# Extract actual answers from the parsed solutions correctly
sol_lookup = {}
for qs in parsed_sol:
    key = (qs['year'], qs['num'])
    sol_lookup[key] = qs['res']

# Apply answers to enunciados
for q in parsed_en:
    key = (q['year'], q['num'])
    if key in sol_lookup:
        q['res'] = sol_lookup[key]
        
print("Writing files...")
with open('guia_matematicas_enunciados_por_tema_old.tex', 'w', encoding='utf-8') as f:
    f.write(generate_grouped(parsed_en, "enunciados", False))

with open('guia_matematicas_solucionespor_tema_old.tex', 'w', encoding='utf-8') as f:
    f.write(generate_grouped(parsed_sol, "solucionario", True))

print("Done")
