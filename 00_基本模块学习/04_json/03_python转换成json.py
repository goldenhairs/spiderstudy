import json

python_str = [{'id': '1', 'name': '菜鸟教程', 'url': 'www.runoob.com'}, {'id': '2', 'name': '菜鸟工具', 'url': 'c.runoob.com'}, {'id': '3', 'name': 'Google', 'url': 'www.google.com'}]

# ensure_ascii：是否使用阿斯克码，默认为True
json_str = json.dumps(python_str, ensure_ascii=False)
print(type(json_str))
