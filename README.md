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


