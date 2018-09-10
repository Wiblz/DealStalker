import scrapy

class QuotesSpider(scrapy.Spider):
    name = "product"

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
            yield {
                'text': quote.extract()
            }
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
        #open('testfile', 'w').close()
        file = open("testfile", "a+")
        for product in response.css("div.product-hero h1"):
            yield {
            'text': product.extract()
            }
            self.log(product.extract())
            file.write(product.extract())
            file.write("\n")
        file.close()
