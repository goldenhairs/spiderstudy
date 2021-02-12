import numpy as np
import pandas as pd

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

score_df = pd.DataFrame(score, index=['学生A', '学生B', '学生C', '学生D'], columns=['科目1', '科目2', '科目3', '科目4', '科目5'])

# Series：带索引的行数据
series_ex1 = pd.Series(np.arange(10))
print('series_ex1:\n', series_ex1)
series_ex2 = pd.Series(np.arange(10), index=np.arange(1, 11))
print('series_ex2:\n', series_ex2)
series_ex3 = pd.Series({'red': 1000, 'green': 1001, 'blue': 1002})
print('series_ex3:\n', series_ex3)

series = score_df.iloc[1, :]
print(series.index)
print(series.values)
print(type(series))

