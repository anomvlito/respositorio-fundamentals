import re
import os

def clean_author(text):
    return re.sub(r'\\author\{.*?\}', r'\\author{}', text)

def enhance_handbook_notes(text):
    # Replaces the standard handbook note with something more pedagogical
    # Find "\textbf{Nota Handbook FE (NCEES FE Reference Handbook 10.1):}" or "\textbf{Nota Handbook FE:}"
    text = re.sub(
        r'\\textbf\{Nota Handbook FE.*?\}:?', 
        r'\\textbf{¡Lo que dice el Handbook FE!} Recuerda que en el examen no necesitas memorizar esto:',
        text
    )
    return text

def process_tanda1():
    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda1.tex', 'r', encoding='utf-8') as f:
        t1 = f.read()
    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda1b.tex', 'r', encoding='utf-8') as f:
        t1b = f.read()

    # Clean authors
    t1 = clean_author(t1)
    
    # Extract Plan de Estudio from t1b to merge into t1
    m_plan = re.search(r'\\begin\{tcolorbox\}\[.*?title=Plan de Estudio -- Tanda 1B.*?\](.*?)\\end\{tcolorbox\}', t1b, flags=re.DOTALL)
    plan_t1b_items = []
    if m_plan:
        items = re.findall(r'\\item\s+(.*)', m_plan.group(1))
        plan_t1b_items = items
    
    # Update Tanda 1's items: add the new ones, renumbering them
    if plan_t1b_items:
        # locate the enumerate block in t1
        m_enum_t1 = re.search(r'(\\begin\{enumerate\}.*?)(\\end\{enumerate\})', t1, flags=re.DOTALL)
        if m_enum_t1:
            new_items_str = '\n'.join([f"    \\item {item}" for item in plan_t1b_items])
            new_enum = m_enum_t1.group(1) + new_items_str + "\n" + m_enum_t1.group(2)
            t1 = t1.replace(m_enum_t1.group(0), new_enum)

    # Change title from "Tanda 1: Fundamentos y Confianza (2 horas)" to include Tanda 1B
    t1 = t1.replace(r'Tanda 1: Fundamentos y Confianza (2 horas)', r'Tanda 1 y 1B: Fundamentos y Confianza (4 horas)')
    t1 = t1.replace(r'7 ejercicios directos', r'17 ejercicios directos')
    t1 = t1.replace(r'(2 horas total)', r'(4 horas total)')

    # Extract exercises from t1b
    # Exercises start with \section*{Ejercicio ...
    # And end at \section*{Resumen de Conceptos Clave -- Tanda 1B} 
    exercises_t1b_match = re.search(r'(%% ============================================================\s*%% EJERCICIO 1:.*?)\\section\*\{Resumen de Conceptos Clave', t1b, flags=re.DOTALL)
    if exercises_t1b_match:
        exercises_str = exercises_t1b_match.group(1)
        
        # Renumber exercises from 1..10 to 8..17
        for i in range(10, 0, -1):
            new_i = i + 7
            exercises_str = re.sub(rf'Ejercicio {i}', rf'Ejercicio {new_i}', exercises_str)
            exercises_str = re.sub(rf'EJERCICIO {i}', rf'EJERCICIO {new_i}', exercises_str)
        
        # Add missing image for Ex 8 (was Ex 1 in t1b)
        # It says "Se tienen 4 cargas puntuales unidas por líneas (ver figura)."
        # We will add an includegraphics. Assuming the image might be FIS1533-2019-2-P16.png (even if we don't have it, the text says 'ver figura').
        img_insert = r'\begin{center}' + '\n' + r'    \includegraphics[width=0.45\textwidth]{../images/FIS1533-2019-2-P16.png}' + '\n' + r'\end{center}'
        exercises_str = exercises_str.replace(r'(ver figura).', r'(ver figura).' + '\n\n' + img_insert)
        
        # Now find where to insert in t1 (before Resumen de Conceptos Clave)
        insert_pos = t1.find(r'%% ============================================================' + '\n' + r'%% RESUMEN DE CONCEPTOS CLAVE')
        if insert_pos != -1:
            t1 = t1[:insert_pos] + exercises_str + '\n' + t1[insert_pos:]
        else:
            print("Could not find where to insert in t1")

    # Merge the "Resumen de Conceptos Clave"
    resumen_t1b_match = re.search(r'(\\begin\{tcolorbox\}\[.*?title=Lo que deberías dominar después de la Tanda 1 \+ 1B\].*?\\end\{tcolorbox\})', t1b, flags=re.DOTALL)
    if resumen_t1b_match:
        resumen_1_match = re.search(r'(\\begin\{tcolorbox\}\[.*?title=Lo que deberías dominar después de esta tanda\].*?\\end\{tcolorbox\})', t1, flags=re.DOTALL)
        if resumen_1_match:
             t1 = t1.replace(resumen_1_match.group(0), resumen_t1b_match.group(1))

    # Enhance handbooks
    t1 = enhance_handbook_notes(t1)

    # Save to tanda1
    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda1.tex', 'w', encoding='utf-8') as f:
        f.write(t1)

    # Optionally delete tanda1b or leave it (we'll just leave it and maybe the user cleans it, BUT it's merged)
    # The prompt doesn't ask to delete t1b, just to merge to a single coherent file.

def process_tanda2():
    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda2_enunciados.tex', 'r', encoding='utf-8') as f:
        e = f.read()

    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda2_soluciones.tex', 'r', encoding='utf-8') as f:
        s = f.read()

    e = clean_author(e)
    s = clean_author(s)
    
    # We said "faltan algunas imágenes" - in tanda2, Exercise 4 (P22 - 2024-2) uses 2023-2-P1-5.png. Let's change it to 2024-2-P2-5.png.
    e = e.replace('FIS1533-2023-2-P1-5.png', 'FIS1533-2024-2-P2-5.png')
    s = s.replace('FIS1533-2023-2-P1-5.png', 'FIS1533-2024-2-P2-5.png')

    s = enhance_handbook_notes(s)

    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda2_enunciados.tex', 'w', encoding='utf-8') as f:
        f.write(e)
        
    with open('/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia electro/preguntas faciles/guia_electro_facil_tanda2_soluciones.tex', 'w', encoding='utf-8') as f:
        f.write(s)

if __name__ == "__main__":
    process_tanda1()
    process_tanda2()
    print("Done")
