#!/usr/bin/env python3
"""
Refined extraction and merge of missing pages into handbook_map.json.
Reads each missing page from the PDF, extracts proper titles,
and produces rigorous JSON entries sorted by pdf_index.
"""
import json
import subprocess
import re
import os
import sys

PDF_PATH = "fe-handbook-10-1 - ECF.pdf"
PAGE_MAP_PATH = ".agent/skills/fe-handbook-ref/resources/page_mapping.json"
HANDBOOK_MAP_PATH = ".agent/skills/fe-handbook-ref/resources/handbook_map.json"
IMAGES_DIR = ".agent/skills/fe-handbook-ref/resources/images"

def extract_pdf_page(pdf_index):
    """Extract text from a single PDF page using pdftotext."""
    try:
        result = subprocess.run(
            ["pdftotext", "-f", str(pdf_index), "-l", str(pdf_index), "-layout", PDF_PATH, "-"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout
    except Exception as e:
        return ""

def extract_title_from_text(text, handbook_page):
    """
    Extract a meaningful title from the page text.
    FE Handbook pages typically have the section name in the right margin
    and specific topic headings at the top.
    """
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return f"Page {handbook_page}"
    
    # Known section names that appear in right margins
    sections = {
        "Mathematics": "Mathematics",
        "Engineering Probability and Statistics": "Engineering Probability & Statistics",
        "Engineering Probability": "Engineering Probability & Statistics",
        "Ethics and Professional Practice": "Ethics & Professional Practice",
        "Engineering Economics": "Engineering Economics",
        "Statics": "Statics",
        "Dynamics": "Dynamics",
        "Mechanics of Materials": "Mechanics of Materials",
        "Thermodynamics": "Thermodynamics",
        "Fluid Mechanics": "Fluid Mechanics",
        "Heat Transfer": "Heat Transfer",
        "Instrumentation, Measurement, and Control": "Instrumentation & Control",
        "Instrumentation": "Instrumentation & Control",
        "Electrical and Computer Engineering": "Electrical & Computer Engineering",
        "Chemistry and Biology": "Chemistry & Biology",
        "Materials Science": "Materials Science",
        "Materials Science/Structure of Matter": "Materials Science",
    }
    
    # Find section from right-margin text
    section = None
    for line in lines:
        for key, val in sections.items():
            if key.lower() in line.lower():
                section = val
                break
        if section:
            break
    
    if not section:
        section = f"Page {handbook_page}"
    
    # Find the first heading (usually UPPERCASE or a distinctive line)
    heading = None
    for line in lines[:15]:
        # Skip page numbers, copyright, section markers
        cleaned = line.strip()
        if not cleaned or len(cleaned) < 4:
            continue
        if cleaned.isdigit():
            continue
        if cleaned.startswith('©') or cleaned.startswith('NCEES'):
            continue
        # Skip lines that are just the section name
        if any(s.lower() == cleaned.lower() for s in sections.keys()):
            continue
        # Check for heading-like text (often has uppercase words)
        upper_words = sum(1 for w in cleaned.split() if w[0].isupper()) if cleaned.split() else 0
        if upper_words >= 1 and len(cleaned) > 5:
            heading = cleaned[:100]
            break
    
    if heading:
        # Clean up heading
        heading = re.sub(r'\s+', ' ', heading).strip()
        return f"{section} ({heading})" if section != f"Page {handbook_page}" else heading
    
    return section

def determine_content_type(text):
    """
    Analyze text to determine what type of content blocks to create.
    Returns a list of block descriptors.
    """
    lines = [l for l in text.split('\n') if l.strip()]
    
    # Detect if page is primarily a table/chart (heavy tabular data)
    tab_lines = sum(1 for l in lines if '\t' in l or l.count('  ') > 3)
    has_heavy_table = tab_lines > len(lines) * 0.3 if lines else False
    
    # Detect formula-heavy content
    formula_chars = set('=∫∑√±×÷∂∇αβγδεζηθλμνπρστφψω')
    formula_count = sum(1 for l in lines if any(c in l for c in formula_chars) or '=' in l)
    is_formula_heavy = formula_count > 3
    
    # Detect diagram references
    has_diagram = bool(re.search(r'(?i)(figure|fig\.|diagram|chart|graph|schematic)', text))
    
    return {
        'is_table': has_heavy_table,
        'is_formula_heavy': is_formula_heavy,
        'has_diagram': has_diagram,
        'line_count': len(lines)
    }

def build_entry(pdf_index, handbook_page, text):
    """Build a well-structured handbook_map entry."""
    title = extract_title_from_text(text, handbook_page)
    content_type = determine_content_type(text)
    
    entry = {
        "handbook_page": handbook_page,
        "pdf_index": pdf_index,
        "title": title,
        "blocks": []
    }
    
    # For table-heavy or diagram pages, add image block
    if content_type['is_table'] or content_type['has_diagram']:
        entry['blocks'].append({
            "type": "image",
            "heading": f"Content from Page {handbook_page}",
            "path": f".agent/skills/fe-handbook-ref/resources/images/p{handbook_page}_content.png",
            "caption": f"Full content from handbook page {handbook_page}."
        })
    
    # Extract meaningful text content (first substantive paragraph)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    meaningful = []
    for line in lines:
        if len(line) > 10 and not line.isdigit() and not line.startswith('©'):
            meaningful.append(line)
        if len(meaningful) >= 3:
            break
    
    if meaningful:
        summary = ' '.join(meaningful)[:400]
        entry['blocks'].append({
            "type": "text",
            "heading": "Page Content",
            "content": summary
        })
    
    return entry

def main():
    # Load source files
    with open(PAGE_MAP_PATH) as f:
        page_map = json.load(f)
    
    with open(HANDBOOK_MAP_PATH) as f:
        data = json.load(f)
    
    existing = set(p['pdf_index'] for p in data['pages'])
    
    # Find missing pages
    missing = []
    for entry in page_map:
        idx = entry['pdf_index']
        hb = entry['handbook_page']
        if entry['type'] == 'arabic' and isinstance(hb, int) and hb > 0:
            if idx not in existing:
                missing.append({'pdf_index': idx, 'handbook_page': hb})
    
    missing.sort(key=lambda x: x['pdf_index'])
    
    if not missing:
        print("No missing pages found!")
        return
    
    print(f"Extracting and merging {len(missing)} missing pages...")
    
    new_entries = []
    for i, m in enumerate(missing):
        text = extract_pdf_page(m['pdf_index'])
        entry = build_entry(m['pdf_index'], m['handbook_page'], text)
        new_entries.append(entry)
        
        status = "📊" if entry['blocks'] and entry['blocks'][0].get('type') == 'image' else "📝"
        print(f"  {status} [{i+1}/{len(missing)}] PDF {m['pdf_index']:>3} → HB {m['handbook_page']:>3}: {entry['title'][:65]}")
    
    # Merge into existing data
    data['pages'].extend(new_entries)
    
    # Sort all pages by pdf_index
    data['pages'].sort(key=lambda p: p['pdf_index'])
    
    # Verify no duplicates
    from collections import Counter
    indices = [p['pdf_index'] for p in data['pages']]
    dupes = [idx for idx, count in Counter(indices).items() if count > 1]
    if dupes:
        print(f"\n⚠️  WARNING: Duplicate pdf_indices found: {dupes}")
        print("NOT saving to avoid corruption.")
        return
    
    # Save
    with open(HANDBOOK_MAP_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    
    print(f"\n✅ Successfully merged {len(new_entries)} pages into handbook_map.json")
    print(f"   Total pages now: {len(data['pages'])}")
    print(f"   File: {HANDBOOK_MAP_PATH}")

if __name__ == "__main__":
    main()
