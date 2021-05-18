# !-*- coding: utf8 -*-
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeRegressor

data_source = pd.read_excel('附件2：某地消防救援出警数据.xlsx')

data = data_source['接警日期']

month_times_dict_train = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                          '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

month_times_dict_test = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                         '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

for i in range(len(data)):
    if str(data[i]).split('-')[0] == '2020':
        month_times_dict_test[str(data[i]).split('-')[1]] += 1
    else:
        month_times_dict_train[str(data[i]).split('-')[1]] += 1

x_train = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_train = []
max_depth = 5

for k, v in month_times_dict_train.items():
    y_train.append(int(v))

x_train = np.array(x_train).reshape(-1, 1)
y_train = np.array(y_train).reshape(-1, 1) / 4

r_tree = DecisionTreeRegressor(max_depth=max_depth)
r_tree.fit(x_train, y_train)
h = r_tree.predict(x_train)

print('真实值', end='        ')
for item in y_train:
    print('%.2f' % item[0], end=' ')
print()

print('预测值', max_depth, '树', end='   ')
for item in h:
    print('%.2f' % item, end=' ')
print()

test = []
for k, v in month_times_dict_test.items():
    test.append(int(v))

print('熵', r_tree.score(x_train, test))
print()

plt.figure(figsize=(10, 8), dpi=80)

plt.plot(x_train, h, label='预测值', color='r')
plt.plot(x_train, test, label='真实值', color='b')
plt.legend()

plt.grid(linestyle='-.', alpha=0.5)
title = '最大深度为' + str(max_depth) + '的决策树预测'
plt.title(title)
plt.xlabel('月份')
plt.ylabel('接警次数')
plt.savefig(title)

for i in h:
    print(round(i), end='  ')
