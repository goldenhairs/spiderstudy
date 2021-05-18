import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from get_plot_data import GetPlotData

corona_df = pd.read_csv('data/疫情数据.csv', index_col='国家')

# 准备日期数据
columns_ndarray = corona_df.columns.values
x = list(range(len(columns_ndarray)))
x_labels = ['{}月{}日'.format(int(i) % 10000 // 100, int(i) % 100) for i in columns_ndarray]

fig = plt.figure(figsize=(10, 6), dpi=80)

fir_line, = plt.plot([], [], marker='o')
sec_line, = plt.plot([], [], marker='o')
thr_line, = plt.plot([], [], marker='o')
for_line, = plt.plot([], [], marker='o')
fit_line, = plt.plot([], [], marker='o')

x_range = 10
plt.xlim(0, x_range)
plt.xticks(ticks=x[0:x_range], labels=x_labels[0:x_range])

line_range = 6

g = GetPlotData()


def update(i):
    start = 0 if i - line_range < 0 else i - line_range
    end = i + 1
    date, country, data, color = g.get_top_of_day(i, corona_df)

    fir_line.set_data(x[start:end], data[0])
    sec_line.set_data(x[start:end], data[1])
    thr_line.set_data(x[start:end], data[2])
    for_line.set_data(x[start:end], data[3])
    fit_line.set_data(x[start:end], data[4])

    colors = []
    for index in country:
        colors.append(color[index])

    fir_line.set_color(colors[0])
    sec_line.set_color(colors[1])
    thr_line.set_color(colors[2])
    for_line.set_color(colors[3])
    fit_line.set_color(colors[4])

    if i > line_range:
        x_end = i + (x_range - line_range) if (x_range - line_range) < len(x) else len(x)
        plt.xlim(start, x_end)
        plt.xticks(ticks=x[start:end], labels=x_labels[start:end])
    plt.ylim(min(data) * 0.7, max(data) * 1.3)
    plt.xlabel(date // 10000)

    return fir_line, sec_line, thr_line, for_line, fit_line


plt.legend()

animation = FuncAnimation(fig=fig, func=update, repeat=False, interval=200)

plt.show()
