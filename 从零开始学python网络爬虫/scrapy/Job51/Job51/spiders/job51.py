from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from ..items import Job51Item
from scrapy.http import Request
import  re
from copy import deepcopy


class Job51(CrawlSpider):
    name = 'job51'#与建立的py文件名相同
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    start_urls = [url]
    #可以不用去设置settings文件，直接指定管道文件
    # custom_settings = {
    #     'ITEM_PIPELINES' : {
    #     # 'job51.pipelines.Job51Pipeline': 300,
    #     'job51.pipelines.saveToJson': 310
    #     #'job51.pipelines.saveToMongoDB': 320
    # }
    # }


    # 定义一个计数变量
    times = 0
    def parse(self, response):
        self.times+=1
        #response是下载器下载的网页内容
        selector = Selector(response)#创建selector对象

        item=Job51Item()

        parent = selector.xpath('//div[@id="resultList"]//div[@class="el"]')
        #print(parent)
        for each in parent:
        	#获取职位信息
            jobname = each.xpath('./p/span/a/@title').extract()
            jobsrc = each.xpath('./p/span/a/@href').extract()[0]
            companyname = each.xpath('./span[1]/a/text()').extract()
            address = each.xpath('./span[2]/text()').extract()
            money = each.xpath('./span[3]/text()').extract()
            ptime = each.xpath('./span[4]/text()').extract()
            #print(jobname,companyname,address,money,ptime)

            if money:
                money=money[0]
            else:
                money='面谈'
            item['jobname']=jobname[0]
            item['companyname']=companyname[0]
            item['address']=address[0]
            item['money']=money
            item['ptime']=ptime[0]

            #因为每一条都在循环内
            yield Request(jobsrc,meta={'front_item':deepcopy(item)},callback=self.parse_detail,dont_filter=True)


#实现多页爬取
        #寻找下一页的链接
        next = selector.xpath('//div[@class="dw_page"]//ul//li[@class="bk"][2]/a/@href')[0].extract()
        print("下一页：",next)



        #提交请求
        if self.times<4:
            yield Request(next,callback=self.parse)

    #爬取详情页的函数
    def parse_detail(self,response):
        item = response.meta['front_item']
        selector = Selector(response)
        #提取信息
        div = selector.xpath('//div[@class="bmsg job_msg inbox"]')
        if div:
            div=div[0]
        else:
            return
        #提取所有文本
        #txt = div.xpath('./p/font/font/text()').extract()
        txt = div.xpath('string(.)').extract()[0]
        #print(txt)
        #使用正则去除空格
        reg = re.compile('\S*',re.S)
        #提取所有非空白符
        result = re.findall(reg,txt)

        datalist = []
        for i in result:
            if i :
                datalist.append(i)
        #print(datalist)
        #给item
        item['detail']=str(datalist)
        yield item
