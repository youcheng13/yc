import scrapy


class XmSpider(scrapy.Spider):
    name = 'xm'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
