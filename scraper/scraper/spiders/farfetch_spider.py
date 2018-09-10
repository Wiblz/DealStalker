import scrapy
from scrapy.loader import ItemLoader

from scraper.items import ScraperItem


class FarfetchSpider(scrapy.spiders.CrawlSpider):
    name = "farfetch"
    alowed_domains = ["farfetch"]

    def __init__(self):
        super().__init__()
        self.current_page = 1
        self.pages_available = None
        self.current_url_base = None

    def start_requests(self):
        urls = ['https://www.farfetch.com/shopping/men/clothing-2/items.aspx']
        for url in urls:
            self.current_url_base = url
            yield scrapy.Request(url=url, callback=self.parse, headers={
                'Accept-Language': 'en-US',
                'Content-Language': 'en-US'
            }, cookies={
                'ckm-ctx-sf': '/'
            })

    def parse(self, response):
        if self.current_page == 1:
            self.pages_available = int(response.xpath('//*[@data-tstid="paginationTotal"]/text()').extract_first())

        items = response.xpath('//*[@data-tstid="Div_ListingProduct"]/a[1]/@href').extract()
        for item in items:
            if item is not None:
                item_url = response.urljoin(item)
            yield scrapy.Request(item_url, callback=self.parse_item)

        for next_page in range(self.current_page + 1, self.pages_available + 1):
            yield scrapy.Request(self.current_url_base + "?page=" + str(next_page), callback=self.parse)

    def parse_item(self, response):
        item_loader = ItemLoader(item=ScraperItem(), response=response)

        brand = response.xpath('//*[@itemprop="brand"]/text()').extract_first()
        item_loader.add_value('brand', brand)
        return item_loader.load_item()
