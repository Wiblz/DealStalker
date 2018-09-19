import scrapy
import re
import datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

from scraper.category_resolvers import ForwardResolver
from scraper.items import ScraperItem

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class AsosSpider(scrapy.Spider):
    name = "asos"

    #starting request point
    def start_requests(self):
        #TODO here should be all the categories, if no crawling logic from main page be implemented
        urls = ['http://www.asos.com/women/coats-jackets/cat/?cid=2641&nlid=ww']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #parsing links which lead to product entries 
    def parse(self, response):
    #logic is only for ASOS pages
        for quote in response.css("article._2oHs74P a::attr(href)"):
            next_product = quote.extract()
            if next_product is not None:
                next_product = response.urljoin(next_product)
                yield scrapy.Request(next_product, callback=self.parseProductAsos)
         
        next_page = response.css("a._2HG66Ah::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    
    #parsing product entries logic
    def parseProductAsos(self, response):
        item_loader = ItemLoader(item=ScraperItem(), response=response)

        for product in response.css("div.product-hero h1::text"):
            self.log(product.extract())

        brand = response.css("div.brand-description a::text").extract_first()
        inner_id = response.css("div.product-code h4::text").extract_first()
        #price = response.css("span.price::text").extract_first()

        model = response.css("div.product-hero h1::text").extract_first()
        image = response.css("div.product-gallery-static img::attr(src)").extract_first()

        description = ''
        for desc in response.css("div.product-description li::text"):
            description += desc.extract()
            description += ', '
        
        is_discounted = False
        gender = 'u'
        pricef = '75.0'
        db_category = ''
        color = ''
        price_currency = "GBP"


        item_loader.add_value('gender', gender)
        item_loader.add_value('is_discounted', is_discounted)
        item_loader.add_value('description', description)
        item_loader.add_value('model',model)       
        item_loader.add_value('price',pricef)
        item_loader.add_value('brand', brand)
        item_loader.add_value('db_category',db_category)
        item_loader.add_value('inner_id', inner_id)
        item_loader.add_value('color',color)

        item_loader.add_value('resource', "asos")
        item_loader.add_value('url', response.url)
        item_loader.add_value('date', str(datetime.datetime.now()))

        return item_loader.load_item()

