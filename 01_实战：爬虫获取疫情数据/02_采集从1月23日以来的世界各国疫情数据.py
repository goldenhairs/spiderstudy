import requests
from bs4 import BeautifulSoup
import re
import json

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

soup = BeautifulSoup(home_page, 'lxml')
datas = soup.find(attrs={'id': 'getListByCountryTypeService2true'})

json_str = re.findall(r'\[.+\]', str(datas))[0]

all_corona_virus_world = json.loads(json_str)

for country in all_corona_virus_world:
    url = country['statisticsData']
    countryDatas = requests.get(url)
    jsonDatas = countryDatas.content.decode()


    file_name = '所有数据/' + country['provinceName']
    with open(file_name, 'w', encoding='utf8') as fp:
        fp.write(jsonDatas)
