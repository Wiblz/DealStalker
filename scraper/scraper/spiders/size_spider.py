import scrapy

class SizeSpider(scrapy.spiders.Spider):
    name = "size"
    #alowed_domains = ["size"]
    start_urls = (
        #"https://www.size.co.uk/mens/"
        "https://www.size.co.uk/product/yellow-carhartt-wip-script-sweatshirt---size-exclusive/073385/",
    )

    def parse(self, response):
        self.log(response.xpath('/html/head/script[10]/text()').extract())