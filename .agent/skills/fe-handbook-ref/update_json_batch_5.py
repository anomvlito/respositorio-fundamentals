import json
import os

JSON_PATH = "resources/handbook_map.json"

def update_batch_5():
    print(f"Updating {JSON_PATH} for Batch 5 (Pages 41-50)...")
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

    page_map = {p['handbook_page']: p for p in pages_list if 'handbook_page' in p}

    for p_num in range(41, 51):
        image_path = f".agent/skills/fe-handbook-ref/resources/images/p{p_num}_content.png"
        
        if p_num in page_map:
            print(f"Page {p_num} exists. Adding image...")
            page = page_map[p_num]
            has_image = any(b.get('type') == 'image' and f"p{p_num}_content.png" in b.get('path', '') for b in page.get('blocks', []))
            if not has_image:
                 new_block = {
                    "type": "image",
                    "heading": f"Content from Page {p_num}",
                    "path": image_path,
                    "caption": f"Full content from handbook page {p_num}."
                }
                 if 'blocks' not in page:
                    page['blocks'] = []
                 page['blocks'].insert(0, new_block)
        else:
            print(f"Creating new entry for Page {p_num}...")
            new_page = {
                "handbook_page": p_num,
                "pdf_index": p_num + 6,
                "title": f"Handbook Page {p_num}",
                "blocks": [
                    {
                        "type": "image",
                        "heading": f"Content from Page {p_num}",
                        "path": image_path,
                        "caption": f"Full content from handbook page {p_num}."
                    }
                ]
            }
            pages_list.append(new_page)

    pages_list.sort(key=lambda x: x.get('handbook_page', 0))

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Batch 5 Update Complete.")

if __name__ == "__main__":
    update_batch_5()
