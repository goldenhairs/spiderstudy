# !-*- coding: utf8 -*-
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeRegressor


def decisionTree(train_dict: dict, test_dict: dict, max_depth, type):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = []

    for k, v in train_dict.items():
        y.append(int(v))

    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1) / 5

    r_tree = DecisionTreeRegressor(max_depth=max_depth)

    r_tree.fit(x, y)

    h = r_tree.predict(x)

    print(type, '类型')
    print('真实值', end='        ')
    for item in y:
        print('%.2f' % item[0], end=' ')
    print()
    print('预测值', max_depth, '树', end='   ')
    for item in h:
        print('%.2f' % item, end=' ')
    print()

    test = []
    for k, v in test_dict.items():
        test.append(int(v))
    print('得分', r_tree.score(x, test))
    print()
    plt.figure(figsize=(10, 8), dpi=80)
    plt.plot(x, y, label='训练集值', color='r')
    plt.plot(x, test, label='检测集值', color='g')
    plt.plot(x, h, label='预测值', color='b')
    plt.xlabel('月份')
    plt.ylabel('发生次数')

    title = type + '类型预测示意图'

    plt.title(title)
    plt.grid(linestyle='-.', alpha=0.5)
    plt.legend()
    # plt.show()
    plt.savefig(title)

    return h


data_source = pd.read_excel('附件2：某地消防救援出警数据.xlsx')

category = ['①', '②', '③', '④', '⑤', '⑥', '⑦']

event_data = [
    data_source[data_source['事件类别'] == '①']['接警日期'],
    data_source[data_source['事件类别'] == '②']['接警日期'],
    data_source[data_source['事件类别'] == '③']['接警日期'],
    data_source[data_source['事件类别'] == '④']['接警日期'],
    data_source[data_source['事件类别'] == '⑤']['接警日期'],
    data_source[data_source['事件类别'] == '⑥']['接警日期'],
    data_source[data_source['事件类别'] == '⑦']['接警日期']
]

event_train = {
    '①': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '②': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '③': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '④': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑤': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑥': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑦': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
}

event_test = {
    '①': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '②': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '③': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '④': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑤': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑥': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0},
    '⑦': {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}
}

for i in range(7):
    for j in event_data[i]:
        event_train[category[i]][str(j).split('-')[1]] += 1
        if str(j).split('-')[0] == '2020':
            event_test[category[i]][str(j).split('-')[1]] += 1


def get_list(train_dict: dict, test_dict: dict, max_depth):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = []

    for k, v in train_dict.items():
        y.append(int(v))

    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1) / 5

    r_tree = DecisionTreeRegressor(max_depth=max_depth)

    r_tree.fit(x, y)

    h = r_tree.predict(x)

    # print(type, '类型')
    # print('真实值', end='        ')
    # for item in y:
    #     print('%.2f' % item[0], end=' ')
    # print()
    # print('预测值', max_depth, '树', end='   ')
    # for item in h:
    #     print('%.2f' % item, end=' ')
    # print()

    test = []
    for k, v in test_dict.items():
        test.append(int(v))

    return y, test, h
    # print('得分', r_tree.score(x, test))
    # print()
    # plt.figure(figsize=(10, 8), dpi=80)
    # plt.plot(x, y, label='训练集值', color='r')
    # plt.plot(x, test, label='检测集值', color='g')
    # plt.plot(x, h, label='预测值', color='b')
    # plt.xlabel('月份')
    # plt.ylabel('发生次数')
    #
    # title = type + '类型预测示意图'
    #
    # plt.title(title)
    # plt.grid(linestyle='-.', alpha=0.5)
    # plt.legend()
    # plt.show()
    # plt.savefig(title)


y0, test0, h0 = get_list(event_train[category[0]], event_test[category[0]], 4)
y1, test1, h1 = get_list(event_train[category[1]], event_test[category[1]], 4)
y2, test2, h2 = get_list(event_train[category[2]], event_test[category[2]], 4)
y3, test3, h3 = get_list(event_train[category[3]], event_test[category[3]], 4)
y4, test4, h4 = get_list(event_train[category[4]], event_test[category[4]], 4)
y5, test5, h5 = get_list(event_train[category[5]], event_test[category[5]], 4)
y6, test6, h6 = get_list(event_train[category[6]], event_test[category[6]], 4)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(60, 60), dpi=80)

ax[0][0].plot(x, y0, label='训练集值')
ax[0][0].plot(x, test0, label='检测集值')
ax[0][0].plot(x, h0, label='预测值')
ax[0][0].set_title('①类型建模图')
ax[0][0].set_xlabel('月份')
ax[0][0].set_ylabel('次数')
ax[0][0].legend()

ax[0][1].plot(x, y1, label='训练集值')
ax[0][1].plot(x, test1, label='检测集值')
ax[0][1].plot(x, h1, label='预测值')
ax[0][1].set_title('②类型建模图')
ax[0][1].set_xlabel('月份')
ax[0][1].set_ylabel('次数')
ax[0][1].legend()

ax[0][2].plot(x, y2, label='训练集值')
ax[0][2].plot(x, test2, label='检测集值')
ax[0][2].plot(x, h2, label='预测值')
ax[0][2].set_title('③类型建模图')
ax[0][2].set_xlabel('月份')
ax[0][2].set_ylabel('次数')
ax[0][2].legend()

ax[1][0].plot(x, y3, label='训练集值')
ax[1][0].plot(x, test3, label='检测集值')
ax[1][0].plot(x, h3, label='预测值')
ax[1][0].set_title('④类型建模图')
ax[1][0].set_xlabel('月份')
ax[1][0].set_ylabel('次数')
ax[1][0].legend()

ax[1][1].plot(x, y4, label='训练集值')
ax[1][1].plot(x, test4, label='检测集值')
ax[1][1].plot(x, h4, label='预测值')
ax[1][1].set_title('⑤类型建模图')
ax[1][1].set_xlabel('月份')
ax[1][1].set_ylabel('次数')
ax[1][1].legend()

ax[1][2].plot(x, y5, label='训练集值')
ax[1][2].plot(x, test5, label='检测集值')
ax[1][2].plot(x, h5, label='预测值')
ax[1][2].set_title('⑥类型建模图')
ax[1][2].set_xlabel('月份')
ax[1][2].set_ylabel('次数')
ax[1][2].legend()

ax[2][0].plot(x, y6, label='训练集值')
ax[2][0].plot(x, test6, label='检测集值')
ax[2][0].plot(x, h6, label='预测值')
ax[2][0].set_title('⑦类型建模图')
ax[2][0].set_xlabel('月份')
ax[2][0].set_ylabel('次数')
ax[2][0].legend()

# plt.savefig('图-问题3')
plt.show()


# decisionTree(event_train[category[0]], event_test[category[0]], 4, category[0])
# decisionTree(event_train[category[1]], event_test[category[1]], 4, category[1])
# decisionTree(event_train[category[2]], event_test[category[2]], 4, category[2])
# decisionTree(event_train[category[3]], event_test[category[3]], 4, category[3])
# decisionTree(event_train[category[4]], event_test[category[4]], 4, category[4])
# decisionTree(event_train[category[5]], event_test[category[5]], 4, category[5])
# decisionTree(event_train[category[6]], event_test[category[6]], 4, category[6])



