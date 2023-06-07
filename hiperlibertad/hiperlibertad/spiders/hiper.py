import scrapy


class HiperSpider(scrapy.Spider):
    name = "hiper"
    allowed_domains = ["hiperlibertad.com.ar"]
    start_urls = ["https://hiperlibertad.com.ar"]

    def parse(self, response):
        pass
