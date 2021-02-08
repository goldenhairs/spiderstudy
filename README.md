# spiderstudy

## 一、网络爬虫的定义和作用
- 网络爬虫的定义：网络爬虫就是模拟客户端发送网络请求，获取响应数据，一种按照一定的规则，自动地抓取万维网信息的程序或脚本   
- 网络爬虫的作用：从网络上获取我们需要的数据

## 二、requests
### 1、requests
requests是一个简单的python http请求库，用于发送请求获取响应数据
### 2、requests安装
`pip install requests`
### 3、requests基本使用
步骤：导入模块 > 发送和get请求，获取响应 > 从响应中获取数据
```python
import requests

# 发送请求、获取相应
response = requests.get('https://www.baidu.com')

# 获取相应数据
# 方法一
response.encoding = 'utf8'  # 指定编码格式，防止乱码
result1 = response.text  # 获取相应内容
print(result1)

# 方法二
result2 = response.content.decode()  # content获取的是二进制编码，使用decode()方法解码，decode方法默认编码格式是utf8
print(result2)
```

## 三、BeautifulSoup
### 1、BeautifulSoup
BeautifulSoup可以从html或xml提取数据
### 2、BeautifulSoup安装
`pip install bs4`   
`pip install lxml`
### 3、BeautifulSoup使用
> 方法介绍：
> - find(self, name=None, attrs={}, recursive=True, text=None, **kwargs)：
>   - name：标签名
>   - attrs：属性字典
>   - recursive：是否递归查找，默认为True
>   - text：根据文本内容进行查找
>   - return：返回查询到的第一个对象
> - find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)：
>   - 用法同find()
>   - limit：限定查询多少条数据，如果不指定就查询所有

> Tag对象：
> - find()或find_all()方法返回的对象
> - 属性：
>   - name：获取标签名称
>   - attrs：获取标签所有属性的键和值
>   - text：获取标签的文本字符串
```python
from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>example</title>
    </head>
    <body>
        <p class="title>
            <b>example p</b>
        </p>
        <p class="content">
            <a href="http://www.kewencoder.cn" class="url" id="url1">科文码农</a>
            <a href="https://www.baidu.com" class="url" id="url2">百度</a>
            <a href="https://www.csdn.net" class="url" id="url1">CSDN</a>
        </p>
    </body>
</html>
'''

"""---------------根据标签查找---------------"""
# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'lxml')

# 查找title标签
title = soup.find(name='title')
# print('title:', title)

# 查找a标签
a = soup.find(name='a')
# print('a:', a)
a_s = soup.find_all(name='a')
# print('a_x:', a_s)


"""---------------根据属性查找---------------"""
url1 = soup.find(attrs={'id': 'url1'})
# print(url1)

"""---------------根据文本内容查找---------------"""
kwcoder = soup.find(text='科文码农')
# print(kwcoder)
```


## 四、re
### 1、re   
re：正则模块，正则表达式（Regular Expression），是一种被用于从文本中检索符合某些特定模式的文本。
### 2、基本内容
#### 1）基本匹配
"Cat" => The cat sat on the ***Cat***.    
"cat" => The ***cat*** sat on the Cat.
#### 2）元字符
|元字符|描述|
|:---:|---|
|.|匹配除换行符以外的任意单字符。|
|[]|字符类，匹配方括号中包含的任意字符。|
|[^]|否定字符类，匹配方括号中不包含的任意字符。|
|*|匹配前面的子表达式零次或多次。|
|+|匹配前面的子表达式一次或多次。|
|?|匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。|
|{n,m}|花括号，匹配前面字符至少n次，但不超过m次|
|(xyz)|字符组，按照确切的额顺序匹配字符xyz|
|&#124;|分支结构，匹配符号之前的字符或后面的字符|
|\\|转义字符，可以还原元字符原来的含义|
|^|匹配行的开始|
|\$|匹配行的结束|
- .   
".ar" => The ***car*** ***par***ked in the ***gar***age.
- []   
"\[Tt\]he" => ***The*** car parked in ***the*** garage.  
但是"."用在此处就表示匹配"."   
"ar\[.\]" => A garage is a good place to park a c***ar.***
- \[^\]
"\[^c\]ar" => The car ***par***ked in the ***gar***age.
- \*
"\[a-z\]\*" => T***he car parked in the garage*** #21.  （表示匹配所有的小写字符）
> .* 可以表示匹配任意字符
- \+
"c.+t" => The fat ***cat sat on t***he wall.     （一个小写字母 c，后跟任意数量的字符，后跟小写字母 t。）
- ?   
观察差异：   
"[T]he" => ***The*** car is parked in ***the*** garage.   
"[T]?he" => ***The*** car is parked in t***he*** garage.
- {}
"[0-9]{2,3}" => The number was 9.***9997*** but we rounded it off to ***10***.0.
匹配 2 个或更多个数字。如果我们也删除逗号，则正则表达式 [0-9]{2}，表示：匹配正好为 2 位数的数字。   
"[0-9]{2,}" => The number was 9.***9997*** but we rounded it off to ***10***.0.   
"[0-9]{2}" => The number was 9.***99***97 but we rounded it off to ***10***.0.
- ()   |   
"(c|p)ar" => The ***car*** is ***par***ked in the garage.
- ^   
观察：   
  "(c|p)ar" => The ***car*** is ***par***ked in the garage.   
