import os
import re
import glob

tex_files = glob.glob('*.tex')
missing_images = []

for file in tex_files:
    if file == 'guia_electro_facil_tanda1b.tex':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and check images
    images = re.findall(r'\\includegraphics\[.*?\]\{(.*?)\}', content)
    for img_path in images:
        # resolve relative path
        full_path = os.path.normpath(os.path.join(os.path.dirname(file), img_path))
        if not os.path.exists(full_path):
            missing_images.append((file, img_path))

    # Remove instances of " (4 horas)", " (2 horas)", etc. from title
    content = re.sub(r' \(\d+ horas\)', '', content)
    content = re.sub(r' \(\d+ horas total\)', '', content)
    
    # Remove lines containing "Tiempo estimado:" or "Tiempo sugerido:"
    content = re.sub(r'\\textbf\{Tiempo estimado:\}.*\n?', '', content)
    content = re.sub(r'\\textbf\{Tiempo sugerido:\}.*\n?', '', content)
    
    # Just in case, general minute cleanup
    content = re.sub(r'.*?(\~)?\d+\s+minutos? por ejercicio.*?\n?', '', content)
    content = re.sub(r'.*?(\~)?\d+\s+min\/ejercicio.*?\n?', '', content)

    # Let's save it
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

if missing_images:
    for f, img in missing_images:
        print(f"MISSING: File {f} depends on {img}")
else:
    print("ALL IMAGES EXIST.")
