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


