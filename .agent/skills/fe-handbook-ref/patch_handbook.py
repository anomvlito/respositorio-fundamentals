import json
import os

JSON_PATH = "resources/handbook_map.json"

# Orphan mapping from the approved plan
ORPHAN_MAP = {
    102: "p102_cooling_rates.png",
    112: "p112_area_properties_2.png",
    113: "p113_area_properties_3.png",
    116: "p116_circular_motion.png",
    128: "p128_mass_properties_1.png",
    132: "p132_stress_element.png",
    139: "p139_material_constants.png",
    145: "p145_ideal_gas_mixtures.png",
    159: "p159_steam_tables.png",
    184: "p184_refrigerant_134a.png",
    187: "p187_pipe_flow.png",
    195: "p195_compressibility.png",
    217: "p217_heat_exchanger_ntu.png",
    356: "p356_magnetic_circuits.png",
    361: "p361_transistor_circuits.png",
    374: "p374_bode_plots_detailed.png",
    392: "p392_osi_detailed.png",
    395: "p395_ipv4_header.png",
    40: "p40_mensuration_diag.png",
    68: "p68_control_charts.png",
    75: "p75_normal_dist.png"
}

def patch_json():
    print(f"Patching {JSON_PATH}...")
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    # Handle structure (list vs dict with 'pages')
    pages_list = None
    if isinstance(data, list):
        pages_list = data
    elif isinstance(data, dict) and 'pages' in data:
        pages_list = data['pages']
    
    if pages_list is None:
        print("Could not find pages list in JSON.")
        return

    # 1. Fix Page 121
    p121_found = False
    for page in pages_list:
        if page.get('handbook_page') == 121:
            p121_found = True
            print("Found Page 121. Checking for image block...")
            # Check if image block exists
            has_image = False
            for block in page.get('blocks', []):
                if block.get('type') == 'image' and 'p121_content.png' in block.get('path', ''):
                    has_image = True
                    break
            
            if not has_image:
                print("Adding p121_content.png block...")
                new_block = {
                    "type": "image",
                    "heading": "Content from Page 121",
                    "path": ".agent/skills/fe-handbook-ref/resources/images/p121_content.png",
                    "caption": "Placeholder for missing handbook page 121."
                }
                # Insert at the beginning of blocks for visibility
                if 'blocks' not in page:
                    page['blocks'] = []
                page['blocks'].insert(0, new_block)
            else:
                print("Page 121 already has the image block.")

    # 2. Reintegrate Orphans
    for p_num, img_file in ORPHAN_MAP.items():
        # Find page
        page_entry = next((p for p in pages_list if p.get('handbook_page') == p_num), None)
        if page_entry:
            print(f"Processing Orphan for Page {p_num}: {img_file}")
            # Check if this specific image is already linked
            linked = False
            for block in page_entry.get('blocks', []):
                if block.get('type') == 'image' and img_file in block.get('path', ''):
                    linked = True
                    break
            
            if not linked:
                print(f"  -> Linking {img_file} to Page {p_num}")
                new_block = {
                    "type": "image",
                    "heading": f"Diagram: {img_file.replace('.png', '').replace('_', ' ').title()}",
                    "path": f".agent/skills/fe-handbook-ref/resources/images/{img_file}",
                    "caption": "Reintegrated supplementary diagram."
                }
                if 'blocks' not in page_entry:
                    page_entry['blocks'] = []
                page_entry['blocks'].append(new_block)
        else:
            print(f"Warning: Page {p_num} not found in JSON for orphan {img_file}")

    # Save
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    print("Patch complete.")

if __name__ == "__main__":
    patch_json()
