import os
import sys

import requests
import logging
from datetime import datetime


class ResponseDownloader:

    def __init__(self, content, url, count, download_path):
        self.url = url
        self.content_type = content
        self.count = count
        self.download_path = download_path

        self.logger = logging.getLogger(url)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(filename=os.path.join(download_path, 'requests.log'),
                                           encoding='utf-8', mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stdout_handler)

    def get_headers(self):
        return {
            'Content-Type': self.content_type
        }

    def get_file(self, filename):
        full_filename = os.path.join(self.download_path, filename)
        file_url = f'{self.url}{filename}.pdf'

        headers = self.get_headers()
        self.logger.info(f'{filename} GET: headers={headers}, url={file_url}')
        response = requests.get(file_url, headers=headers)

        if response:
            try:
                self.logger.warning(f'ОТВЕТ: status_code={response.status_code}')
                if response.status_code == 200:
                    with open(full_filename, 'wb') as f:
                        f.write(response.content)
                return response.status_code
            except Exception as e:
                self.logger.error(f'ОТВЕТ: {str(e)}')
                return str(e)

    def get_result(self):
        self.logger.info(f'НАЧАЛО ЗАПРОСОВ ДЛЯ АДРЕСА: {self.url}')

        for i in range(0, self.count):
            self.get_file(f'{i+1}_1-5.pdf')
            self.get_file(f'{i+1}_6-10.pdf')
            self.get_file(f'{i+1}_11-15.pdf')
            self.get_file(f'{i+1}_16-20.pdf')

    @staticmethod
    def now() -> str:
        result = datetime.now().strftime('%m.%d.%y %H:%M:%S')
        return result
