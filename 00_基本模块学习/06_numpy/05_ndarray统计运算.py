import numpy as np

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

# 获取所有数中最大的
max_of_all = score.max()

# 按列获取最大值
max_of_col = score.max(axis=0)
# 按行获取最大值
max_of_row = score.max(axis=1)
# 其他解释：axis=0指的是shape元组的第一个数字

# 获取最大值的索引位置
arg = score.argmax(axis=0)
