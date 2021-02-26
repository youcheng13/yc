import scrapy


class A1Spider(scrapy.Spider):
    name = 'a1'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
