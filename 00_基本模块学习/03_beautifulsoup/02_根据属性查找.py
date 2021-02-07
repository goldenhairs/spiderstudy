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
# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'lxml')

url1 = soup.find(attrs={'id': 'url1'})
print(url1)
