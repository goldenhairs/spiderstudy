import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.array([
    [1],
    [2],
    [3]
])
d = np.array([
    [4],
    [5],
    [6]
])

# 水平拼接
h1 = np.hstack((a, b))
h2 = np.hstack((c, d))

# 竖直拼接
v1 = np.vstack((a, b))
v2 = np.vstack((c, d))

# 指定维度拼接
c = np.concatenate((a, b), axis=0)
