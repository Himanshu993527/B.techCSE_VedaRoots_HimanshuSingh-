import json
import urllib.parse

with open('plants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

emojis = {
    "Tulsi": "🌿",
    "Ashwagandha": "🌰",
    "Neem": "🌳",
    "Turmeric": "🌶️",
    "Aloe Vera": "🌱",
    "Giloy": "🌿",
    "Shatavari": "🌱",
    "Brahmi": "🌿",
    "Karela": "🥒",
    "Arjuna": "🌳"
}

for item in data:
    # Fix Emoji
    if item["name"] in emojis:
        item["emoji"] = emojis[item["name"]]
    
    # Fix URL
    if "ixid=" in item["image"]:
        # Only keep 'photo-id' part up to '?'
        base = item["image"].split("?")[0]
        # Append some generic params
        item["image"] = base + "?w=600&fit=max&q=80"

with open('plants.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Fixed plants.json")
