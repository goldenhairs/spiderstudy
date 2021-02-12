import pandas as pd

# 读进来就是DataFrame
data = pd.read_csv('data/stock_day.csv')

# 删除一些列,axis是维度参数
data = data.drop(['ma5', 'ma10', 'ma20', 'v_ma10', 'v_ma20'], axis=1)

# 获取指定位置的值
print('---------获取指定位置的值---------')
print(data['open']['2018-02-26'])
print(data.loc['2018-02-26']['open'])
print(data.loc[data.index[0:4]]['open'])
print(data.iloc[1][0])
print(data.iloc[0:4]['open'])
