import requests
from datetime import datetime


class ResponseDownloader:

    def __init__(self, content, url, count, download_path):
        self.url = url
        self.content_type = content
        self.count = count
        self.download_path = download_path

    def get_headers(self):
        return {
            'Content-Type': self.content_type
        }

    def get_response(self, filename: str):
        file_url = f'{self.url}{filename}'
        headers = self.get_headers()

        response = requests.get(file_url, headers=headers)
        return response.content

    def save_content(self, content, filename):
        try:
            with open(f'{self.download_path}{filename}', 'wb') as f:
                f.write(content)
                return 'OK'
        except Exception as e:
            return str(e)

    def get_file(self, filename):
        full_filename = f'{self.download_path}{filename}'
        request = {
            'datetime_begin': self.now(),
            'filename': full_filename,
        }
        content = self.get_response(f'{filename}.pdf')
        request['result'] = self.save_content(content, full_filename)
        request['datetime_end'] = self.now()

        return request

    def get_result(self):
        response = {
            'url': self.url,
            'datetime_begin': self.now(),
            'requests': [],
        }

        for i in range(0, self.count):
            filename = f'{i}_1_15.pdf'
            response['requests'] += self.get_file(filename)

        response['datetime_end'] = self.now()

        return response

    @staticmethod
    def now():
        return datetime.now().strftime('%m/%d/%y %H:%M:%S')