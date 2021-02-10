import numpy as np

score = np.array([
    [80, 36],
    [82, 80],
    [85, 78],
    [90, 90],
    [86, 82],
    [92, 94]
])

# 矩阵化
score_mat = np.mat(score)

# print(type(score_mat))
# print(score_mat)

weights = np.array([[0.3], [0.7]])
weights_mat = np.mat(weights)

# 矩阵相乘的两种方法
target1 = np.matmul(score, weights)
target2 = np.dot(score, weights)
target3 = score @ weights
target4 = score_mat * weights_mat

