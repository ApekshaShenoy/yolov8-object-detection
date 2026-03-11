from icrawler.builtin import BingImageCrawler
import os

classes = {
    "red_cup": ["red cup on table", "red coffee mug", "red mug kitchen", "red ceramic cup", "small red cup"],
    # "blue_bottle": ["blue water bottle", "blue plastic bottle", "blue sports bottle"],
    # "phone": ["smartphone on table", "mobile phone on desk", "smartphone with objects"]
}

base_folder = "dataset/images"

for class_name, queries in classes.items():
    folder = os.path.join(base_folder, class_name)
    os.makedirs(folder, exist_ok=True)

    for query in queries:
        print(f"Crawling '{query}' into '{folder}'")
        crawler = BingImageCrawler(
            storage={"root_dir": folder},
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4
        )
        crawler.crawl(
            keyword=query,
            max_num=100,
            filters={
                "size": "large",        
                "type": "photo"        
            }
        )