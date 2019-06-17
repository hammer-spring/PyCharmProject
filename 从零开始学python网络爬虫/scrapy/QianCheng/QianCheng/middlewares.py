from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOptions
import time
from scrapy.http import HtmlResponse
class SeleniumMiddlewares(object):
    def __init__(self):
        self.options = FOptions()
        # self.options.add_argument("-headless")
        self.browser = webdriver.Firefox(executable_path="/home/hello/Downloads/geckodriver",
                                         firefox_options=self.options)

    def process_request(self, request, spider):
        if int(request.meta['page']) == 0:
            self.browser.get(request.url)
            input_name = self.browser.find_element_by_xpath('//*[@id="kwdselectid"]')
            input_name.click()
            input_name.send_keys('python')
            btn_seacher = self.browser.find_element_by_xpath('//*[@id="supp"]/div[1]/div/div[1]/button')
            btn_seacher.click()
            time.sleep(3)

        if int(request.meta['page']) == 1:
            self.browser.get(request.url)
            time.sleep(3)
        if int(request.meta['page']) == 2:
            self.browser.get(request.url)
            next_page = self.browser.find_element_by_xpath('//a[contains(text(),"下一页")]')
            next_page.click()

        return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding="utf-8",
                            request=request)