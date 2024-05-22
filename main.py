from pprint import pprint
from response_downloader import ResponseDownloader

DOWNLOAD_PATH = 'C:\\Users\\63286\\Pictures\\PDD'
CONTENT_TYPE = 'application/pdf'
COUNT = 1
URLS = [
    'https://xn--90adear.xn--p1ai/upload/site1000/folder/original/avtovladeltsam/fees/abm-2023/',
    'https://xn--90adear.xn--p1ai/upload/site1000/folder/original/avtovladeltsam/fees/cd-2023/'
]

if __name__ == '__main__':
    for url in URLS:
        print(f'--- GET ЗАПРОСЫ по адресу:  "{url}" ---')
        downloader = ResponseDownloader(CONTENT_TYPE, url, COUNT, DOWNLOAD_PATH)
        pprint(downloader.get_result())
