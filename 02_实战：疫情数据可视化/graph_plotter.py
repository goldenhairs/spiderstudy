import json
import re

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from matplotlib.animation import FuncAnimation


class CoronaVirusData(object):
    def __init__(self):
        home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia').content.decode()
        soup = BeautifulSoup(home_page, 'lxml')
        # 获取所有国家的数据并进行处理
        page_data = soup.find(attrs={'id': 'getListByCountryTypeService2true'})
        json_data = re.findall(r'\[.+]', str(page_data))[0]
        self.list_data = json.loads(json_data)

    def get_all_data_list(self, start=20200201):
        """
        获取六个国家的确诊总数、国家名称；以及返回时间序列
        :param start: 开始时间，为了保证每个位置上都有数据，建议从20200201开始
        :return:
        """
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
                    if start <= country_data['dateId']:
                        confirmed_count.append(country_data['confirmedCount'])
                all_confirmed_count.append(confirmed_count)
        return all_confirmed_count, country_name, time

    def __get_all_time(self):
        """
        获取时间序列
        :return:
        """
        time = []
        all_json = requests.get(self.list_data[0]['statisticsData']).content.decode()
        all_list = json.loads(all_json)['data']
        for i in all_list:
            time.append(i['dateId'])
        return time[9:]


# 处理中文不能正常显示问题
# plt.rcParams['font.sans-serif'] = ['FangSong']
# plt.rcParams['axes.unicode_minus'] = False

# 获取并处理数据
data, country, time = CoronaVirusData().get_all_data_list()

x = list(range(len(time)))
time_label = ['{}月{}日'.format(i % 10000 // 100, i % 100) for i in time]
usa_data = data[0]
uk_data = data[1]
france_data = data[2]
russia_data = data[3]
india_data = data[4]
china_data = data[5]
fig = plt.figure(figsize=(10, 6), dpi=80)

# 创建六个国家的折线
usa_line, = plt.plot([], [], color='b', marker='o', label='美国')
uk_line, = plt.plot([], [], color='y', marker='o', label='英国')
france_line, = plt.plot([], [], color='pink', marker='o', label='法国')
russia_line, = plt.plot([], [], color='deepskyblue', marker='o', label='俄罗斯')
india_line, = plt.plot([], [], color='g', marker='o', label='印度')
china_line, = plt.plot([], [], color='r', marker='o', label='中国')

# 显示图例
plt.legend()


# 获取y轴的上下限
def get_ylim(i):
    count = []
    for j in data:
        count.append(j[i])
    return min(count) * 0.7, max(count) * 1.3


# 对y轴的设置，分别为：初始y轴的上下限、禁止y轴使用科学计数法、y轴的标签
plt.ylim(get_ylim(0)[0], get_ylim(0)[1])
plt.ticklabel_format(style='plain')
plt.ylabel('累计确诊人数')

# 对x轴的设置，分别为：初始x轴的范围、x轴坐标更改（即将20200201更改为2月1日，以此类推）
x_range = 10
plt.xlim(0, x_range)
plt.xticks(x[0:x_range], time_label[0:x_range])

line_range = 8


def update(i):
    """
    动画更新函数
    :param i:
    :return:
    """
    # 获取x轴需要展示的范围
    start = 0 if i - line_range < 0 else i - line_range
    end = i + 1
    # 对六个国家的数据进行更新
    usa_line.set_data(x[start:end], usa_data[start:end])
    uk_line.set_data(x[start:end], uk_data[start:end])
    france_line.set_data(x[start:end], france_data[start:end])
    russia_line.set_data(x[start:end], russia_data[start:end])
    india_line.set_data(x[start:end], india_data[start:end])
    china_line.set_data(x[start:end], china_data[start:end])
    # 更新x轴
    if i > line_range:
        x_end = i + (x_range - line_range) if i + (x_range - line_range) < len(x) else len(x)
        plt.xlim(start, x_end)
        plt.xticks(ticks=x[start:end], labels=time_label[start:end])
    # 更新y轴和x轴的标签
    plt.ylim(get_ylim(i)[0], get_ylim(i)[1])
    plt.xlabel('{}年'.format(time[i] // 10000))
    return usa_line, uk_line, france_line, russia_line, india_line, china_line


# 动画的标题
plt.title('2020年2月1日以来“五常”与印度确诊人数')

# 展示动画
animation = FuncAnimation(fig, update, frames=x, repeat=False, interval=200)

# 保存文件(gif格式需要安装Pillow、mp4格式需要安装ffmpeg)
# animation.save(filename='2020年2月1日以来“五常”与印度确诊人数.mp4')

# 展示动画
plt.show()
