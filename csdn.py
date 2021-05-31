import requests

import json
from bs4 import BeautifulSoup


class CsdnSeacher:
    def __init__(self):
        self.url = 'https://so.csdn.net/api/v3/search?q={}&t={}'
        self.headers = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
                'Origin': 'https://blog.csdn.net'
            }
        ]

    def get_requests(self, url):
        return requests.get(url).content.decode()

    def parse_data(self, data):
        json_data = json.loads(data)
        result_data = json_data['result_vos']
        blogs = []
        for i in result_data:
            content = BeautifulSoup(requests.get(url=i['url_location'], headers=self.headers[0]).content.decode()).find(attrs={'id': 'article_content'}).getText()
            blog = {'title': i['title'], 'content': content, 'url_location': i['url_location']}
            blogs.append(blog)
        return blogs

    def write_to_file(self, data, filename):
        with open(f'./csdn/{filename}', 'w', encoding='utf-8') as f:
            f.write(data)

    def run(self, q='python', t='all'):
        url = self.url.format(q, t)
        result = self.get_requests(url)
        data = self.parse_data(result)
        self.write_to_file(data, f'{q}查询结果')
        pass


if __name__ == '__main__':
    CsdnSeacher().run()
