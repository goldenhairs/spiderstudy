import requests
from bs4 import BeautifulSoup
import re
import json


class VirusData(object):
    def __init__(self):
        home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia').content.decode()
        soup = BeautifulSoup(home_page, 'lxml').find(attrs={'id': 'getListByCountryTypeService2true'})
        json_data = re.findall(r'\[.+\]', str(soup))[0]
        self.last_day_corona_virus_data = json.loads(json_data)

    def get_virus_data(self, country='中国', start=20210101, end=20210110):
        """
        返回制定国家在规定时间内的疫情数据
        :param country:
        :param start:
        :param end:
        :return: 返回一个字典列表，每个字段的含义为：
                        confirmedCount  --  累计确诊
                        confirmedIncr -- 新增确诊
                        curedCount -- 累计治愈
                        curedIncr -- 新增治愈
                        currentConfirmedCount -- 现存确诊
                        currentConfirmedIncr -- 确诊增量，如果为复数说明现存确诊人数减少
                        dateId -- 日期
                        deadCount -- 累计死亡
                        deadIncr -- 新增死亡
                        highDangerCount -- 高风险数量
                        midDangerCount -- 中风险数量
                        suspectedCount -- 累计境外输入
                        suspectedCountIncr -- 新增境外输入
        """
        result_list = []

        for country_data in self.last_day_corona_virus_data:
            if country_data['provinceName'] == country:
                url = country_data['statisticsData']
                country_data_dict = json.loads(requests.get(url).content.decode())['data']

                for day_data in country_data_dict:
                    if start <= day_data['dateId'] <= end:
                        result_list.append(day_data)
        return result_list


v = VirusData()
china_datas = v.get_virus_data(country='中国', start=20200123, end=20210208)
china = []

for data in china_datas:
    china.append(data['confirmedIncr'])

print(china)
