import scrapy


class XmSpider(scrapy.Spider):
    name = 'xm'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # src是伪属性，移动到就变为了src2,所以xpath要用src2表达
            src = div.xpath('./div/a/img/@src2').extract_first()
            print(src)
