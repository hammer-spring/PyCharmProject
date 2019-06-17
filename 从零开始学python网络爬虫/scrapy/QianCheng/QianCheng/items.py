import scrapy

class QianchengItem(scrapy.Item):

    job_name = scrapy.Field()
    company= scrapy.Field()
    saray= scrapy.Field()
    company_desc= scrapy.Field()