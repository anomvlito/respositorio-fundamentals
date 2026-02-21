import json
import re

file_path = '/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia matematicas/ejercicios_matematicas.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pattern = re.compile(r'Respuesta Correcta:\s*([^}]+)')

for item in data:
    sol_text = item.get("solucion", "")
    match = pattern.search(sol_text)
    if match:
        item["respuesta correcta"] = match.group(1).strip()
    else:
        item["respuesta correcta"] = "No Encontrada"

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Atributo 'respuesta correcta' agregado a todos los elementos correctamente.")
