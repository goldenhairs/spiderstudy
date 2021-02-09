import numpy as np

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

print('score:', score)
print('type(score):', type(score))
print('score.shape:', score.shape)          # 返回score的形状
print('score.ndim:', score.ndim)            # 返回向量的维度
print('score.size:', score.size)            # 返回向量内元素的个数
print('score.dtype:', score.dtype)          # 返回向量元素的类型
print('score.itemsize:', score.itemsize)    # 返回每个元素所占的字节数

