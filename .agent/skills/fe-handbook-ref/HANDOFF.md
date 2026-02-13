# FE Handbook Skill — Handoff Document (Context Transfer)

> **Fecha:** 2026-02-13
> **Propósito:** Documento de transferencia de contexto para continuar el trabajo en una nueva ventana de conversación.

---

## 1. Objetivo General del Proyecto

Enriquecer sistemáticamente la skill `fe-handbook-ref` para que funcione como un **sistema de búsqueda y referencia completo** del NCEES FE Reference Handbook v10.1. La skill debe ser capaz de:

1. **Encontrar** cualquier fórmula/concepto por palabra clave (búsqueda en texto).
2. **Mostrar** la página exacta del handbook como imagen (fuente visual de verdad).
3. **Citar** la página correcta del handbook impreso en documentos LaTeX.

---

## 2. Arquitectura del Sistema

```
.agent/skills/fe-handbook-ref/
├── SKILL.md                    # Instrucciones para el Agente (cómo usar la skill)
├── HANDOFF.md                  # Este documento
├── resources/
│   ├── handbook_map.json       # BASE DE DATOS CENTRAL (8,265 líneas, ~1.2 MB)
│   └── images/                 # 411 archivos PNG (imágenes extraídas del PDF)
│       ├── p1_content.png      # Imagen de la página 1 del handbook
│       ├── p2_content.png      # ...
│       └── p269_content.png    # Última página mapeada
├── scripts/                    # Scripts de consulta
├── process_batch.py            # Script unificado de extracción por lotes
├── extract_text_full.py        # Script de extracción de texto completo
├── map_sections.py             # Genera tabla de secciones desde el JSON
└── [otros scripts auxiliares]  # extract_batch_*.sh, update_json_batch_*.py, etc.
```

### Fuente PDF
- **Archivo:** `fe-handbook-10-1 - ECF.pdf`
- **Ubicación:** `/home/fabian/src/fundamentals/respositorio-fundamentals/`
- **Total páginas PDF:** 275
- **Contenido útil:** Páginas 1 a 269 del handbook (impresas)

### Calibración de Páginas (CRÍTICO)
```
PDF_index = Handbook_page + 6
```
- La página **1** del handbook impreso está en la página **7** del PDF.
- La página **269** del handbook está en la página **275** del PDF.
- Las primeras 6 páginas del PDF son portada/índice (no mapeadas).

---

## 3. Estado Actual de `handbook_map.json`

### Estructura de cada entrada:
```json
{
  "handbook_page": 47,
  "pdf_index": 53,
  "title": "Mathematics (L'Hôpital's Rule / Integral Calculus)",
  "blocks": [
    {
      "type": "image",
      "heading": "Content from Page 47",
      "path": ".agent/skills/fe-handbook-ref/resources/images/p47_content.png",
      "caption": "Full content from handbook page 47."
    },
    {
      "type": "formulas",
      "heading": "...",
      "latex": "..."
    }
  ],
  "content_raw": "Mathematics\n\nL'Hospital's Rule...\n..."
}
```

### Campos clave:
| Campo | Descripción | Estado |
|-------|-------------|--------|
| `handbook_page` | Número de página impresa | ✅ Completo (1-269) |
| `pdf_index` | Índice real en el PDF | ✅ Completo |
| `title` | Título descriptivo de la página | ⚠️ **PARCIAL** — Págs 1-3 tienen buen título; Págs 4-10 decían "TBD" (Pág 4 ya corregida a "Mathematics (Discrete Math)"); Págs 5-269 dicen "Handbook Page X" |
| `blocks[image]` | Imagen PNG de la página | ✅ Completo (269 imágenes `pX_content.png`) |
| `blocks[formulas/text/table]` | Contenido LaTeX manual | ⚠️ Solo Págs 1-3 tienen bloques detallados de LaTeX; resto solo tiene imagen |
| `content_raw` | Texto extraído del PDF (`pdftotext`) | ✅ Completo — Inyectado para todas las 269 páginas |

### Problema de Duplicados (Página 1):
La página 1 aparece **DOS VECES** en el JSON:
1. Primera entrada (líneas 9-98): `pdf_index: 2`, con bloques detallados de LaTeX (entrada original manual).
2. Segunda entrada (líneas 101-118): `pdf_index: 7`, con imagen + `content_raw` (entrada generada por script).

> El `pdf_index: 2` de la primera es **incorrecto** (debería ser 7). Esta es una entrada legacy que necesita limpieza.

### Página 34 — Entrada duplicada:
La página 34 también tiene una entrada duplicada (líneas 587-600) con `pdf_index: 10` que es incorrecto (debería ser 40). Esta es otra entrada legacy del mapeo inicial de Discrete Math.

---

## 4. Trabajo Completado

### Fase 1: Enriquecimiento de Módulos LaTeX
- [x] Módulo 1: Análisis, cheatsheet, referencias FE en archivos `.tex`
- [x] Módulo 2: Análisis, cheatsheet, referencias FE en archivos `.tex`
- [x] Macro `\fehandbook{página}{sección}` definida en ambos módulos

### Fase 2: Extracción de Imágenes (27 lotes)
- [x] Extracción de imágenes PNG para páginas 1-269
- [x] 411 archivos PNG en `resources/images/`
- [x] Cada página mapeada en `handbook_map.json` con bloque `type: "image"`
- [x] Herramienta: `pdftoppm` + `process_batch.py`

