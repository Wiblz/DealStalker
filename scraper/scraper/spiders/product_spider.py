import scrapy

class QuotesSpider(scrapy.Spider):
    name = "product"

    #starting request point
    def start_requests(self):
        #TODO here should be all the categories, if no crawling logic from main page be implemented
	urls = [
             #ASOS clothing
            'http://www.asos.com/women/coats-jackets/cat/?cid=2641&nlid=ww&page=1'
            'http://www.asos.com/women/dresses/cat/?cid=8799&nlid=ww',
            'http://www.asos.com/women/tops/hoodies-sweatshirts/cat/?cid=11321&nlid=ww',
            'http://www.asos.com/women/jeans/cat/?cid=3630&nlid=ww',
            'http://www.asos.com/women/jumpers-cardigans/cat/?cid=2637&nlid=ww' ,
            'http://www.asos.com/women/jumpsuits-playsuits/cat/?cid=7618&nlid=ww' 
            'http://www.asos.com/women/lingerie-nightwear/cat/?cid=6046&nlid=ww', 
            'http://www.asos.com/women/loungewear/cat/?cid=21867&nlid=ww' ,
            'http://www.asos.com/women/multi-packs-save/cat/?cid=19224&nlid=ww', 
            'http://www.asos.com/women/skirts/cat/?cid=2639&nlid=ww' ,
            'http://www.asos.com/women/socks-tights/cat/?cid=7657&nlid=ww', 
            'http://www.asos.com/women/suits-separates/cat/?cid=13632&nlid=ww', 
            'http://www.asos.com/women/swimwear-beachwear/cat/?cid=2238&nlid=ww',
            'http://www.asos.com/women/tops/cat/?cid=4169&nlid=ww' 
            #ASOS shoes
            	#TODO
            #ASOS Accessories
            	#TODO
            #ASOS Activewear
            	#TODO            
           ]

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
         
	next_page = response.css("a._2HG66Ah::attr(href)")[-1].extract()
	if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    
    #parsing product entries logic
    def parseProductAsos(self,response):
	file = open("testfile","a+")
	for product in response.css("div.product-hero h1"):
	    yield {
		'text': product.extract()
	    }
	    self.log(product.extract())
	    file.write(product.extract())
            file.write("\n")
	file.close()
