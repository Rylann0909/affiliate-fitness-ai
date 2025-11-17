# scripts/generate.py
# Safe version for GitHub Actions

import os
import json
import random
from datetime import datetime
os.makedirs("site", exist_ok=True)
os.makedirs("videos", exist_ok=True)
# --- CONFIG ---
PRODUCTS_JSON = "site/products.json"
VIDEOS_DIR = "videos"

AFFILIATE_PROGRAMS = ["amazon", "clickbank", "impact"]

# Example products (replace with real API or scraping logic)
EXAMPLE_PRODUCTS = [
    {
        "title": "Adjustable Dumbbell Set",
        "description": "Perfect for home workouts",
        "price": 79.99,
        "image": "https://via.placeholder.com/420",
        "affiliate_source": "amazon",
        "affiliate_url": "https://amazon.com/example"
    },
    {
        "title": "Resistance Bands",
        "description": "Strengthen your muscles anywhere",
        "price": 19.99,
        "image": "https://via.placeholder.com/420",
        "affiliate_source": "clickbank",
        "affiliate_url": "https://clickbank.com/example"
    },
    {
        "title": "Yoga Mat",
        "description": "Comfortable and durable",
        "price": 25.99,
        "image": "https://via.placeholder.com/420",
        "affiliate_source": "impact",
        "affiliate_url": "https://impact.com/example"
    }
]

# --- FUNCTIONS ---
def generate_products(n=5):
    products = []
    for _ in range(n):
        p = random.choice(EXAMPLE_PRODUCTS)
        # create video path even if video doesn't exist yet
        safe_title = p['title'].replace(' ', '_')
        p['video'] = os.path.join(VIDEOS_DIR, f"{safe_title}.mp4")
        products.append(p)
    return products

def save_products(products):
    data = {"generated_at": str(datetime.now()), "products": products}
    os.makedirs(os.path.dirname(PRODUCTS_JSON), exist_ok=True)
    with open(PRODUCTS_JSON, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(products)} products to {PRODUCTS_JSON}")

def ensure_videos_folder():
    # make videos folder if missing
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    keep_file = os.path.join(VIDEOS_DIR, ".keep")
    if not os.path.exists(keep_file):
        with open(keep_file, "w") as f:
            f.write("placeholder")
        print("Created videos/.keep placeholder")

def main():
    ensure_videos_folder()
    products = generate_products(n=5)
    save_products(products)
    print("Done generating products.")

if __name__ == "__main__":
    main()
