import scrapy
from scrapy import Request
from ..items import QianchengItem
import re


class ExampleSpider(scrapy.Spider):
    name = '51job'

    def start_requests(self):
        url_str = 'https://www.51job.com/zhengzhou/'
        yield Request(url=url_str, callback=self.parse, dont_filter=True, meta={'page': '0'})

    def parse(self, response):
        contents = response.xpath('//div[@class = "el"]')
        for i in contents:
            urls = i.xpath('p/span[1]/a[@href]/@href').extract()
            for urll in urls:
                yield Request(url=urll, callback=self.parse_dail, meta={'page': '1'})
        if re.search(r'search', response.url):
            yield Request(url=response.url, callback=self.parse, meta={'page': '2'})  # 标记page,再中间件中识别并进行翻页操作

    def parse_dail(self, response):
        job_name = response.xpath('//h1[@title]/@title').extract()
        company = response.xpath('//p[@class="cname"]/a[@title]/@title').extract()
        saray = response.xpath('//div[@class="cn"]/strong/text()').extract()
        company_desc = response.xpath('//div[@class="tmsg inbox"]/text()').extract()
        qianchengs = QianchengItem()
        qianchengs['job_name'] = ''.join(job_name)
        qianchengs['company'] = ''.join(company)
        qianchengs['saray'] = ''.join(saray)
        qianchengs['company_desc'] = ''.join(company_desc).strip()
        yield qianchengs