import scrapy
from scrapy.loader import ItemLoader

from scraper.items import ScraperItem


class FarfetchSpider(scrapy.spiders.CrawlSpider):
    name = "forward"
    alowed_domains = ["fwrd"]

    def __init__(self):
        super().__init__()
        self.current_page = None
        self.pages_available = None
        self.current_url_base = None
        self.__pages_parsed = 0
        self.__items_parsed = 0

    def start_requests(self):
        urls = ['https://www.fwrd.com/mens-category-clothing/15d48b/?navsrc=main']
        for url in urls:
            self.current_url_base = url
            self.current_page = 1
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     with open('fwrd_index_true_form.txt', 'a') as the_file:
    #         the_file.write(response.body.decode(response.encoding))

    def parse(self, response):
        self.pages_available = int(
            response.xpath('(//*[contains(@class, "pagination__link")])[last()]/text()').extract_first())

        self.parse_page(response)

        for self.current_page in range(2, self.pages_available + 1):
            yield scrapy.Request(self.current_url_base + "&pageNum=" + str(self.current_page), callback=self.parse_page,
                                 dont_filter=True)

    def parse_page(self, response):
        items = response.xpath('//*[contains(@class, "products-grid__item")]/a[1]/@href').extract()
        for item in items:
            if item is not None:
                item_url = response.urljoin(item)
            yield scrapy.Request(item_url, callback=self.parse_item)

    def parse_item(self, response):
        item_loader = ItemLoader(item=ScraperItem(), response=response)

        return item_loader.load_item()
