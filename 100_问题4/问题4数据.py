import pandas
import matplotlib.pyplot as plt
import numpy as np

def draw(values, type):
    place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P']
    plt.figure(figsize=(10, 8), dpi=160)
    plt.scatter(place, values, marker='*')
    plt.plot(place, values)
    plt.xlabel('地区')
    plt.ylabel('次数')
    title = 'img/' + type + '事件类型（未分析P地区）'
    plt.title(title)
    plt.grid(linestyle='-.', alpha=0.5)
    # plt.savefig(title)
    plt.show()


data = pandas.read_excel('问题4.xlsx')

area_data = pandas.read_excel('附件1：各区域的人口、面积.xlsx')
area_data = area_data['面积（km2）']

x = ['①', '②', '③', '④', '⑤', '⑥', '⑦']
place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P']

values = []

for i in range(len(x)):
    data_list = data[i:i+1].drop(columns='地区').values[0]
    value = []
    for area in range(len(area_data)):
        value.append(data_list[area] / area_data[area])
    values.append(value)

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(60, 60), dpi=100)

ax[0][0].plot(place, values[0])
ax[0][0].set_title('①类型建模图')

ax[0][1].plot(place, values[1])
ax[0][1].set_title('②类型建模图')


ax[0][2].plot(place, values[2])
ax[0][2].set_title('③类型建模图')


ax[1][0].plot(place, values[3])
ax[1][0].set_title('④类型建模图')

ax[1][1].plot(place, values[4])
ax[1][1].set_title('⑤类型建模图')

ax[1][2].plot(place, values[5])
ax[1][2].set_title('⑥类型建模图')

ax[2][0].plot(place, values[6])
ax[2][0].set_title('⑦类型建模图')

# plt.savefig('图-问题4')
plt.show()