### Fase 3: Extracción de Texto (`content_raw`)
- [x] Texto completo extraído para páginas 1-269
- [x] Campo `content_raw` inyectado en cada entrada del JSON
- [x] Herramienta: `pdftotext -layout` + `extract_text_full.py`

### Fase 4: Documentación
- [x] `SKILL.md` actualizado con tabla de secciones y mejores prácticas
- [x] Tabla de organización del handbook completa

---

## 5. Trabajo Pendiente (PRÓXIMA SESIÓN)

### 5.1 Corrección de Títulos en `handbook_map.json` (PRIORIDAD ALTA)
**Problema:** La mayoría de las páginas (5-269) tienen títulos genéricos como `"Handbook Page X"`.
**Solución:** Leer el `content_raw` de cada página y asignar un título descriptivo basado en el contenido real.

**Progreso:**
- [x] Página 4: Corregida a "Mathematics (Discrete Math)"
- [ ] Páginas 5-269: Pendientes (ir de 10 en 10, verificando manualmente)

**Instrucciones para el Agente:**
1. Leer `handbook_map.json` en bloques de ~300 líneas.
2. Para cada página con título genérico, leer el campo `content_raw`.
3. Extraer el título real (primera línea significativa del texto, ej: "Mathematics", "Thermodynamics").
4. Asignar un título descriptivo como: `"Mathematics (Trigonometric Identities)"` o `"Fluid Mechanics (Bernoulli Equation)"`.
5. NO usar scripts Python. El agente debe hacer la verificación manual.

### 5.2 Limpieza de Entradas Duplicadas
- [ ] Eliminar la entrada duplicada de Página 1 (la que tiene `pdf_index: 2`)
- [ ] Eliminar la entrada duplicada de Página 34 (la que tiene `pdf_index: 10`)

### 5.3 Actualización de `SKILL.md`
- [ ] Añadir instrucciones de búsqueda por `content_raw` (grep/búsqueda de texto)
- [ ] Documentar el flujo completo: Búsqueda → Localización → Imagen → Cita LaTeX
- [ ] Asegurar que la skill cubra TODOS los casos de uso del Fundamentals

### 5.4 Módulo 3 (Futuro)
- [ ] Analizar estructura de Módulo 3
- [ ] Enriquecer con referencias FE
- [ ] Crear cheatsheet

---

## 6. Tabla de Secciones del Handbook

| Sección | Páginas Handbook | Páginas PDF |
|---------|-----------------|-------------|
| **Units & Conversion Factors** | 1-3 | 7-9 |
| *(Gap / Ethics / Safety)* | 4-33 | 10-39 |
| **Mathematics** | 34-62 | 40-68 |
| **Probability & Statistics** | 63-84 | 69-90 |
| **Chemistry & Biology** | 85-93 | 91-99 |
| **Materials Science** | 94-106 | 100-112 |
| **Statics** | 107-113 | 113-119 |
| **Dynamics** | 114-129 | 120-135 |
| **Mechanics of Materials** | 130-142 | 136-148 |
| **Thermodynamics** | 143-176 | 149-182 |
| **Fluid Mechanics** | 177-203 | 183-209 |
| **Heat Transfer** | 204-219 | 210-225 |
| **Instrumentation & Controls** | 220-229 | 226-235 |
| **Engineering Economics** | 230-237 | 236-243 |
| **Chemical / Civil / Electrical / Computer** | 238-269 | 244-275 |

---

## 7. Comandos Útiles

### Buscar un concepto en el JSON:
```bash
cd /home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref
grep -i "bernoulli" resources/handbook_map.json | head -5
```

### Extraer imagen de una página específica:
```bash
pdftoppm -f 53 -l 53 -png "/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf" "resources/images/temp"
# Renombrar: mv resources/images/temp-053.png resources/images/p47_content.png
```

### Extraer texto de una página:
```bash
pdftotext -f 53 -l 53 -layout "/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf" -
```

### Ejecutar lote de extracción:
```bash
python3 process_batch.py 101 110  # Extrae e inyecta páginas 101-110
```

---

## 8. Archivos Clave (Rutas Absolutas)

| Archivo | Ruta |
|---------|------|
| **PDF fuente** | `/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf` |
| **JSON central** | `/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/resources/handbook_map.json` |
| **SKILL.md** | `/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/SKILL.md` |
| **Imágenes** | `/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/resources/images/` |
| **Script lotes** | `/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/process_batch.py` |
| **Script texto** | `/home/fabian/src/fundamentals/respositorio-fundamentals/.agent/skills/fe-handbook-ref/extract_text_full.py` |

---

## 9. Decisiones de Diseño Importantes

1. **Texto (`content_raw`) es para BUSCAR, Imagen (`pX_content.png`) es para MOSTRAR.** El texto extraído por `pdftotext` es feo/corrupto para fórmulas, pero perfecto para `grep`. Las imágenes son la fuente de verdad visual.

2. **El `pdf_index` es la clave primaria de integridad.** Tanto la imagen como el texto se extraen del mismo índice PDF, haciendo imposible un desajuste.

3. **No se usan scripts de comparación automática.** El usuario prefiere que el agente haga verificación manual, lote por lote (10 páginas a la vez).

4. **Los bloques LaTeX detallados solo existen para las páginas 1-3.** El resto de páginas dependen de `content_raw` + imagen. No se ha completado el mapeo LaTeX detallado para el resto del handbook.

5. **Las páginas 4-33 no son un "gap" real.** Contienen contenido de Mathematics (Discrete Math, Algebra, Trigonometry, etc.). El título "gap" en la tabla de secciones del SKILL.md es una simplificación.
