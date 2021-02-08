from cartopy.crs import PlateCarree
from cartopy.io import shapereader
import matplotlib.pyplot as plt
from matplotlib.cm import YlOrRd
from matplotlib.colors import rgb2hex
from matplotlib.colors import Normalize
from matplotlib.colorbar import ColorbarBase

# 获取文件路径信息
"""
    resolution：解析度（分辨率），10m，50m，110m
    category：physical地理位置信息，cultural地理及国家信息
    name：coastline海岸线，admin_0_countries国家边界线和国家名称信息
"""
filename = shapereader.natural_earth(resolution='110m', category='cultural', name='admin_0_countries')
# 创建地理文件阅读器对象
reader = shapereader.Reader(filename)
# 获取数据
countries = reader.records()

# 创建绘图区
"""
    subplot_kw：是一个字典参数，用于制定绘图区
"""
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': PlateCarree()})


"""
add_geometries(geoms, crs, **kwargs)

geoms：集合图形的集合
crs：cartopy.crs模块中提供地图形状
facecolor：前景色，集合形状内部的填充色
edgecolor：边界的颜色，集合形状边缘线的颜色
"""
max_value = 200
for i, country in enumerate(countries):
    # 可以根据给定的参数生成热度颜色，为rgba格式
    """
    YlOrRd(value)
    参数：
    value : 0~1之间的值
    """
    rgba = YlOrRd(i / max_value)
    # 将rgba格式转换成#rrggbb格式的方法
    """
    rgb2hex(c, keep_alpha=False)
    c：rgba元组
    keep_alpha：是否保留透明度，若保留则返回#rrggbbaa
    """
    color = rgb2hex(rgba)
    ax.add_geometries(geoms=[country.geometry], crs=PlateCarree(), facecolor=color, edgecolor='r')


# 添加颜色条
# 添加新绘图区：add_axes(rect)，返回一个cax
"""
rect：用于指定新会图区位置和宽高，形式[left, bottom, width, height]
left：左边界举例最左侧的位置，范围[0, 1]
bottom：下边界距离最底部的位置，范围[0, 1]
width：宽度[0, 1]
height：[0, 1]
"""
cax = fig.add_axes([0.95, 0.3, 0.02, 0.4])
# 创建统一规划器：Normalize(vmin vmax)
norm = Normalize(vmin=0, vmax=max_value)
# print(norm(50))  # 0.25——按照比例转换

# 创建颜色调对象
"""
ColorbarBase(ax, cmap=None, norm=None, label)
ax：指定颜色条添加到哪个坐标系上
cmap：Colormap对象，一般为plt.m.YlOrRd
norm：Normalize对象，把数据转换为0~1之间
label：颜色条名称
"""
ColorbarBase(cax, cmap=YlOrRd, norm=norm, label='颜色条')


plt.show()

