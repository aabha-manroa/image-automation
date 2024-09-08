from icrawler.builtin import BingImageCrawler

# Create a crawler instance for Bing
crawler = BingImageCrawler(storage={"root_dir": "outputfolder1"})

# Define your search criteria
crawler.crawl(
    keyword="sunset beach",  # Search for whatever images you want
    max_num=10,              # Number of images to download
    file_idx_offset=0
)
