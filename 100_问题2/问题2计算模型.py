# !-*- coding: utf8 -*-
# 一元线性回归分析
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeRegressor


def decisionTree(month_times_dict_train, max_depth, year, month_times_dict_test):
    x_train = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_train = []

    for k, v in month_times_dict_train.items():
        y_train.append(int(v))

    x_train = np.array(x_train).reshape(-1, 1)
    y_train = np.array(y_train).reshape(-1, 1)

    r_tree = DecisionTreeRegressor(max_depth=max_depth)

    r_tree.fit(x_train, y_train)

    h = r_tree.predict(x_train)

    print(year, '真实值', end='        ')
    for item in y_train:
        print('%.2f' % item[0], end=' ')
    print()
    print(year, '预测值', max_depth, '树', end='   ')
    for item in h:
        print('%.2f' % item, end=' ')
    print()

    test = []
    for k, v in month_times_dict_test.items():
        test.append(int(v))
    print('得分', r_tree.score(x_train, test))
    print()
    # plt.figure(figsize=(10, 8), dpi=80)
    # plt.plot(x_train, y_train, label='真实值')
    # plt.plot(x_train, h, label='预测值')
    # plt.xlabel('月份')
    # plt.ylabel('比例')
    # title = str(year) + '每月出警比例' + str(max_depth) + '次决策树'
    # plt.title(title)
    # plt.grid(linestyle='-.', alpha=0.5)
    # plt.legend()
    # plt.savefig(title)

    return h


# 用pandas读取excel
data_source = pd.read_excel('附件2：某地消防救援出警数据.xlsx')

data = data_source['接警日期']

month_times_dict_train_1 = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                            '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

month_times_dict_train_2 = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                            '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

month_times_dict_train_3 = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                            '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

month_times_dict_train_4 = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                            '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

month_times_dict_test = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                         '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

for i in range(len(data)):
    if str(data[i]).split('-')[0] == '2016':
        month_times_dict_train_1[str(data[i]).split('-')[1]] += 1
    if str(data[i]).split('-')[0] == '2017':
        month_times_dict_train_2[str(data[i]).split('-')[1]] += 1
    if str(data[i]).split('-')[0] == '2018':
        month_times_dict_train_3[str(data[i]).split('-')[1]] += 1
    if str(data[i]).split('-')[0] == '2019':
        month_times_dict_train_4[str(data[i]).split('-')[1]] += 1
    if str(data[i]).split('-')[0] == '2020':
        month_times_dict_test[str(data[i]).split('-')[1]] += 1

h1 = decisionTree(month_times_dict_train_1, 5, 2016, month_times_dict_test)
h2 = decisionTree(month_times_dict_train_2, 5, 2017, month_times_dict_test)
h3 = decisionTree(month_times_dict_train_3, 5, 2018, month_times_dict_test)
h4 = decisionTree(month_times_dict_train_4, 5, 2019, month_times_dict_test)

h = (h1 + h2 + h3 + h4) / 4
h_list = []
for i in h:
    h_list.append(float('%.2f' % i))
    print('%.2f' % i, end=' ')


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.figure(figsize=(10, 8), dpi=80)
plt.scatter(x, h1, label='2016年')
plt.scatter(x, h2, label='2017年')
plt.scatter(x, h3, label='2018年')
plt.scatter(x, h4, label='2019年', color='grey')
plt.plot(x, h_list, marker='*', label='均值', color='r')
plt.title('预测比例散点图')
plt.grid(linestyle='-.', alpha=0.5)
plt.legend()
plt.savefig('预测比例散点图')
