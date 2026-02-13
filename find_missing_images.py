import json
import os
import glob
import re

# File paths
HANDBOOK_MAP_PATH = ".agent/skills/fe-handbook-ref/resources/handbook_map.json"
REPO_ROOT = "."

def main():
    print(f"Checking for images in {os.path.abspath(REPO_ROOT)}...")
    
    # 1. Load handbook_map.json
    try:
        with open(HANDBOOK_MAP_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {HANDBOOK_MAP_PATH}")
        return

    # 2. Extract PDF indices that have images in the JSON
    json_image_pdf_indices = set()
    
    for page in data.get("pages", []):
        pdf_index = page.get("pdf_index")
        
        # Check blocks
        blocks = page.get("blocks", [])
        for block in blocks:
            if block.get("type") == "image":
                if pdf_index:
                    json_image_pdf_indices.add(pdf_index)

    print(f"Found {len(json_image_pdf_indices)} PDF indices with images defined in handbook_map.json")

    # 3. Find images on disk
    # Pattern: math_final_check-XXX.png
    print(f"Searching recursively for 'math_final_check-*.png' in {REPO_ROOT}...")
    image_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for file in files:
            if file.startswith("math_final_check-") and file.endswith(".png"):
                image_files.append(os.path.join(root, file))
    
    disk_pdf_indices = set()
    
    print(f"Found {len(image_files)} 'math_final_check-*.png' files in {REPO_ROOT}")

    for img_path in image_files:
        filename = os.path.basename(img_path)
        # Extract number
        match = re.search(r"math_final_check-(\d+)\.png", filename)
        if match:
            idx = int(match.group(1))
            disk_pdf_indices.add(idx)

    # 4. Compare
    missing_in_json = disk_pdf_indices - json_image_pdf_indices
    
    print("\n--- Discrepancy Report ---")
    
    if not missing_in_json:
        print("All images on disk are accounted for in handbook_map.json!")
    else:
        print(f"Found {len(missing_in_json)} images on disk that are NOT in handbook_map.json:")
        sorted_missing = sorted(list(missing_in_json))
        print(sorted_missing)

        # Generate JSON content
        print("\n--- Suggestion: Add these blocks to handbook_map.json ---")
        for pdf_idx in sorted_missing:
            # We don't verify handbook page here easily without page_mapping.json logic, 
            # but we can print the block.
            print(f"\n// For PDF Index {pdf_idx}")
            block = {
                "type": "image",
                "heading": f"Diagram from PDF Index {pdf_idx}",
                "path": f"math_final_check-{pdf_idx}.png",
                "caption": "TODO: Describe this image"
            }
            print(json.dumps(block, indent=2))
            
if __name__ == "__main__":
    main()
