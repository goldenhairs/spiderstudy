import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

corona_df = pd.read_csv('data/疫情数据.csv', index_col='国家')


def get_top_of_day(i):
    """
    获取当日现存确诊人数排名前五的数据
    :param i: 第几天
    :return: 日期、国家、数据
    """
    data_of_day = corona_df.iloc[:, i:i + 1]
    columns_name = data_of_day.columns.values[0]
    data_of_day = data_of_day.sort_values(columns_name, ascending=False).head()
    date = int(data_of_day.columns.values[0])
    country = data_of_day.index.values
    data = data_of_day.values.reshape(1, -1)[0]
    return date, country, data


columns_ndarray = corona_df.columns.values

x = list(range(len(columns_ndarray)))
x_labels = ['{}月{}日'.format(int(i) % 10000 // 100, int(i) % 100) for i in columns_ndarray]

fig = plt.figure(figsize=(10, 6), dpi=80)

fir_line = plt.plot([], [])
sec_line = plt.plot([], [])
thr_line = plt.plot([], [])
for_line = plt.plot([], [])
fit_line = plt.plot([], [])

x_range = 10
plt.xticks(x[0:x_range], x_labels[0:x_range])

line_range = 6


def update(i):
    start = 0 if i - line_range < 0 else i - line_range
    end = i + 1
    

animation = FuncAnimation()

plt.show()

