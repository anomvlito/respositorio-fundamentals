import json
import os
import subprocess
import sys

# Configuration
PDF_PATH = "/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
IMAGES_DIR = "resources/images"
JSON_PATH = "resources/handbook_map.json"
OFFSET = 6  # PDF Index = Handbook Page + 6

def run_command(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}\n{e.stderr.decode()}")
        raise

def process_batch(start_page, end_page):
    print(f"Processing Batch: Pages {start_page} to {end_page}")
    
    # 1. Extraction
    pdf_start = start_page + OFFSET
    pdf_end = end_page + OFFSET
    
    print(f"  - Extracting PDF pages {pdf_start}-{pdf_end}...")
    # pdftoppm uses 1-based indexing for pages
    cmd_extract = f"pdftoppm -f {pdf_start} -l {pdf_end} -png \"{PDF_PATH}\" \"{IMAGES_DIR}/extract_temp\""
    run_command(cmd_extract)
    
    # 2. Renaming
    print("  - Renaming files...")
    # pdftoppm generates extract_temp-001.png etc. relative to the START of the extraction?
    # NO: pdftoppm numbers files based on the PAGE NUMBER if using -png? 
    # Actually, pdftoppm usually outputs prefix-digits.png. 
    # If we extract pages 67-76 (handbook 61-70), it might output extract_temp-067.png OR extract_temp-1.png?
    # Default behavior: uses PDF page number if not single page? Let's check previous output behavior.
    # Previous script: pdftoppm -f 8 -l 16 ... produced extract-08.png, extract-09.png.
    # So it uses the PDF page number with padding.
    
    # Pad width likely 3 digits (008, 067, 120).
    
    for h_page in range(start_page, end_page + 1):
        pdf_idx = h_page + OFFSET
        # Construct expected source filename (e.g., extract_temp-067.png)
        # padding varies? previous output showed extract-008.png (3 digits).
        # Let's try 3 digits formatting.
        src_filename = f"extract_temp-{pdf_idx:03d}.png"
        src_path = os.path.join(IMAGES_DIR, src_filename)
        
        # Target
        dest_filename = f"p{h_page}_content.png"
        dest_path = os.path.join(IMAGES_DIR, dest_filename)
        
        if os.path.exists(src_path):
            os.rename(src_path, dest_path)
            # print(f"    Renamed {src_filename} -> {dest_filename}")
        else:
            # Fallback: maybe 2 digits if < 100? or more? 
            # pdftoppm naming can be tricky.
            # Let's try globbing if specific file not found?
            # Or just try various paddings.
            src_filename_2 = f"extract_temp-{pdf_idx:02d}.png" # Unlikely if 008 was used
            src_path_2 = os.path.join(IMAGES_DIR, src_filename_2)
            if os.path.exists(src_path_2):
                os.rename(src_path_2, dest_path)
            else:
                 # Check for 4 digits?
                src_filename_4 = f"extract_temp-{pdf_idx:04d}.png"
                src_path_4 = os.path.join(IMAGES_DIR, src_filename_4)
                if os.path.exists(src_path_4):
                     os.rename(src_path_4, dest_path)
                else:
                    print(f"    WARNING: Source image for Handbook Page {h_page} (PDF {pdf_idx}) not found. Expected {src_filename}")

    # clean up any logic artifacts if needed
    
    # 3. Update JSON
    print("  - Updating JSON map...")
    update_json_map(start_page, end_page)
    print("  Batch Complete.\n")

def update_json_map(start_page, end_page):
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    if isinstance(data, list):
        pages_list = data
    elif isinstance(data, dict) and 'pages' in data:
        pages_list = data['pages']
    else:
        print("Invalid JSON structure")
        return

    page_map = {p['handbook_page']: p for p in pages_list if 'handbook_page' in p}
    
    pages_modified = False

    for p_num in range(start_page, end_page + 1):
        image_filename = f"p{p_num}_content.png"
        image_path_rel = f".agent/skills/fe-handbook-ref/resources/images/{image_filename}"
        
        # Verify file exists now
        if not os.path.exists(os.path.join(IMAGES_DIR, image_filename)):
            print(f"    Warning: Image {image_filename} missing, skipping JSON update for this page.")
            continue

        if p_num in page_map:
            # Page exists, check/add image
            page = page_map[p_num]
            has_image = any(b.get('type') == 'image' and image_filename in b.get('path', '') for b in page.get('blocks', []))
            if not has_image:
                 new_block = {
                    "type": "image",
                    "heading": f"Content from Page {p_num}",
                    "path": image_path_rel,
                    "caption": f"Full content from handbook page {p_num}."
                }
                 if 'blocks' not in page:
                    page['blocks'] = []
                 page['blocks'].insert(0, new_block)
                 pages_modified = True
                 # print(f"    Updated Page {p_num}")
        else:
            # Create new page
            # print(f"    Creating Page {p_num}")
            new_page = {
                "handbook_page": p_num,
                "pdf_index": p_num + OFFSET,
                "title": f"Handbook Page {p_num}",
                "blocks": [
                    {
                        "type": "image",
                        "heading": f"Content from Page {p_num}",
                        "path": image_path_rel,
                        "caption": f"Full content from handbook page {p_num}."
                    }
                ]
            }
            pages_list.append(new_page)
            pages_modified = True

    if pages_modified:
        pages_list.sort(key=lambda x: x.get('handbook_page', 0))
        with open(JSON_PATH, 'w') as f:
            json.dump(data, f, indent=2)
        print("    JSON saved.")
    else:
        print("    No JSON changes needed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 process_batch.py <start_page> <end_page>")
        sys.exit(1)
    
    s = int(sys.argv[1])
    e = int(sys.argv[2])
    process_batch(s, e)
