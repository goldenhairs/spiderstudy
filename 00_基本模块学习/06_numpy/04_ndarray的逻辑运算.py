import numpy as np

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

# 将大于90的标记为True，其他为False
flags = score > 90
print('flags:', flags)

# 取出大于90的数字
score_gt_ninety = score[score > 90]
print('score_gt_ninety', score_gt_ninety)

# 判断score中是否都大于90/是否存在大于90的数
all_gt_ninety = np.all(score > 90)    # True
any_gt_ninety = np.any(score > 90)    # False


