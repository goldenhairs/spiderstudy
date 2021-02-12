import numpy as np
import pandas as pd

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

score_df = pd.DataFrame(score, index=['学生A', '学生B', '学生C', '学生D'], columns=['科目1', '科目2', '科目3', '科目4', '科目5'])
print('score_df:\n', score_df)

# 重设索引：恢复默认索引，即0，1，2，但不会删除原有索引
score_df_reset1 = score_df.reset_index()
print('score_df_reset1:\n', score_df_reset1)

# 删除原有索引
score_df_reset2 = score_df.reset_index(drop=True)
print('score_df_reset2:\n', score_df_reset2)

# 设置新索引
score_df_reset3 = score_df.set_index('科目1', drop=False)
score_df_reset4 = score_df.set_index('科目1', drop=True)
print('score_df_reset3:\n', score_df_reset3)
print('score_df_reset4:\n', score_df_reset4)

# 设置多索引
score_df_reset5 = score_df.set_index(['科目1', '科目2'])
print('score_df_reset5:\n', score_df_reset5)

# 获取索引(MultiIndex是多级或分层索引对象)
print('score_df_reset4.index:\n', score_df_reset4.index)
print('score_df_reset5.index:\n', score_df_reset5.index)
