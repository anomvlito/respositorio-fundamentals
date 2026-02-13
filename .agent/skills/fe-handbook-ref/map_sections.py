import json
import re

def generate_table():
    with open('resources/handbook_map.json', 'r') as f:
        data = json.load(f)
    
    pages = data.get('pages', [])
    pages.sort(key=lambda x: x['handbook_page'])
    
    sections = []
    current_section = None
    start_page = None
    end_page = None
    pdf_start = None
    pdf_end = None
    
    # Heuristic to group titles. e.g. "Mathematics (Discrete)" -> "Mathematics"
    def get_main_topic(title):
        if "Handbook Page" in title: return "Unassigned / Gap"
        if "(" in title:
            return title.split('(')[0].strip()
        return title.strip()

    for p in pages:
        h_page = p['handbook_page']
        pdf_idx = p['pdf_index']
        title = p.get('title', 'Unknown')
        main_topic = get_main_topic(title)
        
        if current_section != main_topic:
            if current_section:
                sections.append({
                    'topic': current_section,
                    'h_range': f"{start_page}-{end_page}" if start_page != end_page else str(start_page),
                    'pdf_range': f"{pdf_start}-{pdf_end}" if pdf_start != pdf_end else str(pdf_start)
                })
            current_section = main_topic
            start_page = h_page
            end_page = h_page
            pdf_start = pdf_idx
            pdf_end = pdf_idx
        else:
            end_page = h_page
            pdf_end = pdf_idx
            
    # Add last
    if current_section:
        sections.append({
            'topic': current_section,
            'h_range': f"{start_page}-{end_page}" if start_page != end_page else str(start_page),
            'pdf_range': f"{pdf_start}-{pdf_end}" if pdf_start != pdf_end else str(pdf_start)
        })

    print("| Section | Handbook Page (Printed) | PDF Page (Index) |")
    print("|---------|-------------------------|------------------|")
    for s in sections:
        print(f"| {s['topic']} | {s['h_range']} | {s['pdf_range']} |")

if __name__ == "__main__":
    generate_table()
