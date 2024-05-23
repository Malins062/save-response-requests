import os.path
from response_downloader import ResponseDownloader

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), 'download')
FILE_LOG = 'download.log'
CONTENT_TYPE = 'application/pdf'
REQUESTS = [
    {
        'url': 'https://xn--90adear.xn--p1ai/upload/site1000/folder/original/avtovladeltsam/fees/abm-2023/',
        'dir': os.path.join(DOWNLOAD_DIR, 'ABM'),
        'count': 40,
    },
    {
        'url': 'https://xn--90adear.xn--p1ai/upload/site1000/folder/original/avtovladeltsam/fees/cd-2023/',
        'dir': os.path.join(DOWNLOAD_DIR, 'CD'),
        'count': 40,
    },
]

if __name__ == '__main__':
    for req in REQUESTS:
        downloader = ResponseDownloader(CONTENT_TYPE, req.get('url'), req.get('count'), req.get('dir'))
        downloader.get_result()
