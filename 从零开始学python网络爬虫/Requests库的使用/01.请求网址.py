import requests
res = requests.get("http://baidu.com")
print(res)
print(res.text)