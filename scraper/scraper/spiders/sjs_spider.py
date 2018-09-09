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

        # Get product brand
        item_loader.add_xpath('brand', '//*[@id="columns"]/div[1]/span[2]/span[9]/a/span/text()')

        item_loader.add_xpath('price', '//*[@id="our_price_display"]/text()',
                              MapCompose(lambda i: i[2:]))

        item_loader.add_xpath('price_currency', '(//*[@itemprop="priceCurrency"])[1]/@content')

        model = response.xpath('//*[@id="columns"]/div[1]/span[2]/text()').extract()

        item_loader.add_value('model', model)

        available_sizes = response.xpath('//*[contains(@class, "attribute_select")]/option/text()').extract()
        del available_sizes[0]

        item_loader.add_value('available_sizes', available_sizes)

        full_product_name = response.xpath('(//*[@class="h4"])[1]/text()').extract()
        item_loader.add_value('color', full_product_name.replace(model, ''), MapCompose(str.strip))

        is_discounted = len(response.xpath('//*[contains(@class, "price_reduced")]').extract()) == 0
        item_loader.add_value('is_discounted', is_discounted)

        return item_loader.load_item()
