import json

with open('.agent/skills/fe-handbook-ref/resources/handbook_map.json', 'r') as f:
    d = json.load(f)

for p in d['pages']:
    text = p.get('content_raw', '').lower()
    if 'thermal deformation' in text or 'alpha' in text and 'delta t' in text:
        print(f"Page {p['handbook_page']}: {p['title']}")
