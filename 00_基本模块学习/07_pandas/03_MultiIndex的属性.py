import numpy as np
import pandas as pd

score = np.array([
    [80, 89, 86, 67, 79],
    [78, 97, 89, 67, 81],
    [90, 94, 78, 67, 74],
    [91, 91, 90, 67, 69]
])

score_df = pd.DataFrame(score, index=['学生A', '学生B', '学生C', '学生D'], columns=['科目1', '科目2', '科目3', '科目4', '科目5'])

score_df_reset5 = score_df.set_index(['科目1', '科目2'])

multi_index = score_df_reset5.index

print('multi_index.names:', multi_index.names)
print('multi_index.values:', multi_index.values)
