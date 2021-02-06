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

