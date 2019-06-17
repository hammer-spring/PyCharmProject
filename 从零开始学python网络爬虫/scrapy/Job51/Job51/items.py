import scrapy
from scrapy import Item,Field

class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = Field()
    companyname = Field()
    address = Field()
    money = Field()
    ptime = Field()
    detail =Field()
