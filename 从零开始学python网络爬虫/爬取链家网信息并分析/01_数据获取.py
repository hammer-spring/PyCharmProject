import asyncio
import aiohttp
import pandas as pd
from lxml import etree


class LianjiaSpider(object):

    def __init__(self):
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
        self._data = list()

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=self._headers, timeout=3) as resp:
                    if resp.status == 200:
                        result = await resp.text()
                        return result
            except Exception as e:
                print(e.args)

    async def parse_html(self):
        for page in range(1, 77):
            url = "https://sjz.lianjia.com/zufang/pg{}/".format(page)
            print("正在爬取{}".format(url))
            html = await self.get(url)  # 获取网页内容
            html = etree.HTML(html)
            self.parse_page(html)
            print("正在存储数据....")
            data = pd.DataFrame(self._data)
            data.to_csv("lianjia.csv", encoding='utf_8_sig')  # 写入文件

    def parse_page(self, html):
        info_panel = html.xpath("//div[@class='info-panel']")
        for info in info_panel:
            region = info.xpath(".//span[@class='region']/text()")
            zone = info.xpath(".//span[@class='zone']/span/text()")
            meters = info.xpath(".//span[@class='meters']/text()")
            where = info.xpath(".//div[@class='where']/span[4]/text()")

            con = info.xpath(".//div[@class='con']/text()")
            floor = con[0]  # 楼层
            type = con[1]  # 样式

            agent = info.xpath(".//div[@class='con']/a/text()")[0]

            has = info.xpath(".//div[@class='left agency']//text()")

            price = info.xpath(".//div[@class='price']/span/text()")[0]
            price_pre = info.xpath(".//div[@class='price-pre']/text()")[0]
            look_num = info.xpath(".//div[@class='square']//span[@class='num']/text()")[0]

            one_data = {
                "region": region,
                "zone": zone,
                "meters": meters,
                "where": where,
                "louceng": floor,
                "type": type,
                "xiaoshou": agent,
                "has": has,
                "price": price,
                "price_pre": price_pre,
                "num": look_num
            }
            self._data.append(one_data)  # 添加数据

    def run(self):
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.parse_html())]
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    Lian_jia = LianjiaSpider()
    Lian_jia.run()