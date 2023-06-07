import scrapy
import json


class HiperSpider(scrapy.Spider):
    name = "hiper"
    start_urls = ["https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/tecnologia/tv-y-video?O=OrderByTopSaleDESC&_from=0&_to=23&ft&sc=1"]

    def parse(self, response):
        data = json.loads(response.text)
        products = data
        for product in products:
            name = product['productName']
            regular_price = product['items'][0]['sellers'][0]['commertialOffer']['ListPrice']
            promotional_price = product['items'][0]['sellers'][0]['commertialOffer']['Price']
            category = product['categories']
            sku = product['productId']
            url = product['link']
            stock = product['items'][0]['sellers'][0]['commertialOffer']['AvailableQuantity']
            description = product['description']

            yield {
                'name': name,
                'regular_price': regular_price,
                'promotional_price': promotional_price,
                'category': category,
                'sku': sku,
                'url': url,
                'stock': stock,
                'description': description
            }
            
