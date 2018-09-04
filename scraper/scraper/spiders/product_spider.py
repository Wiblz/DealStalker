import scrapy


class QuotesSpider(scrapy.Spider):
    name = "product"

    #starting request point
    def start_requests(self):
        urls = [
            'http://www.asos.com/women/coats-jackets/cat/?cid=2641&nlid=ww',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #parsing links which lead to product entries 
    def parse(self, response):
        for quote in response.css("article._2oHs74P a::attr(href)"):
            yield {
		'text': quote.extract()
            }
	    next_page = quote.extract()
	    if next_page is not None:
            	next_page = response.urljoin(next_page)
            	yield scrapy.Request(next_page, callback=self.parseProductAsos)
    
    #parsing product entries logic
    def parseProductAsos(self,response):
	for product in response.css("div.product-hero h1"):
		yield {
			'text': product.extract()
		}
		self.log(product.extract())
