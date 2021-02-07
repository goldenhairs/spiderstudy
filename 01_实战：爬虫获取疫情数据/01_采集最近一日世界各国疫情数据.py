import requests
from bs4 import BeautifulSoup
import re
import json

# 1. 发送请求，获取疫情首页
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 2. 从疫情首页提取最近一日各国疫情数据
soup = BeautifulSoup(home_page, 'lxml')
datas = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
# 3. 从疫情数据中，获取json格式的字符串
json_str = re.findall(r'\[.+\]', str(datas))[0]

# 4. 把json格式的字符串转换为python类型
last_day_corona_virus_world = json.loads(json_str)
# 5. 以json格式保存，最近一日各国疫情数据
with open('data/last_day_corona_virus_world.json', 'w', encoding='utf8') as fp:
    json.dump(last_day_corona_virus_world, fp, ensure_ascii=False)
