import pandas as pd

# 读进来就是DataFrame
data = pd.read_csv('data/stock_day.csv')

# 删除一些列,axis是维度参数
data = data.drop(['ma5', 'ma10', 'ma20', 'v_ma10', 'v_ma20'], axis=1)

data['open'] = 100
print(data)

data.iloc[1, 0] = 160
print(data)
