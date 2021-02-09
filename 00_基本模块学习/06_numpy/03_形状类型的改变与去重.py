import numpy as np

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

# 将原向量打成一维向量且内存不共享
oned = score.flatten()
print(oned)
print('-----------------------')

# 返回新的向量，原对象不改变，但共享地址
new_shaped = score.reshape(2, -1)
print(new_shaped)
print('-----------------------')

# 不返回新的对象
score.resize([2, 10])
print(score)
score.resize([4, 5])
print('-----------------------')

# 数组转置
score_T = score.T
print(score_T)
print('-----------------------')

# 改变类型
score.astype(dtype=str)

# 去重
# 法一
unique_score = np.unique(score)
print(unique_score)
# 法二
unique_score = score.flatten()
unique_score = set(unique_score)

