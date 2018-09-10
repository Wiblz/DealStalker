import js2xml as js2xml
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

from scraper.items import ScraperItem


class FarfetchSpider(scrapy.spiders.CrawlSpider):
    name = "farfetch"
    alowed_domains = ["farfetch"]

    def __init__(self):
        super().__init__()
        self.pages_available = None
        self.current_url_base = None

    def start_requests(self):
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

        items = response.xpath('//*[@data-tstid="Div_ListingProduct"]/a[1]/@href').extract()
        for item in items:
            if item is not None:
                item_url = response.urljoin(item)
                yield scrapy.Request(item_url, callback=self.parse_item, meta={'retries':0})

        next_page = response.meta['page_number'] + 1
        if next_page <= self.pages_available:
            yield scrapy.Request(self.current_url_base + "?page=" + str(next_page), callback=self.parse,
                                 dont_filter=True, meta={'page_number': next_page})

    def parse_item(self, response):
        item_loader = ItemLoader(item=ScraperItem(), response=response)

        script = response.xpath('//*/script[6]/text()').extract_first()
        jstree = js2xml.parse(script)
        item_properties = js2xml.jsonlike.getall(jstree)[0]

        # try:
        item_loader.add_value('brand', item_properties['designerName'])
        item_loader.add_value('price', item_properties['unitPrice'])
        item_loader.add_value('price_currency', item_properties['currency'])
        item_loader.add_value('model', item_properties['name'])
        item_loader.add_value('image', item_properties['imageUrl'])
        item_loader.add_value('description', item_properties['description'])

        # price = response.xpath('//*[@property="og:price:amount"]/text()').extract_first()
        # item_loader.add_value('price', price, MapCompose(str.strip, float))
        #
        # item_loader.add_xpath('price_currency', '(//*[@property="og:price:currency"])[1]/text()')

        return item_loader.load_item()
