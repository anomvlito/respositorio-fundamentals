import json
import re

json_file = '/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/ejercicios_matematicas.json'
out_enunciados = '/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/guia_matematicas_enunciados.tex'
out_soluciones = '/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/guia_matematicas_soluciones.tex'

with open(json_file, 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Agrupamos por año-semestre
por_semestre = {}
for ej in datos:
    semestre = ej['año-semestre']
    if semestre not in por_semestre:
        por_semestre[semestre] = []
    por_semestre[semestre].append(ej)

# Ordenamos semestres
semestres_ordenados = sorted(por_semestre.keys())
# Para cada semestre, ordenamos por numero de pregunta
for sem in semestres_ordenados:
    por_semestre[sem].sort(key=lambda x: x['numero de pregunta'])

def parse_respuesta(solucion):
    # Buscamos "Respuesta Correcta: X)"
    match = re.search(r'Respuesta Correcta:\s*([a-eA-E])', solucion)
    if match:
        return match.group(1).lower()
    return ""

def generar_encabezado(tipo):
    titulo = "Guía de Ejercicios Matemáticas (Cálculo, EDO, Álgebra Lineal, Probabilidades)"
    if tipo == "solucionario":
        titulo = "Solucionario " + titulo
    return f"""\\documentclass{{article}}
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

"""

def generar_pie():
    return r"""
\vfill
\begin{center}
    \small Puedes ver este repositorio en \url{https://github.com/anomvlito/respositorio-fundamentals}
\end{center}

\end{document}
"""

with open(out_enunciados, 'w', encoding='utf-8') as fe, \
     open(out_soluciones, 'w', encoding='utf-8') as fs:
    
    fe.write(generar_encabezado("enunciados"))
    fs.write(generar_encabezado("solucionario"))
    
    respuestas_tabla = []
    
    for sem in semestres_ordenados:
        fe.write(f"\\section{{{sem}}}\n\n")
        fs.write(f"\\section{{{sem}}}\n\n")
        
        for ej in por_semestre[sem]:
            num = ej['numero de pregunta']
            materia = ej['materia']
            enunciado = ej['enunciado']
            solucion = ej['solucion']
            respuesta = parse_respuesta(solucion)
            
            respuestas_tabla.append({
                'ano': sem,
                'pre': num,
                'res': respuesta
            })
            
            # Bloque de Enunciado
            bloque_enun = f"\\subsection*{{Pregunta {num} - {sem} ({materia})}}\n"
            # Aseguramos que el label comience con \textbf{Enunciado:}
            if not enunciado.strip().startswith(r"\textbf{Enunciado:}"):
                bloque_enun += "\\textbf{Enunciado:}\n\n"
            bloque_enun += enunciado + "\n\\vspace{0.5cm}\n\n"
            fe.write(bloque_enun)
            
            # Bloque de Solucion
            bloque_sol = f"\\subsection*{{Pregunta {num} - {sem} ({materia})}}\n"
            if not enunciado.strip().startswith(r"\textbf{Enunciado:}"):
                bloque_sol += "\\textbf{Enunciado:}\n\n"
            
            # En el solucionario normalmente se pone una version resumida o entera del enunciado, dejaremos entera
            bloque_sol += enunciado + "\n\n"
            
            if not solucion.strip().startswith(r"\textbf{Solución:}"):
                bloque_sol += "\\textbf{Solución:}\n\n"
            bloque_sol += solucion + "\n\\vspace{0.5cm}\n\n"
            fs.write(bloque_sol)

    # Tabla de respuestas solo en enunciados
    fe.write("\\newpage\n\\begingroup\n\\let\\clearpage\\relax\n\\vspace*{1cm}\n\\section*{Tabla de Respuestas}\n\\begin{center}\n\\begin{tabular}{|c|c|c||c|c|c|}\n\\hline\n")
    fe.write("\\textbf{Año} & \\textbf{Pre.} & \\textbf{Res.} & \\textbf{Año} & \\textbf{Pre.} & \\textbf{Res.} \\\\ \\hline\n")
    
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
        fe.write(fila + "\n")
    
    fe.write("\\hline\n\\end{tabular}\n\\end{center}\n\\endgroup\n")
    
    fe.write(generar_pie())
    fs.write(generar_pie())

print("Archivos generados correctamente.")
