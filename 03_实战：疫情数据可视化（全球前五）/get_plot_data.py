class GetPlotData:
    def __init__(self):
        self.unused_color = ['r', 'gray', 'darkorange', 'greenyellow', 'b', 'pink', 'k', 'y', 'yellow', 'midnightblue', 'g', 'm', 'darkred']
        self.pre_color: dict = {}
        self.current_color: dict = {}

    def get_top_of_day(self, i, corona_df):
        """
        获取当日现存确诊人数排名前五的数据
        :param corona_df:
        :param i: 第几天
        :return: 日期、国家、数据
        """
        self.current_color: dict = {}
        data_of_day = corona_df.iloc[:, i:i + 1]
        columns_name = data_of_day.columns.values[0]
        data_of_day = data_of_day.sort_values(columns_name, ascending=False).head()
        date = int(data_of_day.columns.values[0])
        country = data_of_day.index.values
        data = data_of_day.values.reshape(1, -1)[0]

        if 0 == len(self.pre_color.items()):
            for index in range(5):
                country_name = country[index]
                color = self.unused_color[0]
                self.current_color[country_name] = color
                self.unused_color.remove(color)
        else:
            for index in self.pre_color.keys():
                if index not in country:
                    self.unused_color.append(self.pre_color[index])
            for index in country:
                if index not in self.pre_color.keys():
                    color = self.unused_color[0]
                    self.current_color[index] = color
                    self.unused_color.remove(color)
                else:
                    self.current_color[index] = self.pre_color[index]

        self.pre_color = self.current_color

        return date, country, data, self.current_color
