import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'id' : 101,
    '名称' : 'Python语言编程案例课堂',
    '价格' : '59元'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['名称']: ", data2['名称'])
print ("data2['价格']: ", data2['价格'])

