import json
import os
import subprocess

# Configuration
PDF_PATH = "/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
JSON_PATH = "resources/handbook_map.json"
OFFSET = 6  # PDF Index = Handbook Page + 6

def run_pdftotext(pdf_page_index):
    try:
        # Extract text from a single page using -layout to preserve some structure
        cmd = ["pdftotext", "-f", str(pdf_page_index), "-l", str(pdf_page_index), "-layout", PDF_PATH, "-"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting text from page {pdf_page_index}: {e}")
        return ""

def enrich_json_with_text():
    print(f"Loading {JSON_PATH}...")
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    pages_list = data.get('pages', [])
    page_map = {p['handbook_page']: p for p in pages_list if 'handbook_page' in p}
    
    # We know the PDF has 275 pages.
    # We have mapped pages 1 to 269 (roughly 275-6).
    
    print("Starting text extraction and enrichment...")
    
    for p_num in range(1, 270): # 1 to 269
        if p_num not in page_map:
            continue
            
        page = page_map[p_num]
        pdf_idx = page.get('pdf_index')
        
        if not pdf_idx:
            # Fallback calculation if missing
            pdf_idx = p_num + OFFSET
        
        print(f"Processing Page {p_num} (PDF {pdf_idx})...", end='\r')
        
        raw_text = run_pdftotext(pdf_idx)
        
        # Clean up text slightly (remove excessive whitespace maybe, but layout is good)
        # We'll just strip start/end
        cleaned_text = raw_text.strip()
        
        # Inject into JSON
        page['content_raw'] = cleaned_text
        
        # Optional: Add a text block if it doesn't exist AND the page isn't just an image placeholder
        # For now, 'content_raw' is sufficient for the "Search" capability.
        
    print(f"\nSaving updated JSON to {JSON_PATH}...")
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Full-Text Enrichment Complete.")

if __name__ == "__main__":
    enrich_json_with_text()
