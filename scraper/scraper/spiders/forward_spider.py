import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

from scraper.category_resolvers import ForwardResolver
from scraper.items import ScraperItem


class FarfetchSpider(scrapy.spiders.CrawlSpider):
    name = "forward"
    alowed_domains = ["fwrd"]

    custom_settings = {'COOKIES_ENABLED': 'True'}

    def __init__(self, name=None, **kwargs):
        super().__init__()
        self.pages_available = None
        self.current_url_base = None
        self.category_resolver = ForwardResolver()

    def start_requests(self):
        urls = [
            'https://www.fwrd.com/mens-category-clothing/15d48b/?navsrc=main',
            'https://www.fwrd.com/mens-category-shoes/b05f2e/?navsrc=main',
            'https://www.fwrd.com/mens-category-bags/6c97c1/?navsrc=main',
            'https://www.fwrd.com/mens-category-accessories/8ad9de/?navsrc=main',

            'https://www.fwrd.com/category-clothing/3699fc/?navsrc=main',
            'https://www.fwrd.com/category-shoes/3f40a9/?navsrc=main',
            'https://www.fwrd.com/category-bags/2df9df/?navsrc=main',
            'https://www.fwrd.com/category-accessories/2fa629/?navsrc=main'
        ]
        for url in urls:
            self.current_url_base = url
            yield scrapy.Request(url=url, callback=self.parse, meta={
                'page_number': 1
            }, cookies={
                'pageSize': 500,
                'currency': 'USD',
                'currencyOverride': 'USD'
            })

    def parse(self, response):
        if response.meta['page_number'] == 1:
            self.pages_available = int(response.xpath('(//*[contains(@class, "pagination__link")])[last()]/text()').extract_first())

        items = response.xpath('//*[contains(@class, "products-grid__item")]/a[1]/@href').extract()
        for item in items:
            if item is not None:
                item_url = response.urljoin(item)
            yield scrapy.Request(item_url, callback=self.parse_item)

        next_page = response.meta['page_number'] + 1
        if next_page <= self.pages_available:
            yield scrapy.Request(self.current_url_base + "&pageNum=" + str(next_page), callback=self.parse,
                                 dont_filter=True, meta={'page_number': next_page})

    def parse_item(self, response):
        # Check if this item is still in stock
        if response.xpath('//*[@id="sold-out-div"]').extract_first():
            print(response.url, "\nIS SOLD OUT!")
            return

        item_loader = ItemLoader(item=ScraperItem(), response=response)

        item_loader.add_xpath('brand', '(//*[@class="u-color--black"])[1]/text()', MapCompose(str.strip))

        price = response.xpath('//*[@id="tr-pdp-price--sale"]/span[1]/text()').extract_first()
        if price:
            item_loader.add_value('is_discounted', True)
        else:
            item_loader.add_value('is_discounted', False)
            price = response.xpath('//*[@id="tr-pdp-price"]/span[1]/text()').extract_first()

        # removing '$' at the beginning of price string and casting to float
        item_loader.add_value('price', price,
                              MapCompose(lambda i: ''.join(ch for ch in i if ch.isdigit()), float))

        # Supposedly currency of all 'forward' items will be in dollars as we asked so in cookies
        item_loader.add_value('price_currency', 'USD')

        model = response.xpath('//*[@class="product_name"]/text()').extract_first()
        item_loader.add_value('model', model)

        # Should we add last in stock info here as well?
        available_sizes = response.xpath('(//*[@id="size-select"]/option)[.!="Select Size"]/text()').extract()
        if not available_sizes:
            available_sizes = ['One Size']
        item_loader.add_value('available_sizes', filter(lambda size: not size.endswith("(Sold Out)"),
                                                        map(str.strip, available_sizes)))

        color = response.xpath('//*[@id="color-select"]/option[1]/text()').extract_first()
        if not color:
            color = response.xpath('//*[contains(@class, "color_dd")]/div[1]/text()').extract_first()
        item_loader.add_value('color', color, MapCompose(str.strip))

        image_src = response.xpath('//*[@class="product-detail-image"]/@src').extract_first()
        item_loader.add_value('image', image_src)

        gender = response.xpath('//*[@class="nav-toggle__item current"]/a[1]/text()').extract_first()
        if gender == "MENS":
            item_loader.add_value('gender', 'm')
        else:
            item_loader.add_value('gender', 'w')

        inner_id = response.xpath('//*[@class="product_detail"]/ul[1]/li[last()]/text()').extract_first()
        inner_id = inner_id.replace('Manufacturer Style No. ', '')
        item_loader.add_value('inner_id', inner_id)

        inner_categories = list(map(str.strip, response.xpath('//*[@id="ctaMainBtn"]/button[1]/@data-category').extract_first().split(':')))
        item_loader.add_value('db_category', self.category_resolver.resolve(inner_categories, inner_id, gender))

        item_loader.add_value('resource', "forward")
        item_loader.add_value('url', response.url)
        item_loader.add_value('date', str(datetime.datetime.now()))

        return item_loader.load_item()
