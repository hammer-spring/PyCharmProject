BOT_NAME = 'QianCheng'
SPIDER_MODULES = ['QianCheng.spiders']
NEWSPIDER_MODULE = 'QianCheng.spiders'
ROBOTSTXT_OBEY = False
DOWNLOADER_MIDDLEWARES = {
   'QianCheng.middlewares.SeleniumMiddlewares': 543,
}
ITEM_PIPELINES = {
   'QianCheng.pipelines.QianchengPipeline': 300,
}