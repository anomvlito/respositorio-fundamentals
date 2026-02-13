#!/usr/bin/env python3
"""
Extract text from missing PDF pages and generate handbook_map.json entries.
Uses page_mapping.json as ground truth and pdftotext for content extraction.
"""
import json
import subprocess
import re
import os

PDF_PATH = "fe-handbook-10-1 - ECF.pdf"
PAGE_MAP_PATH = ".agent/skills/fe-handbook-ref/resources/page_mapping.json"
HANDBOOK_MAP_PATH = ".agent/skills/fe-handbook-ref/resources/handbook_map.json"
IMAGES_DIR = ".agent/skills/fe-handbook-ref/resources/images"

def extract_pdf_page(pdf_index):
    """Extract text from a single PDF page."""
    try:
        result = subprocess.run(
            ["pdftotext", "-f", str(pdf_index), "-l", str(pdf_index), "-layout", PDF_PATH, "-"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[ERROR: {e}]"

def guess_section_title(text, handbook_page):
    """Try to extract a section title from the page text."""
    # Common section headers appear at edges of pages
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Check for section markers in the right margin
    section_keywords = [
        "Mathematics", "Engineering Probability", "Statistics",
        "Ethics", "Engineering Economics", "Statics",
        "Dynamics", "Mechanics of Materials", "Thermodynamics",
        "Fluid Mechanics", "Heat Transfer", "Instrumentation",
        "Electrical", "Computer", "Chemistry", "Biology",
        "Materials Science", "Civil Engineering", "Environmental",
        "Industrial", "Mechanical"
    ]
    
    section = "Unknown Section"
    for line in lines:
        for kw in section_keywords:
            if kw.lower() in line.lower():
                section = line.strip()
                break
    
    # Try to find the first meaningful heading
    title = None
    for line in lines[:10]:
        # Skip page numbers and short lines
        if len(line) > 5 and not line.isdigit() and not line.startswith('©'):
            if any(c.isalpha() for c in line):
                title = line[:80]
                break
    
    return title or f"Page {handbook_page} Content"

def classify_page_content(text):
    """Classify whether page has tables, formulas, diagrams, or text."""
    has_table = bool(re.search(r'\t{2,}|\s{4,}\d', text))
    has_formulas = bool(re.search(r'[=∫∑√±×÷∂∇αβγδεζηθλμνπρστφψω]', text))
    has_figure_ref = bool(re.search(r'(?i)(figure|fig\.|diagram|chart|graph)', text))
    
    return {
        'has_table': has_table,
        'has_formulas': has_formulas,
        'has_figure_ref': has_figure_ref,
        'line_count': len(text.split('\n'))
    }

def create_entry(pdf_index, handbook_page, text):
    """Create a handbook_map entry from extracted text."""
    title = guess_section_title(text, handbook_page)
    classification = classify_page_content(text)
    
    entry = {
        "handbook_page": handbook_page,
        "pdf_index": pdf_index,
        "title": title,
        "blocks": []
    }
    
    # For pages with heavy visual content (tables, diagrams), create image block
    if classification['has_figure_ref'] or classification['has_table']:
        entry['blocks'].append({
            "type": "image",
            "heading": f"Content from Handbook Page {handbook_page}",
            "path": f".agent/skills/fe-handbook-ref/resources/images/p{handbook_page}_content.png",
            "caption": f"Full page content from handbook page {handbook_page}."
        })
    
    # Extract any identifiable formulas as text blocks
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if lines:
        # Create a text block with a summary of content
        content_summary = ' '.join(lines[:5])[:300]
        entry['blocks'].append({
            "type": "text",
            "heading": "Page Content Summary",
            "content": content_summary
        })
    
    return entry

def main():
    # Load both JSON files
    with open(PAGE_MAP_PATH) as f:
        page_map = json.load(f)
    
    with open(HANDBOOK_MAP_PATH) as f:
        handbook = json.load(f)
    
    # Get existing pdf_indices
    existing = set(p['pdf_index'] for p in handbook['pages'])
    
    # Find missing pages
    missing = []
    for entry in page_map:
        idx = entry['pdf_index']
        hb = entry['handbook_page']
        if entry['type'] == 'arabic' and isinstance(hb, int) and hb > 0:
            if idx not in existing:
                missing.append({'pdf_index': idx, 'handbook_page': hb})
    
    missing.sort(key=lambda x: x['pdf_index'])
    
    print(f"Processing {len(missing)} missing pages...")
    print(f"Extracting text from PDF: {PDF_PATH}")
    print()
    
    new_entries = []
    for i, m in enumerate(missing):
        pdf_idx = m['pdf_index']
        hb_page = m['handbook_page']
        
        text = extract_pdf_page(pdf_idx)
        entry = create_entry(pdf_idx, hb_page, text)
        new_entries.append(entry)
        
        # Show progress
        print(f"  [{i+1}/{len(missing)}] PDF {pdf_idx:>3} -> HB {hb_page:>3}: {entry['title'][:60]}")
    
    # Save extracted data for review
    output_path = "missing_pages_extracted.json"
    with open(output_path, 'w') as f:
        json.dump(new_entries, f, indent=2, ensure_ascii=False)
        f.write('\n')
    
    print(f"\nSaved {len(new_entries)} entries to {output_path}")
    print("Review and then run: python3 merge_missing_pages.py")

if __name__ == "__main__":
    main()
