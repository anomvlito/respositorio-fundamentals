---
name: gestionar-word
description: Gestiona archivos Microsoft Word (.docx). Permite leer contenido, detectar formato (negrita), y escribir o crear documentos nuevos. Úsese cuando el usuario quiera leer, analizar o crear archivos Word.
---

# Gestionar Word

## Cuándo usar esta skill
- El usuario pide "leer el archivo word".
- El usuario quiere saber qué partes del documento están en **negrita**.
- El usuario quiere crear un nuevo archivo `.docx` o agregar texto a uno existente.

## Flujo de trabajo
1.  **Verificar dependencia**: Asegúrate de que `python-docx` esté instalado.
    ```bash
    pip show python-docx || pip install python-docx
    ```
2.  **Ejecutar Script**: Utiliza el script `scripts/word_manager.py` para realizar la operación deseada.

## Instrucciones

### Leer Contenido
Para obtener el texto plano de un documento:
```bash
python3 .agent/skills/gestionar-word/scripts/word_manager.py read "/ruta/al/documento.docx"
```

### Inspeccionar Estructura (Negritas)
Para ver qué párrafos contienen texto en negrita:
```bash
python3 .agent/skills/gestionar-word/scripts/word_manager.py inspect "/ruta/al/documento.docx"
```

### Crear Nuevo Documento
Para crear un archivo nuevo:
```bash
python3 .agent/skills/gestionar-word/scripts/word_manager.py create "/ruta/al/nuevo_doc.docx" "Contenido inicial opcional"
```

### Escribir/Agregar a Documento
Para agregar un párrafo al final de un documento existente:
```bash
python3 .agent/skills/gestionar-word/scripts/word_manager.py write "/ruta/al/documento.docx" "Nuevo párrafo de texto"
```

## Recursos
- [word_manager.py](scripts/word_manager.py)
