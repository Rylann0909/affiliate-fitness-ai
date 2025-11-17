# scripts/generate.py
import os
import json
import random
from datetime import datetime

# Paths
PRODUCTS_JSON = "site/products.json"
VIDEOS_DIR = "videos"

# Ensure folders exist
os.makedirs("site", exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

# Add .keep so Git tracks empty videos folder
keep_file = os.path.join(VIDEOS_DIR, ".keep")
if not os.path.exists(keep_file):
    with open(keep_file, "w") as f:
        f.write("placeholder")

# Example products
EXAMPLE_PRODUCTS = [
    {"title":"Adjustable Dumbbell Set","description":"Home workouts","price":79.99,"image":"https://via.placeholder.com/420","affiliate_source":"amazon","affiliate_url":"https://amazon.com/example"},
    {"title":"Resistance Bands","description":"Strengthen muscles anywhere","price":19.99,"image":"https://via.placeholder.com/420","affiliate_source":"clickbank","affiliate_url":"https://clickbank.com/example"},
    {"title":"Yoga Mat","description":"Comfortable and durable","price":25.99,"image":"https://via.placeholder.com/420","affiliate_source":"impact","affiliate_url":"https://impact.com/example"}
]

# Generate 5 random products
products = []
for _ in range(5):
    p = random.choice(EXAMPLE_PRODUCTS)
    safe_title = p["title"].replace(" ","_")
    p["video"] = os.path.join(VIDEOS_DIR,f"{safe_title}.mp4")
    products.append(p)

# Write products.json (timestamp ensures commit)
data = {"generated_at": str(datetime.now()), "products": products}
with open(PRODUCTS_JSON, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(products)} products to {PRODUCTS_JSON}")
