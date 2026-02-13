import json
import os

JSON_PATH = "resources/handbook_map.json"

def update_batch_1():
    print(f"Updating {JSON_PATH} for Batch 1 (Pages 2-10)...")
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    # Handle structure
    if isinstance(data, list):
        pages_list = data
    elif isinstance(data, dict) and 'pages' in data:
        pages_list = data['pages']
    else:
        print("Invalid JSON structure")
        return

    # Pages to process
    # 2, 3: Exist -> Add image block
    # 4-10: Missing -> Create new page entry

    # Create a lookup for existing pages
    page_map = {p['handbook_page']: p for p in pages_list if 'handbook_page' in p}

    # Pages 2 and 3
    for p_num in [2, 3]:
        if p_num in page_map:
            page = page_map[p_num]
            # Check if image already exists
            has_image = any(b.get('type') == 'image' and f"p{p_num}_content.png" in b.get('path', '') for b in page.get('blocks', []))
            if not has_image:
                print(f"Adding image to Page {p_num}...")
                new_block = {
                    "type": "image",
                    "heading": f"Content from Page {p_num}",
                    "path": f".agent/skills/fe-handbook-ref/resources/images/p{p_num}_content.png",
                    "caption": f"Full content from handbook page {p_num}."
                }
                if 'blocks' not in page:
                    page['blocks'] = []
                # Add to top
                page['blocks'].insert(0, new_block)

    # Pages 4-10
    for p_num in range(4, 11):
        if p_num not in page_map:
            print(f"Creating new entry for Page {p_num}...")
            # Titles are likely "Units..." or "Mathematics".
            # Page 1-3 are "Units and Conversion Factors".
            # Page 34 is "Mathematics".
            # We will use "Extracted Page" as a placeholder title or "Units/Math"
            # Given the gap, it's safer to use a generic title that helps identify it.
            
            new_page = {
                "handbook_page": p_num,
                "pdf_index": p_num + 6,
                "title": f"Handbook Page {p_num} (Title TBD)",
                "blocks": [
                    {
                        "type": "image",
                        "heading": f"Content from Page {p_num}",
                        "path": f".agent/skills/fe-handbook-ref/resources/images/p{p_num}_content.png",
                        "caption": f"Full content from handbook page {p_num}."
                    }
                ]
            }
            pages_list.append(new_page)
        else:
            print(f"Page {p_num} already exists (unexpected). Checking image...")
            # If it somehow exists (e.g. out of order), add image if missing
            page = page_map[p_num]
            has_image = any(b.get('type') == 'image' and f"p{p_num}_content.png" in b.get('path', '') for b in page.get('blocks', []))
            if not has_image:
                 print(f"Adding image to existing Page {p_num}...")
                 new_block = {
                    "type": "image",
                    "heading": f"Content from Page {p_num}",
                    "path": f".agent/skills/fe-handbook-ref/resources/images/p{p_num}_content.png",
                    "caption": f"Full content from handbook page {p_num}."
                }
                 if 'blocks' not in page:
                    page['blocks'] = []
                 page['blocks'].insert(0, new_block)

    # Sort
    pages_list.sort(key=lambda x: x.get('handbook_page', 0))

    # Save
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Batch 1 Update Complete.")

if __name__ == "__main__":
    update_batch_1()
