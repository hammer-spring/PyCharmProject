
from pymongo import MongoClient
#2.存储为MongoDB
class saveToMongoDB(object):
    # 1.连接本地数据库服务
    def __init__(self):
        self.connection = MongoClient('localhost')
        # 2.连接本地数据库 没有会创建
        self.db = self.connection.job
        # 3.创建集合
        self.job = self.db.job51
    def process_item(self, item, spider):
        self.job.insert_one(dict(item))
    def close_spider(self, spider):
        pass
