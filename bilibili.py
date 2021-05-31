import requests

from bs4 import BeautifulSoup

import json


class bilibili:
    def __init__(self):
        self.url = 'https://search.bilibili.com/all?keyword={}&page={}'

    def get_requests(self, url):
        return requests.get(url).content.decode()

    def parse_data(self, src_data):
        video_list = []
        soup = BeautifulSoup(src_data).find_all(attrs={'class': 'video-item matrix'})
        for i in soup:
            title = i.find(attrs={'class': 'img-anchor'}).get('title')
            url = i.find(attrs={'class': 'img-anchor'}).get('href').replace('//', 'http://')

            html = requests.get(url).content.decode()
            tag_soup = BeautifulSoup(html).find_all(attrs={'class': 'tag'})
            tag_list = []
            for t in tag_soup:
                tag_list.append(t.find('span'))
            video = {
                'title': title,
                'url': url,
                'tag': tag_list
            }
            video_list.append(video)
        return video_list

    def write_to_file(self, data, keyword):
        with open(f'./bilibili/{keyword}', 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def run(self, keyword='蓝桥杯决赛', page=3):
        result = []
        for i in range(1, page + 1):
            url = self.url.format(keyword, i)
            src_data = self.get_requests(url)
            result.extend(self.parse_data(src_data))
        result = {'result': result}
        self.write_to_file(result, keyword)


if __name__ == '__main__':
    bilibili().run()
