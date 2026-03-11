# importing google_images_download module
from google_images_download import google_images_download 

# creating object
response = google_images_download.googleimagesdownload() 

# Search queries for red cup images
search_queries = [
    "red cup",
    "red coffee mug",
    "red mug on table",
    "red ceramic cup",
]

def downloadimages(query):
    arguments = {
        "keywords": query,
        "format": "jpg",
        "limit": 50,       # number of images per query
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "square"
    }
    try:
        response.download(arguments)
    except FileNotFoundError: 
        # fallback if aspect_ratio causes errors
        arguments.pop("aspect_ratio")
        try:
            response.download(arguments)
        except:
            pass

# Driver code
for query in search_queries:
    downloadimages(query)
    print(f"Downloaded images for query: {query}")