import sqlite3


class QianchengPipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect("qiancheng.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "create table IF NOT EXISTS zhaopin(job_name varchar(200),company varchar(500),saray varchar(100),company_desc varchar(100))")

    def process_item(self, item, spider):
        self.cursor.execute("insert into zhaopin values('%s','%s','%s','%s')" % (
        item["job_name"], item["company"], item["saray"], item["company_desc"]))
        self.conn.commit()
        return item