"^(c|p)ar" => The ***car*** is parked in the garage.
> 只对开头进行匹配
- \$   
观察：   
"(at\.)" => The fat c***at.*** s***at.*** on the m***at.***   
"(at\.)$" => The fat cat. sat. on the m***at.***
> 只对末尾进行匹配
#### 3）简写字符集
|简写|描述|
|:---:|---|
|.|匹配除换行符以外的任意字符|
|\w|匹配所有非字母和数字的字符：[a-zA-Z0-9_]|
|\W|匹配非字母和数字的字符：[^\w]|
|\d|匹配数字：[0-9]|
|\D|匹配非数字：[^\d]|
|\s|匹配空格符：[\t\n\f\r\p{Z}]|
|\S|匹配非空格符：[^\s]|




## 五、json
### 1、json   
json模块是python自带的模块，可用于python数据格式和json之间的相互转化
### 2、json与python数据类型的对应关系
|JSON|Python|
|:---:|---|
|object|dict|
|array|list|
|string|str|
|number(int)|int, long|
|number(real)|float|
|true|True|
|false|False|
|null|None|
### 3、json的使用
> 基本方法   
> loads()    load()   
> dumps()    dump()


## 六、matplotlib
### 1、matplotlib
### 2、matplotlib三层结构
#### 1）容器层
- 画板层（Canvas）
- 画布层：`plt.figure(figsize, dpi)`   
其中`figsize`是画布的大小，dpi是画布的像素
- 绘图区、坐标系：`figure, axes = plt.subplots(nrows, ncols, figsize, dpi)`   
`figure`是画布，`axes`是绘图区，如果分割成多个绘图区，则使用`axes[index]`的方式去对每个绘图区做不同的设置
#### 2）辅助显示层
- 修改x，y轴刻度：`plt.xticks(ticks, labels)` `plt.yticks(ticks, labels)`   
`ticks`是当前刻度位置，`labels`是需要设置的标签，刻度位置和标签需要一一对应   
如果使用了多个绘图区，则需要这样替换：   
```python
axes[0].set_xticks(ticks)
axes[0].set_xticklabels(labels)
```
- 添加描述信息：   
`plt.xlabel()` `plt.ylabel` `axes[0].set_xlabel()` `axes[0].set_ylabel()`   
`plt.title()` `axes[0].set_title()`   
- 添加网格线：`plt.grid()`（多个绘图区同理）   
常用参数列表：   
`color`   
`linestyle`   
`linewidth`   
`alpha`：透明度
- 显示图例：`plt.legend()`（多个绘图区同理）
#### 3）图像层(colors为通用属性)
- 折线图   
`plt.plot(scalex, scaley)`
- 散点图   
`plt.scatter(x, y)`
- 柱状图   
`plt.bar(x, y, width, align=center, **kwargs)`   
`plt.barh(x, y, width, align=center, **kwargs)`   
x为横坐标的刻度，y为纵坐标，width为柱子的宽度
- 直方图   
`plt.hist(x, bins=None, density=None, **kwargs)`   
x是数据，bins是组数，density为True时纵坐标显示频率
- 饼图   
`plt.pie(x, labels, autopct)`   
`x`为数据，`labels`为数据对应的标题，`autopct`的值通常为`%1.2f%%`，是百分比例的格式
### 3、常用子模块及其方法
#### 1）matplotlib.pyplot
用于画基本的图，如折线图、散点图、柱状图、直方图、饼图等   

|图形|方法|参数|
|:---:|---|---|
|折线图|plot(x, y)|横轴数据，纵轴数据|
|散点图|scatter(x, y)|横轴数据，纵轴数据|
|柱状图|bar(x, y)|横轴数据，纵轴数据|
|直方图|hist(x, bins, density)|数据，组数，是否用频率展示|
|饼图|pie(x, labels, autopct)|数据，每个数据对应的标签，显示百分比格式（通常为%1.2f%%）|

使用步骤：
```python
import matplotlib.pyplot as plt

# 准备数据
x = []
y = []

# 准备画布
plt.figure(figsize=(10, 8), dpi=80)

# 绘制折线图（或其他图形）
plt.plot(x, y)

# 添加辅助层
# 修改横坐标
plt.xticks(x, x)
plt.xlabel('')

plt.yticks(y)
plt.ylabel('')
# 添加标题
plt.title('')
# 添加网格线
plt.grid(linestyle='-.', alpha=0.5)

# 展示数据
plt.show()
```

建立多个绘图区：
```python
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10), dpi=200)

ax[0].plot(x, y1, color='b', label='中国')
ax[1].plot(x, y2, color='r', label='美国')

ax[0].legend()
ax[1].legend()

time_label = ''
ax[0].set_xticks(x)
ax[0].set_xticklabels(time_label)
ax[1].set_xticks(x)
ax[1].set_xticklabels(time_label)

ax[0].set_ylabel('')
ax[1].set_ylabel('')

ax[0].set_xlabel('')
ax[1].set_xlabel('')

ax[0].grid(linestyle='-.', alpha=0.5)
ax[1].grid(linestyle='-.', alpha=0.5)

ax[0].set_title('')
ax[1].set_title('')

plt.show()
```

#### 2）matplotlib.animation.FuncAnimation
用于绘制动画

常用属性
- `fig`：画布
- `func`：动画更新的方法
- `frames`：动画中每帧的数据，遍历frames，每次传入一条数据到func方法中，改变图形，产生一个动画画面
- `init_func`：初始方法，只会在最开始的时候执行一次
- `repeat`：动画是否重复执行
- `interval`：每帧时间间隔的毫秒数，默认值200

常用方法   
`save('文件路径.mp4', fps)` 保存为mp4视频文件

#### 3)加载世界地理信息
```python
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
```

