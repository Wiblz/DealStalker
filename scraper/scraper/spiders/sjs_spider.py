import datetime
from urllib.parse import urlparse

import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scraper.items import ScraperItem


class SJSSpider(scrapy.spiders.CrawlSpider):
    name = "SJS"
    alowed_domains = ["slamjamsocialism"]
    start_urls = (
        "https://www.slamjamsocialism.com/clothing/",
    )

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@id="pagination_next_bottom"]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="right-block"]'), callback='parse_item')
    )

    def parse_item(self, response):
        item_loader = ItemLoader(item=ScraperItem(), response=response)

        item_loader.add_xpath('brand', '(//*[@itemprop="title"])[last()]/text()')

        price = response.xpath('//*[@id="our_price_display"]/text()').extract_first()
        item_loader.add_value('price', price,
                              MapCompose(lambda i: i[2:].replace(',', '.'), float))

        item_loader.add_xpath('price_currency', '(//*[@itemprop="priceCurrency"])[1]/@content')

        model = response.xpath('//*[@id="columns"]/div[1]/span[2]/text()').extract_first()
        item_loader.add_value('model', model)

        available_sizes = response.xpath('(//*[contains(@class, "attribute_select")]/option)[.!="Select Size"]/text()').extract()
        item_loader.add_value('available_sizes', available_sizes)

        full_product_name = response.xpath('//*[@class="h4"]/text()').extract_first()
        item_loader.add_value('color', full_product_name.replace(model, ''), MapCompose(str.strip))

        image_src = response.xpath('(//*[@itemprop="image"])[1]/@src').extract_first()
        item_loader.add_value('image', image_src)

        description = response.xpath('//*[@id="prod-desc"]/div/p/text()').extract_first()
        item_loader.add_value('description', description)

        is_discounted = len(response.xpath('//*[contains(@class, "price_reduced")]').extract()) != 0
        item_loader.add_value('is_discounted', is_discounted)

        item_loader.add_value('resource', 'slamjamsocialism')
        item_loader.add_value('url', response.url)
        item_loader.add_value('date', str(datetime.datetime.now()))

        return item_loader.load_item()
