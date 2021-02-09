import requests
from bs4 import BeautifulSoup
import re
import json


class CoronaVirusData(object):
    def __init__(self):
        home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia').content.decode()
        soup = BeautifulSoup(home_page, 'lxml')
        # 获取所有国家的数据
        page_data = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
        json_data = re.findall(r'\[.+]', str(page_data))[0]
        self.list_data = json.loads(json_data)

    def get_all_data_list(self, start=20200123):
        all_confirmed_count = []
        country_name = []
        time = self.__get_all_time()
        # 对每个国家进行遍历
        for country in self.list_data:
            if country['provinceName'] in ['美国', '英国', '法国', '俄罗斯', '中国', '印度']:
                country_name.append(country['provinceName'])
                country_all_data_json = requests.get(country['statisticsData']).content.decode()
                country_all_data_list = json.loads(country_all_data_json)['data']
                # 获取国家的确诊总数
                confirmed_count = []
                for country_data in country_all_data_list:
                    if start < country_data['dateId']:
                        confirmed_count.append(str(country_data['confirmedCount']))
                all_confirmed_count.append(confirmed_count)
        return all_confirmed_count, country_name, time

    def __get_all_time(self):
        time = []
        all_json = requests.get(self.list_data[0]['statisticsData']).content.decode()
        all_list = json.loads(all_json)['data']
        for i in all_list:
            time.append(str(i['dateId']))
        return time

c = CoronaVirusData()
count, name, time1 = c.get_all_data_list()
print(name)

