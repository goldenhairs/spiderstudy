import numpy as np
import pandas as pd

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

# pd.DataFrame()将二维数组转换成DataFrame，index行索引，columns列索引
score_df = pd.DataFrame(score, index=['学生A', '学生B', '学生C', '学生D'], columns=['科目1', '科目2', '科目3', '科目4', '科目5'])

print('score_df:', score_df)

# DataFrame的属性
print('score_df.shape:', score_df.shape)        # 形状
print('score_df.index:', score_df.index)        # 行索引
print('score_df.columns:', score_df.columns)    # 列索引
print('score_df.values:', score_df.values)      # 对应的ndarray
print('score_df.T:', score_df.T)                # 转置
print('score_df.head():', score_df.head())      # 不指定参数时返回前五条数据
print('score_df.tail():', score_df.tail())      # 不指定参数时返回后五条数据


