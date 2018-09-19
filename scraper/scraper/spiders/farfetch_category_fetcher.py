import scrapy


class BasicSpider(scrapy.Spider):
    name = "cat"
    allowed_domains = ["farfetch"]

    def start_requests(self):
        urls = [
                # "https://www.farfetch.com/shopping/men/activewear-2/items.aspx",  # 137116 ?
                # "https://www.farfetch.com/shopping/men/beachwear-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/coats-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/denim-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/jackets-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/polo-shirts-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/shirts-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/shorts-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/suits-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/sweaters-knitwear-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/trousers-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/t-shirts-vests-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/underwear-socks-2/items.aspx",
                #
                # "https://www.farfetch.com/shopping/men/deck-shoes-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/boots-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/brogues-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/derbies-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/espadrilles-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/flip-flops-slides-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/lace-up-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/loafers-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/buckled-shoes-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/oxfords-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/sandals-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/slippers-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/trainers-2/items.aspx",
                #
                # "https://www.farfetch.com/shopping/men/belts-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/braces-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/glasses-frames-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/gloves-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/hats-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/keyrings-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/scarves-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/sunglasses-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/ties-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/umbrellas-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/wallets-cardholders-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/wash-bags-2/items.aspx",
                #
                # "https://www.farfetch.com/shopping/men/backpacks-2/items.aspx",
                # "https://www.farfetch.com/sets/men/trend-belt-bags-men.aspx",
                # "https://www.farfetch.com/shopping/men/clutches-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/laptop-briefcases-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/luggage-holdalls-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/messengers-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/shoulder-bags-2/items.aspx",
                # "https://www.farfetch.com/shopping/men/totes-2/items.aspx"

                "https://www.farfetch.com/shopping/women/activewear-1/items.aspx",
                "https://www.farfetch.com/shopping/women/beachwear-1/items.aspx",
                "https://www.farfetch.com/shopping/women/coats-1/items.aspx",
                "https://www.farfetch.com/shopping/women/denim-1/items.aspx",
                "https://www.farfetch.com/shopping/women/dresses-1/items.aspx",
                "https://www.farfetch.com/shopping/women/jackets-1/items.aspx",
                "https://www.farfetch.com/shopping/women/all-in-one-1/items.aspx",
                "https://www.farfetch.com/shopping/women/knitwear-1/items.aspx",
                "https://www.farfetch.com/shopping/women/lingerie-hosiery-1/items.aspx",
                "https://www.farfetch.com/shopping/women/shorts-1/items.aspx",
                "https://www.farfetch.com/shopping/women/skirts-1/items.aspx",
                "https://www.farfetch.com/shopping/women/tops-1/items.aspx",
                "https://www.farfetch.com/shopping/women/trousers-1/items.aspx",

                "https://www.farfetch.com/shopping/women/ballerinas-1/items.aspx",
                "https://www.farfetch.com/shopping/women/boots-1/items.aspx",
                "https://www.farfetch.com/shopping/women/brogues-1/items.aspx",
                "https://www.farfetch.com/shopping/women/espadrilles-1/items.aspx",
                "https://www.farfetch.com/shopping/women/flip-flops-slides-1/items.aspx",
                "https://www.farfetch.com/shopping/women/lace-up-shoe-1/items.aspx",
                "https://www.farfetch.com/shopping/women/loafers-1/items.aspx",
                "https://www.farfetch.com/shopping/women/mules-1/items.aspx",
                "https://www.farfetch.com/shopping/women/pumps-1/items.aspx",
                "https://www.farfetch.com/shopping/women/sandals-1/items.aspx",
                "https://www.farfetch.com/shopping/women/slippers-1/items.aspx",
                "https://www.farfetch.com/shopping/women/trainers-1/items.aspx",

                "https://www.farfetch.com/shopping/women/belts-1/items.aspx",
                "https://www.farfetch.com/shopping/women/glasses-frames-1/items.aspx",
                "https://www.farfetch.com/shopping/women/gloves-1/items.aspx",
                "https://www.farfetch.com/shopping/women/hair-accessories-1/items.aspx",
                "https://www.farfetch.com/shopping/women/hats-1/items.aspx",
                "https://www.farfetch.com/shopping/women/keyrings-1/items.aspx",
                "https://www.farfetch.com/shopping/women/make-up-bag-1/items.aspx",
                "https://www.farfetch.com/shopping/women/scarves-1/items.aspx",
                "https://www.farfetch.com/shopping/women/sunglasses-1/items.aspx",
                "https://www.farfetch.com/shopping/women/wallets-purses-1/items.aspx",

                "https://www.farfetch.com/shopping/women/backpacks-1/items.aspx",
                "https://www.farfetch.com/sets/women/trend-belt-bags-women.aspx",
                "https://www.farfetch.com/sets/women/trend-bucket-bag-women.aspx",
                "https://www.farfetch.com/shopping/women/clutches-1/items.aspx",
                "https://www.farfetch.com/shopping/women/luggage-holdalls-1/items.aspx",
                "https://www.farfetch.com/shopping/women/mini-bags-1/items.aspx",
                "https://www.farfetch.com/shopping/women/satchel-cross-body-bags-1/items.aspx",
                "https://www.farfetch.com/shopping/women/shoulder-bags-1/items.aspx",
                "https://www.farfetch.com/shopping/women/totes-1/items.aspx",
                "https://www.farfetch.com/shopping/women/bag-accessories-1/items.aspx"
                ]
        for url in urls:
            # Dodging annoying redirect using cookies and additional headers
            yield scrapy.Request(url=url, callback=self.parse, headers={
                'Accept-Language': 'en-US',
                'Content-Language': 'en-US'
            }, cookies={
                'ckm-ctx-sf': '/'
            })

    def parse(self, response):
        with open("categories.txt", "a") as file:
            cat_names = response.xpath('//*[contains(@class, "tree-title")]/@title').extract()
            cat_ids = response.xpath('//*[contains(@class, "tree-title")]/@data-lp-value').extract()
            sub_cat_names = response.xpath('//*[contains(@class, "hierarchical-option")]/@title').extract()
            sub_cat_ids = response.xpath('//*[contains(@class, "hierarchical-option")]/@data-lp-value').extract()

            for i in range(len(cat_ids)):
                file.write(cat_ids[i] + ": " + cat_names[i] + "[W]\n")
            for i in range(len(sub_cat_ids)):
                file.write(sub_cat_ids[i] + ": " + sub_cat_names[i] + "[W]\n")
