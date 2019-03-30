import json

# Python 字典类型转换为 JSON 对象
data = {
    'id' : 101,
    '名称' : 'book',
    '价格' : '59元'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
