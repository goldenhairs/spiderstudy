import requests
from bs4 import BeautifulSoup
import re
import json

response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_page = response.content.decode()

soup = BeautifulSoup(home_page, 'lxml')
datas = soup.find(attrs={'id': 'getAreaStat'})

json_str = re.findall(r'\[.+\]', str(datas))[0]

last_day_corona_virus_china = json.loads(json_str)

with open('近一日数据/last_day_corona_virus_china.json', 'w', encoding='utf8') as fp:
    json.dump(last_day_corona_virus_china, fp, ensure_ascii=False)
