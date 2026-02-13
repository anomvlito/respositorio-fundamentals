import json
import os
import re

HANDBOOK_MAP = "resources/handbook_map.json"
IMAGES_DIR = "resources/images"

def audit_images():
    print(f"Auditing {HANDBOOK_MAP} against {IMAGES_DIR}...")
    
    # 1. Load JSON
    try:
        with open(HANDBOOK_MAP, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: handbook_map.json not found.")
        return

    # 2. Get list of actual image files
    try:
        actual_files = set(os.listdir(IMAGES_DIR))
    except FileNotFoundError:
        print("Error: images directory not found.")
        return

    # 3. Analyze JSON entities
    pages_with_images = []
    pages_without_images = []
    referenced_images = set()

    # Sort data by handbook_page just in case
    if isinstance(data, dict):
        if 'pages' in data:
             data = data['pages']
        else:
             # Try to find a list value
             for k, v in data.items():
                 if isinstance(v, list):
                     data = v
                     break
    
    if not isinstance(data, list):
        print("Error: JSON root is not a list and could not find a list property.")
        return

    data.sort(key=lambda x: x.get('handbook_page', 0))

    for entry in data:
        page_num = entry.get('handbook_page')
        title = entry.get('title', 'Unknown')
        blocks = entry.get('blocks', [])
        
        has_image = False
        page_images = []

        for block in blocks:
            if block.get('type') == 'image':
                has_image = True
                path = block.get('path')
                if path:
                    # Clean path to get basename
                    basename = os.path.basename(path)
                    referenced_images.add(basename)
                    page_images.append(basename)
        
        if has_image:
            # Check if all referenced images exist
            missing_refs = [img for img in page_images if img not in actual_files]
            if missing_refs:
                 print(f"Page {page_num} ({title}) references missing images: {missing_refs}")
            pages_with_images.append(page_num)
        else:
            pages_without_images.append({'page': page_num, 'title': title})

    # 4. Analyze specific gaps (like 121)
    print("\n--- Pages WITHOUT an 'image' block in JSON ---")
    for p in pages_without_images:
        print(f"Page {p['page']}: {p['title']}")

    # 5. Check for images in directory that are NOT referenced in JSON (Orphans)
    orphaned_images = []
    for f in actual_files:
        if f.endswith('.png') or f.endswith('.jpg'):
            if f not in referenced_images:
                orphaned_images.append(f)
    
    # Filter orphans that look like pXXX_content.png (might be unmapped)
    potential_page_content_orphans = [f for f in orphaned_images if re.match(r'p\d+_content\.png', f)]

    print("\n--- Orphaned Images (Exist in dir, not in JSON) ---")
    if orphaned_images:
        for f in sorted(orphaned_images):
            print(f)
    else:
        print("None.")

    print("\n--- Missing Sequence Analysis (pXXX_content.png) ---")
    # Heuristic: Check for gaps in pXXX_content.png sequence for existing pages
    # If Page X exists in JSON, does pX_content.png exist?
    
    missing_content_files = []
    for entry in data:
        page_num = entry.get('handbook_page')
        expected_filename = f"p{page_num}_content.png"
        
        if expected_filename not in actual_files:
             # It's missing from disk. Is it referenced?
             # We already checked references. This is checking if the "standard" screenshot exists.
             missing_content_files.append({'page': page_num, 'file': expected_filename, 'has_image_block': page_num in pages_with_images})

    # Display meaningful gaps (e.g. page exists, no image block, and pXXX_content.png missing)
    print("Pages that represent a gap (JSON exists, no standard 'pXXX_content.png' found):")
    for item in missing_content_files:
        status = "Has other images" if item['has_image_block'] else "NO IMAGES referenced"
        print(f"Page {item['page']}: Missing {item['file']} ({status})")

if __name__ == "__main__":
    audit_images()
