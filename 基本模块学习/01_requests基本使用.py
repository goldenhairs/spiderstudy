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
