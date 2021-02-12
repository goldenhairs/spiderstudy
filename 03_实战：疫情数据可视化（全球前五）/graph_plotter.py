import copy

import requests
import re
from bs4 import BeautifulSoup
import json
import pandas as pd
import datetime


class CoronaVirusData(object):
    def __init__(self):
        home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia').content.decode()
        soup = BeautifulSoup(home_page, 'lxml')
        # 获取所有国家的数据并进行处理
        page_data = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
        json_data = re.findall(r'\[.+]', str(page_data))[0]
        self.list_data = json.loads(json_data)

    def get_all_data_list(self):
        time, time_dict = self.__get_all_time()

        country_current_dataframe = pd.DataFrame(columns=time)

        for i in self.list_data:
            country_data = copy.deepcopy(time_dict)
            country_all_data_json = requests.get(i['statisticsData']).content.decode()
            country_all_data_list = json.loads(country_all_data_json)['data']

            country_data['国家'] = i['provinceName']

            for data_list in country_all_data_list:
                key = data_list['dateId']
                value = data_list['currentConfirmedCount']
                country_data[key].append(value)
            for k, v in country_data.items():
                if not v:
                    country_data[k].append(0)
            country_current_dataframe = country_current_dataframe.append(pd.DataFrame(country_data), ignore_index=True)
        country_current_dataframe.to_csv('data/自2020年1月19日以来全球各国当日存在确诊人数统计表.csv', index=False)

    def __get_all_time(self):
        """
        获取时间序列
        :return:
        """
        time = ['国家']
        time_dict = {'国家': []}
        now = datetime.datetime.now()
        for year in [2020, 2021]:
            for month in range(1, 13):
                days = []
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    days = list(range(1, 32))
                if month in [4, 6, 9, 11]:
                    days = list(range(1, 31))
                if month == 2 and year == 2020:
                    days = list(range(1, 30))
                if month == 2 and year == 2021:
                    days = list(range(1, 29))
                if month == 1 and year == 2020:
                    days = list(range(19, 32))
                for day in days:
                    date_id = year * 10000 + month * 100 + day
                    time.append(date_id)
                    time_dict[date_id] = []
                    if date_id == now.year * 10000 + now.month * 100 + now.day - 1:
                        return time, time_dict

    def test(self):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        print(year * 10000 + month * 100 + day)


c = CoronaVirusData()
c.get_all_data_list()
