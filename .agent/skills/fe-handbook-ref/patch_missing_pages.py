import json
import os

JSON_PATH = "resources/handbook_map.json"

NEW_PAGES = [
    {
        "handbook_page": 112,
        "pdf_index": 88,
        "title": "Statics (Area Properties)",
        "blocks": [
            {
                "type": "image",
                "heading": "Area Moments of Inertia (Continued)",
                "path": ".agent/skills/fe-handbook-ref/resources/images/p112_area_properties_2.png",
                "caption": "Formulas for areas and centroids (Part 2)."
            }
        ]
    },
    {
        "handbook_page": 113,
        "pdf_index": 89,
        "title": "Statics (Area Properties)",
        "blocks": [
            {
                "type": "image",
                "heading": "Area Moments of Inertia (Continued)",
                "path": ".agent/skills/fe-handbook-ref/resources/images/p113_area_properties_3.png",
                "caption": "Formulas for areas and centroids (Part 3)."
            }
        ]
    }
]

def patch_missing_pages():
    print(f"Patching {JSON_PATH}...")
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

    # Check if they already exist - handle potential list vs dict item
    existing_ids = set()
    for p in pages_list:
        if isinstance(p, dict):
             existing_ids.add(p.get('handbook_page'))
    
    for new_page in NEW_PAGES:
        p_num = new_page['handbook_page']
        if p_num in existing_ids:
            print(f"Page {p_num} already exists. Skipping.")
        else:
            print(f"Adding Page {p_num}...")
            pages_list.append(new_page)
    
    # Sort the list by handbook_page to maintain order
    # Filter out non-dict items if any garbage exists
    pages_list.sort(key=lambda x: x.get('handbook_page', 0) if isinstance(x, dict) else 0)

    # Save
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Patch complete.")

if __name__ == "__main__":
    patch_missing_pages()
