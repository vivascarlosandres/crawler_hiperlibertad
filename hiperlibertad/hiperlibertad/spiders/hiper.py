import scrapy
import json
from scrapy.selector import Selector


class HiperSpider(scrapy.Spider):
    name = "hiper"
    base_url = 'https://www.hiperlibertad.com.ar/api/catalog_system/pub/products/search/hogar/muebles-de-interior'
    start_urls = [f'{base_url}?O=OrderByTopSaleDESC&_from=0&_to=23']
    sc_value = '1' # Default value
    
    def __init__(self, sc_value='1', *args, **kwargs):
        super(HiperSpider, self).__init__(*args, **kwargs)
        self.sc_value = sc_value
        
    def start_requests(self):
        url = f'{self.base_url}?O=OrderByTopSaleDESC&_from=0&_to=23&sc={self.sc_value}'
        yield scrapy.Request(url, self.parse)

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
            
            # Extract description text without HTML tags
            description_html = product['description']
            description_text = Selector(text=description_html).xpath('//text()').getall()
            description = ' '.join(description_text).strip()

            yield {
                'Nombre': name,
                'Precio regular': regular_price,
                'Precio promocional': promotional_price,
                'Categoria/s': category,
                'SKU': sku,
                'URL': url,
                'Stock': stock,
                'Descripcion': description
            }
            
            # Check if there are more products on the current page
            has_more_products = len(data) > 0

            # Extract current page range from the URL
            current_page_from = int(response.url.split('_from=')[1].split('&')[0])
            current_page_to = int(response.url.split('_to=')[1].split('&')[0])

            # Calculate the next page range
            next_page_from = current_page_from + 24
            next_page_to = current_page_to + 24

            if has_more_products:
                # Construct URL for the next page
                next_page = f"{self.base_url}?O=OrderByTopSaleDESC&_from={next_page_from}&_to={next_page_to}&sc={self.sc_value}"
                yield scrapy.Request(next_page, callback=self.parse)