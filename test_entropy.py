import json

with open('.agent/skills/fe-handbook-ref/resources/handbook_map.json', 'r') as f:
    d = json.load(f)

for p in d['pages']:
    text = p.get('content_raw', '').lower()
    if 'entrop' in text:
        if 'probab' in text or 'boltzmann' in text or 'micro' in text or 'equili' in text:
            print(f"Page {p['handbook_page']}: {p['title']}")
