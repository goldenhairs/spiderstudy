import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. 准备数据
columns = ['日期', '中国', '美国', '意大利']
datas = [
    [20200327, 385.00, 189.00, 589.00],
    [20200328, 478.00, 122.00, 1434.00],
    [20200329, 337.00, 1674.00, 646.00],
    [20200330, 288.00, 2200.00, 1590.00],
    [20200331, 190.00, 2045.00, 1109.00],
    [20200401, 195.00, 1524.00, 1118.00],
    [20200402, 175.00, 557.00, 1431.00],
    [20200403, 199.00, 781.00, 1480.00],
    [20200404, 226.00, 4880.00, 1238.00],
    [20200405, 138.00, 2614.00, 819.00]
]

# 2. 创建画布，通过这种方式获取绘图区，可以在每一次绘图前清空绘图区，以增加执行速度
fig, ax = plt.subplots(figsize=(10, 5))


# 3. 实现动画更新方法
def update(row):
    # 清空绘图区
    ax.clear()
    ax.barh(columns[1:], row[1:], height=0.5, color=['r', 'g', 'b'])
    # transform=ax.transAxes可以将坐标系转换成1*1，可以是text的位置固定
    ax.text(0.8, 0.3, row[0], transform=ax.transAxes, fontsize=20)


# 4. 展示动画
animation = FuncAnimation(fig, update, frames=datas, repeat=False)

# 5. 展示
plt.show()
