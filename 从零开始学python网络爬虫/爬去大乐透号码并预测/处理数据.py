import os

with open (r"D:\PyCharm\PyCharmProject\从零开始学python网络爬虫\爬去大乐透号码并预测\data_recent.csv",'r',encoding='utf-8') as f:
    with open('.\simple_data.csv','a') as file:
        for line in f:
            file.write(line[:26]+'\n')
f.close()
file.close()

