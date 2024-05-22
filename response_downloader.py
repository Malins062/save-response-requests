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
            'datetime_begin': datetime.now(),
            'filename': full_filename,
        }
        content = self.get_response(f'{filename}.pdf')
        request['result'] = self.save_content(content, full_filename)
        request['datetime_end'] = datetime.now()

        return request

    def get_result(self):
        response = {
            'url': self.url,
            'datetime_begin': datetime.now(),
            'requests': [],
        }

        for i in range(1, self.count):
            filename = f'{i}_1_15.pdf'
            response['requests'] += self.get_file(filename)

        response['datetime_end'] = datetime.now()

        return response

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f"File - {disk_file_path} success download.")