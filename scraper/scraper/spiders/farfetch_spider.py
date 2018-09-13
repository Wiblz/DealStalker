import datetime
import json

import scrapy
from scrapy.loader import ItemLoader

from scraper.category_resolvers import FarfetchResolver
from scraper.items import ScraperItem

import urllib.parse as urlparse


class FarfetchSpider(scrapy.spiders.CrawlSpider):
    name = "farfetch"
    alowed_domains = ["farfetch"]

    def __init__(self):
        super().__init__()
        self.pages_available = None
        self.current_url_base = None
        self.category_resolver = FarfetchResolver()

    def start_requests(self):
        # TODO: add every single category here and test how the loop works
        urls = ['https://www.farfetch.com/shopping/men/clothing-2/items.aspx']
        for url in urls:
            self.current_url_base = url
            # Dodging annoying redirect using cookies and additional headers
            yield scrapy.Request(url=url, callback=self.parse, headers={
                'Accept-Language': 'en-US',
                'Content-Language': 'en-US'
            }, cookies={
                'ckm-ctx-sf': '/'
            }, meta={
                'page_number': 1
            })

    def parse(self, response):
        if response.meta['page_number'] == 1:
            self.pages_available = int(response.xpath('//*[@data-tstid="paginationTotal"]/text()').extract_first())

        items = response.xpath('//*[@data-product-id]/@data-product-id').extract()
        for item in items:
            yield scrapy.Request('https://www.farfetch.com/pdpslice/product/GetInfoByIds?ids=' + item +
                                 '&mainProductId=' + item + '&isMoreLikeThis=false', callback=self.parse_item_json)

        # TODO: test paging scheme on different categories
        next_page = response.meta['page_number'] + 1
        if next_page <= self.pages_available:
            yield scrapy.Request(self.current_url_base + "?page=" + str(next_page), callback=self.parse,
                                 dont_filter=True, meta={'page_number': next_page})

    def parse_item_json(self, response):

        item_properties = json.loads(response.body.decode('utf-8'))[0]

        item_loader = ItemLoader(item=ScraperItem(), response=response)

        # TODO: cleanup strings where needed
        # TODO: test how this code works with discounted, one-sized and out of stock items
        # TODO: test how this code works with more "exotic" categories and products
        # TODO: implement extracting of product category (both domain and DB specific)

        item_loader.add_value('brand', item_properties['designerDetails']['name'])
        item_loader.add_value('price', item_properties['priceInfo']['default']['finalPrice'])
        item_loader.add_value('price_currency', item_properties['priceInfo']['default']['currencyCode'])
        item_loader.add_value('model', item_properties['details']['shortDescription'])
        item_loader.add_value('image', item_properties['images']['main'][0]['large'])
        item_loader.add_value('description', item_properties['designerDetails']['description'])
        item_loader.add_value('color', item_properties['designerDetails']['designerColour'])
        item_loader.add_value('is_discounted', item_properties['priceInfo']['default']['isOnSale'])
        inner_id = item_properties['details']['productId']
        item_loader.add_value('inner_id', inner_id)

        category_data = urlparse.parse_qs(urlparse.urlparse(item_properties['sizeGuideUri']).query)
        item_loader.add_value('db_category', self.category_resolver.resolve(category_data['CategoryIDs'], inner_id))
        if category_data['Gender'][0] == 'Man':
            item_loader.add_value('gender', 'm')
        else:
            item_loader.add_value('gender', 'w')

        available_sizes = []
        if item_properties['sizes']['isOneSize']:
            available_sizes.append('One Size')
        else:
            for size, value in item_properties['sizes']['available'].items():
                # Should we add last in stock info here as well?
                available_sizes.append(value['description'])
        item_loader.add_value('available_sizes', item_properties['priceInfo']['default']['isOnSale'])

        item_loader.add_value('resource', 'farfetch')
        item_loader.add_value('url', 'https://www.farfetch.com' + item_properties['details']['link']['href'])
        item_loader.add_value('date', str(datetime.datetime.now()))

        return item_loader.load_item()
