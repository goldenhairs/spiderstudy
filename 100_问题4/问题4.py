import pandas

data = pandas.read_excel('附件2：某地消防救援出警数据.xlsx')
area_data = pandas.read_excel('附件1：各区域的人口、面积.xlsx')

print(area_data)

# place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P']

# for i in place:
#     print(data[data['事件所在的区域'] == i])
