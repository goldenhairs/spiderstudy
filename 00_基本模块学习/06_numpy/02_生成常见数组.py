import numpy as np

# 生成0向量
zero = np.zeros(shape=[3, 4])
print('zero:', zero)
print('type(zero):', type(zero))
print('zero.shape:', zero.shape)          # 返回score的形状
print('zero.ndim:', zero.ndim)            # 返回向量的维度
print('zero.size:', zero.size)            # 返回向量内元素的个数
print('zero.dtype:', zero.dtype)          # 返回向量元素的类型
print('zero.itemsize:', zero.itemsize)    # 返回每个元素所占的字节数
print('----------------------------------')

# 生成1向量
one = np.ones(shape=[3, 4], dtype='int32')
print('one:', one)
print('type(one):', type(one))
print('one.shape:', one.shape)          # 返回score的形状
print('one.dtype:', one.dtype)          # 返回向量元素的类型
print('----------------------------------')


# 生成固定范围的向量
linspace_ndarray = np.linspace(0, 10, 5)    # 在闭区间内平均生成5个数
arange_ndarray = np.arange(0, 10, 5)        # 在左闭右开区间内每间隔5生成数
print('linspace_ndarray:', linspace_ndarray)
print('arange_ndarray:', arange_ndarray)
print('----------------------------------')

# 生成随机数
# 生成均匀分布随机数，low：最小值、high：最大值、size：形状
uniform = np.random.uniform(low=-1, high=1, size=10000)
# 生成正态分布随机数，loc：均值即分布的中心、scale标准差，标准差越大图形越矮胖、size：形状
np.random.normal(loc=1.75, scale=0.1, size=10000)

