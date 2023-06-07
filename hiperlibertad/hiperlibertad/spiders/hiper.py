import scrapy
import json


class HiperSpider(scrapy.Spider):
    name = "hiper"
    base_url = 'https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/hogar/muebles-de-interior'
    start_urls = [f'{base_url}?O=OrderByTopSaleDESC&_from=0&_to=23']

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
                'Nombre': name,
                'Precio regular': regular_price,
                'Precio promocional': promotional_price,
                'Categoría/s': category,
                'SKU': sku,
                'URL': url,
                'Stock': stock,
                'Descripción': description
            }
        
        # Exctract current page range from the URL
        current_page_from = int(response.url.split('_from=')[1].split('&')[0])
        current_page_to = int(response.url.split('_to=')[1])
        
        # Calculate the next page range
        next_page_from = current_page_from + 24
        next_page_to = current_page_to + 24

        # Construct URL for the next page
        next_page = f"{self.base_url}?O=OrderByTopSaleDESC&_from={next_page_from}&_to={next_page_to}"
        yield scrapy.Request(next_page, callback=self.parse)