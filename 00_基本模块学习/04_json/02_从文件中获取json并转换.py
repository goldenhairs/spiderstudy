import json

with open('data/test.json', encoding='utf8') as fp:
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
