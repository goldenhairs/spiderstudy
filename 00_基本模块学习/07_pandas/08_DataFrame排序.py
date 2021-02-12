import pandas as pd

# 读进来就是DataFrame
data = pd.read_csv('data/stock_day.csv')

# 删除一些列,axis是维度参数
data = data.drop(['ma5', 'ma10', 'ma20', 'v_ma10', 'v_ma20'], axis=1)

# 对内容进行排序，第一个参数是指定排序的列，可以通过列表指定多列；ascending是否使用升序
data.sort_values('high', ascending=True)
print(data)

# 对索引排序(即对Series排序)
data['high'].sort_index(ascending=True)
