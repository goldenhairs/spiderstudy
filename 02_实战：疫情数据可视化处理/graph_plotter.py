import matplotlib.pyplot as plt


class GraphPlotter(object):
    def __init__(self, all_confirmed_count, country_name, time):
        self.all_confirmed_count = all_confirmed_count
        self.country_name = country_name
        self.time = time
        self.time_label = ['{}月{}日'.format(i % 10000 // 100, i // 100) for i in time]

    def draw(self, figsize=(10, 8), dpi=80):
        fig = plt.subplots(figsize=figsize, dpi=dpi)

        usa_line, = plt.plot([], [], color='r', marker='o')
        uk_line, = plt.plot([], [], color='g', marker='o')
        fra_line, = plt.plot([], [], color='b', marker='o')
        rus_line, = plt.plot([], [], color='y', marker='o')
        chn_line, = plt.plot([], [], color='c', marker='o')
        ind_line, = plt.plot([], [], color='m', marker='o')

        ylim = self.__get_now_ylim(0)
        plt.ylim(ylim[0], ylim[1])

        x_range = 10
        plt.xlim(0, x_range)

        x = list(range(len(self.time)))
        plt.xticks(x[0:x_range], self.time_label[0:x_range])
        plt.xlabel('2020年')

        line_range = 6

        plt.title('中国新冠疫情新增病例动态图展示')

        # 创建动画
        animation = FuncAnimation(fig, self.__update, frames=x, repeat=False, interval=100)

        plt.show()

    def __get_now_ylim(self, index):
        list_count = []
        for i in self.all_confirmed_count:
            list_count.append(i[index])
        min_lim = min(list_count) * 0.7
        max_lim = max(list_count) * 1.3
        return min_lim, max_lim

    def __update(self):
        pass
