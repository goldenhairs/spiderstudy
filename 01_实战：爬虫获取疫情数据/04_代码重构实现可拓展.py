import requests
from bs4 import BeautifulSoup
import re
import json


class CoronaVirusRequests:
    def __init__(self):
        home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia').content.decode()
        data = BeautifulSoup(home_page, 'lxml').find(attrs={'id': 'getListByCountryTypeService2true'})
        json_data = re.findall(r'\[.+]', str(data))[0]
        self.world_data = json.loads(json_data)
        pass

    def get_last_day_data(self, country='world'):
        """
        获取最新疫情数据
        :param country: 指定国家，默认为获取全世界数据
        :return:
        """
        if 'world'.__eq__(country):
            return self.world_data
        else:
            return self.get_last_data(country)

    def get_all_data(self, country):
        """
        获取指定国家所有疫情数据
        :param country: 指定的国家
        :return:
        """
        country_data = self.get_last_data(country)
        url = country_data['statisticsData']
        json_data = requests.get(url).content.decode()
        all_data = json.loads(json_data)
        return all_data['data']

    def get_last_data(self, country):
        for country_data in self.world_data:
            if country_data['provinceName'] == country:
                return country_data
        raise NoCountryFoundException()


class NoCountryFoundException(Exception):
    def __init__(self):
        self.message = '没有此国家！'

    def __str__(self):
        return self.message
