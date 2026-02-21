import re
import json

filename = '/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/guia_matematicas_soluciones.tex'

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

data_dict = {}
current_materia = None
current_semestre = None
current_pregunta_num = None
current_enunciado = []
current_solucion = []

state = None # 'enunciado' or 'solucion'

def save_current(materia, semestre, num, enunc, sol):
    if num is None:
        return
    enunc_str = "".join(enunc).strip()
    sol_str = "".join(sol).strip()
    enunc_str = re.sub(r'\\vspace\{.+?\}\s*$', '', enunc_str).strip()
    sol_str = re.sub(r'\\vspace\{.+?\}\s*$', '', sol_str).strip()
    
    key = (materia, semestre, num)
    if key in data_dict:
        # Keep the one with the longer solution
        if len(sol_str) > len(data_dict[key]['solucion']):
            data_dict[key]['enunciado'] = enunc_str
            data_dict[key]['solucion'] = sol_str
    else:
        data_dict[key] = {
            "año-semestre": semestre,
            "numero de pregunta": num,
            "materia": materia,
            "enunciado": enunc_str,
            "solucion": sol_str
        }

for line in lines:
    line_strip = line.strip()
    
    m_section = re.search(r'\\section\*?\{(.+?)\}', line_strip)
    if m_section:
        if "Tabla de Respuestas" in m_section.group(1):
            break
        current_materia = m_section.group(1).strip()
        continue
        
    m_subsection = re.search(r'\\subsection\*?\{(.+?)\}', line_strip)
    if m_subsection:
        current_semestre = m_subsection.group(1).strip()
        continue
        
    m_subsubsection = re.search(r'\\subsubsection\*?\{Pregunta\s+(\d+)\s*-\s*.+?\}', line_strip)
    if m_subsubsection:
        save_current(current_materia, current_semestre, current_pregunta_num, current_enunciado, current_solucion)
        current_pregunta_num = int(m_subsubsection.group(1))
        current_enunciado = []
        current_solucion = []
        state = None
        continue
        
    if line_strip == r'\textbf{Enunciado:}':
        state = 'enunciado'
        continue
        
    if line_strip == r'\textbf{Solución:}':
        state = 'solucion'
        continue
        
    if state == 'enunciado':
        current_enunciado.append(line)
    elif state == 'solucion':
        current_solucion.append(line)

save_current(current_materia, current_semestre, current_pregunta_num, current_enunciado, current_solucion)

final_data = list(data_dict.values())

with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/ejercicios_matematicas.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print(f"Successfully extracted {len(final_data)} items.")
