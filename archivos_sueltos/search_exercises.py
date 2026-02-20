import json
import re

KEYWORDS = [
    "Poisson", "Log-Normal", "Confidence Interval", "Goodness of Fit", "Chi-Square",
    "Regression", "Slope", "Intercept", "Correlation", "Covariance",
    "Pendulum", "Circular Motion", "Tension", "Centripetal",
    "Incline", "Friction", "Newton", "Force"
]

MAP_PATH = ".agent/skills/fe-handbook-ref/resources/handbook_map.json"

try:
    with open(MAP_PATH) as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: handbook_map.json not found")
    exit(1)

print(f"{'KEYWORD':<25} | {'PAGE':<5} | {'TITLE':<40}")
print("-" * 80)

hits = []

for page in data['pages']:
    page_text = ""
    # Title
    page_text += str(page.get('title', '')) + " "
    
    # Blocks
    for block in page.get('blocks', []):
        page_text += str(block.get('heading', '')) + " "
        page_text += str(block.get('content', '')) + " "
        # Items (formulas)
        for item in block.get('items', []):
            if isinstance(item, dict):
                page_text += str(item.get('name', '')) + " "
                page_text += str(item.get('latex', '')) + " "
            else:
                page_text += str(item) + " "
            
    # Search
    for kw in KEYWORDS:
        # Use simple substring for broader matches or regex for boundaries
        # I'll use case-insensitive substring for robustness
        if kw.lower() in page_text.lower():
            # Don't print every match, just unique page-keyword pairs
            if (kw, page['handbook_page']) not in hits:
                print(f"{kw:<25} | {page['handbook_page']:<5} | {str(page.get('title', ''))[:40]:<40}")
                hits.append((kw, page['handbook_page']))

# Summary
print("\n--- Summary of Findings ---")
found_kws = set(h[0] for h in hits)
for kw in KEYWORDS:
    pages = sorted(list(set([h[1] for h in hits if h[0] == kw])))
    if pages:
        print(f"✅ {kw}: {pages}")
    else:
        print(f"❌ {kw}: Not found")
