# -*- coding: utf-8 -*-

import scrapy


class ScraperItem(scrapy.Item):
    brand = scrapy.Field()
    primary_category = scrapy.Field()
    secondary_category = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    model = scrapy.Field()
    available_sizes = scrapy.Field()
    color = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    is_discounted = scrapy.Field()

    url = scrapy.Field()
    date = scrapy.Field()
