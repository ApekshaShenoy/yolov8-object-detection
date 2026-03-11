import os
import time
import random
import requests
from tqdm import tqdm
from duckduckgo_search import DDGS

# Search queries
search_queries = [
    "red cup",
    "red coffee mug",
    "red mug on table",
    "red ceramic cup"
]

# Your dataset folder
output_folder = r"D:\CAPSTONE_PROJECT\object_detection_project\dataset\images\red_cup"
os.makedirs(output_folder, exist_ok=True)


def download_images(query, limit=50, retries=3):

    print(f"\nSearching images for: {query}")

    for attempt in range(retries):

        try:
            with DDGS() as ddgs:
                results = list(ddgs.images(query, max_results=limit))

            if not results:
                print("No results found")
                return

            start_index = len(os.listdir(output_folder))

            for i, img in enumerate(tqdm(results, desc="Downloading")):

                try:
                    url = img["image"]

                    response = requests.get(
                        url,
                        timeout=10,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )

                    ext = url.split(".")[-1].split("?")[0]

                    if ext.lower() not in ["jpg", "jpeg", "png"]:
                        ext = "jpg"

                    filename = f"red_cup_{start_index+i+1}.{ext}"
                    filepath = os.path.join(output_folder, filename)

                    with open(filepath, "wb") as f:
                        f.write(response.content)

                except Exception as e:
                    print(f"Failed image {i+1}: {e}")

            print(f"Finished downloading for '{query}'")
            return

        except Exception as e:

            print(f"Attempt {attempt+1} failed: {e}")

            wait = random.randint(5, 10)
            print(f"Waiting {wait} seconds before retry...")
            time.sleep(wait)

    print(f"Failed completely for {query}")


# Run downloader
for query in search_queries:

    download_images(query, limit=50)

    # delay between queries to avoid rate limit
    time.sleep(random.randint(5, 8))