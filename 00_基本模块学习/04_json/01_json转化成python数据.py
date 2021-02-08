import json

# 1、json字符串
json_str = """[
  {
    "id": "1",
    "name": "菜鸟教程",
    "url": "www.runoob.com"
  },
  {
    "id": "2",
    "name": "菜鸟工具",
    "url": "c.runoob.com"
  },
  {
    "id": "3",
    "name": "Google",
    "url": "www.google.com"
  }
]
"""
# 2、转换成python数据
rs = json.loads(json_str)
print(type(rs))
