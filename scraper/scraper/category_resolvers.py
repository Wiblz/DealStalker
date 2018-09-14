import logging

class FarfetchResolver:
    def __init__(self):
        self.logger = logging.getLogger('category_resolver')
        handler = logging.FileHandler('logs/farfetch_categories.log')
        self.logger.addHandler(handler)
        self.category_dict = {
            '135970': 'Bags',   # Bags
            '135971': 'Bags [W]',  # Bags[W]
            '135972': 'Undefined',  # Accessories TODO
            '135973': 'Undefined',  # Accessories[W] TODO
            '135974': 'Undefined',  # Lifestyle TODO
            '135979': 'Dresses [W]',  # Dresses[W]
            '135981': 'Jeans & Trousers [W]',  # Pants[W]
            '135983': 'Tops [W]',  # Tops[W]
            '135985': 'Skirts [W]',  # Skirts[W]
            '135996': 'Sanadals, Sliders & Flip Flops',  # Slippers
            '135998': 'Bags',  # Clutch Bags
            '135999': 'Bags [W]',  # Clutch Bags[W]
            '136000': 'Belts & Braces',  # Belts
            '136001': 'Belts & Braces [W]',  # Belts[W]
            '136002': 'Gloves and Scarfs',  # Scarves
            '136003': 'Gloves and Scarfs [W]',  # Scarves[W]
            '136004': 'Ties',  # Ties & Bow Ties
            '136006': 'Hats & Caps',  # Hats
            '136010': 'Ambiguous',  # Keyrings & Chains TODO
            '136011': 'Not really useful stuff [W]',  # Keyrings & Chains[W]
            '136014': 'Bags',  # Laptop Bags & Briefcases
            '136032': 'Bags',  # Tote Bags
            '136033': 'Bags [W]',  # Tote Bags[W]
            '136034': 'Bags',  # Shoulder bags
            '136035': 'Bags [W]',  # Shoulder Bags[W]
            '136043': 'Undefined',  # Denim[W] TODO
            '136045': 'Shorts [W]',  # Shorts[W]
            '136069': 'Hair accessories [W]',  # Hair Accessories[W]
            '136071': 'Lingerie & Nightwear & Kimonos [W]',  # Lingerie[W]
            '136089': 'Jeans & Trousers [W]',  # Leggings[W]
            '136091': 'T-shirts [W]',  # T-Shirts & Jersey Shirts[W]
            '136093': 'Tops [W]',  # Polo Tops[W]
            '136099': 'Shirts [W]',  # Shirts[W]
            '136101': 'Tops [W]',  # Blouses[W]
            '136103': 'Skirts [W]',  # A-Line Skirts[W]
            '136105': 'Skirts [W]',  # Asymmetric & Draped Skirts[W]
            '136107': 'Skirts [W]',  # High-Waisted Skirts[W]
            '136137': 'Hoodies & Sweatshirts [W]',  # Vests & Tank Tops[W]
            '136147': 'Hoodies & Sweatshirts [W]',  # Cardigans[W]
            '136149': 'Hoodies & Sweatshirts [W]',  # Sweaters[W]
            '136157': 'Hoodies & Sweatshirts [W]',  # Hoodies[W]
            '136175': 'Jeans & Trousers [W]',  # Skinny Jeans[W]
            '136177': 'Jeans & Trousers [W]',  # Bootcut Jeans[W]
            '136179': 'Jeans & Trousers [W]',  # Straight-Leg Jeans[W]
            '136181': 'Jeans & Trousers [W]',  # Wide-Leg Jeans[W]
            '136183': 'Jeans & Trousers [W]',  # Flares & Bell Bottom Jeans[W]
            '136185': 'Jeans & Trousers [W]',  # Boyfriend Jeans[W]
            '136187': 'Jeans & Trousers [W]',  # Tapered Jeans[W]
            '136189': 'Dresses [W]',  # Day Dresses[W]
            '136191': 'Dresses [W]',  # Evening Dresses[W]
            '136193': 'Dresses [W]',  # Cocktail & Party Dresses[W]
            '136212': 'Undefined',  # Vintage[W] TODO
            '136214': 'Bags [W]',  # Vintage Bags[W]
            '136225': 'Dresses [W]',  # Sundresses[W]
            '136226': 'Jackets & Coats [W]',  # Jackets[W]
            '136227': 'Jackets & Coats [W]',  # Coats[W]
            '136238': 'Jackets & Coats [W]',  # Capes[W]
            '136239': 'Jackets & Coats [W]',  # Double Breasted & Peacoats[W]
            '136240': 'Jackets & Coats [W]',  # Fur & Shearling Coats[W]
            '136241': 'Jackets & Coats [W]',  # Leather Coats[W]
            '136242': 'Jackets & Coats [W]',  # Military Coats[W]
            '136243': 'Jackets & Coats [W]',  # Parkas[W]
            '136244': 'Jackets & Coats [W]',  # Trench Coats & Raincoats[W]
            '136245': 'Undefined',  # Knitwear[W] TODO
            '136246': 'Hoodies & Sweatshirts [W]',  # Cardi-Coats[W]
            '136247': 'Hoodies & Sweatshirts [W]',  # Cardigans[W]
            '136248': 'Dresses [W]',  # Sweater Dresses[W]
            '136249': 'Jeans & Trousers [W]',  # Knitted Leggings[W]
            '136250': 'Skirts [W]',  # Knitted Skirts[W]
            '136251': 'Hoodies & Sweatshirts [W]',  # Knitted Sweaters[W]
            '136252': 'Hoodies & Sweatshirts [W]',  # Knitted Tops[W]
            '136253': 'Undefined',  # Jumpsuits & All in ones[W] TODO
            '136254': 'Dresses [W]',  # Jumpsuits[W]
            '136255': 'Dresses [W]',  # Playsuits[W]
            '136257': 'Jeans & Trousers [W]',  # Cropped Jeans[W]
            '136258': 'Jackets & Coats [W]',  # Denim Jackets[W]
            '136259': 'Jeans & Trousers [W]',  # Denim Leggings[W]
            '136260': 'Shirts [W]',  # Denim Shirts[W]
            '136261': 'Shorts [W]',  # Jean Shorts[W]
            '136262': 'Skirts [W]',  # Denim Skirts[W]
            '136263': 'Jeans & Trousers [W]',  # Cropped Pants[W]
            '136264': 'Jeans & Trousers [W]',  # Flared & Bell-Bottom Pants[W]
            '136265': 'Jeans & Trousers [W]',  # High Waisted Pants[W]
            '136266': 'Jeans & Trousers [W]',  # Capri Pants[W]
            '136267': 'Jeans & Trousers [W]',  # Skinny Pants[W]
            '136268': 'Jeans & Trousers [W]',  # Slim Pants[W]
            '136269': 'Jeans & Trousers [W]',  # Straight-Leg Pants[W]
            '136270': 'Jeans & Trousers [W]',  # Slacks[W]
            '136271': 'Jeans & Trousers [W]',  # Tapered Pants[W]
            '136272': 'Jeans & Trousers [W]',  # Sweatpants[W]
            '136273': 'Jeans & Trousers [W]',  # Palazzo Pants[W]
            '136274': 'Shorts [W]',  # Short Shorts[W]
            '136275': 'Shorts [W]',  # Knee-Length Shorts[W]
            '136276': 'Skirts [W]',  # Pencil Skirts[W]
            '136277': 'Skirts [W]',  # Pleated Skirts[W]
            '136278': 'Skirts [W]',  # Straight Skirts[W]
            '136279': 'Skirts [W]',  # Full Skirts[W]
            '136285': 'Underwear [W]',  # Bodies[W]
            '136286': 'Bra [W]',  # Bras[W]
            '136287': 'Underwear [W]',  # Panties[W]
            '136288': 'Loungewear [W]',  # Loungewear[W]
            '136289': 'Lingerie & Nightwear & Kimonos [W]',  # Nightwear[W]
            '136290': 'Socks & Tights [W]',  # Socks[W]
            '136291': 'Socks & Tights [W]',  # Pantyhose & Stockings[W]
            '136292': 'Bra [W]',  # Camisoles & Corsets[W]
            '136293': 'Activewear [W]',  # Beachwear[W]
            '136294': 'Swimming wear [W]',  # Bikinis[W]
            '136295': 'Dresses [W]',  # Beach Dresses[W]
            '136296': 'Swimming wear [W]',  # Beach Accessories[W]
            '136298': 'Undefined',  # Beach Cover-Ups[W] TODO
            '136300': 'Swimming wear [W]',  # Swimsuits[W]
            '136302': 'Boots [W]',  # Boots[W]
            '136303': 'Shoes [W]',  # BROGUES & OXFORDS[W]
            '136304': 'Sanadals, Sliders & Flip Flops [W]',  # ESPADRILLES[W]
            '136305': 'Sanadals, Sliders & Flip Flops [W]',  # Flip flops & Slides [W]
            '136306': 'Shoes [W]',  # Loafers[W]
            '136307': 'Shoes [W]',  # Pumps[W]
            '136308': 'Sanadals, Sliders & Flip Flops [W]',  # Sandals[W]
            '136309': 'Sanadals, Sliders & Flip Flops [W]',  # Slippers[W]
            '136310': 'Sneakers & Trainers [W]',  # Sneakers[W]
            '136311': 'Bags [W]',  # Backpacks[W]
            '136312': 'Bags [W]',  # Luggage[W]
            '136315': 'Bags [W]',  # Messenger & Crossbody Bags[W]
            '136321': 'Glasses [W]',  # GLASSES & FRAMES[W]
            '136322': 'Glasses [W]',  # Sunglasses[W]
            '136323': 'Hats & Caps [W]',  # Hats[W]
            '136324': 'Gloves and Scarfs [W]',  # Gloves[W]
            '136325': 'Bags [W]',  # Make Up Bags[W]
            '136326': 'Wallets & Purses [W]',  # Wallets & Purses[W]
            '136331': 'Shirts',  # Shirts
            '136332': 'T-shirts',  # T-shirts & Vests
            '136333': 'Shirts',  # Polo Shirts
            '136334': 'Hoodies & Sweatshirts',  # Sweaters & Knitwear
            '136335': 'Jackets & Coats',  # Jackets
            '136336': 'Jackets & Coats',  # Coats
            '136337': 'Undefined',  # Denim TODO
            '136338': 'Jeans & Trousers',  # Pants
            '136339': 'Shorts',  # Shorts
            '136340': 'Jackets & Coats',  # Suits
            '136341': 'Undefined',  # Underwear & Socks TODO
            '136342': 'Activewear',  # Beachwear
            '136353': 'Boots',  # Boots
            '136354': 'Shoes',  # Brogues
            '136355': 'Shoes',  # Boat & Deck shoes
            '136356': 'Sanadals, Sliders & Flip Flops',  # Espadrilles
            '136357': 'Sanadals, Sliders & Flip Flops',  # Flip Flops & Slides
            '136358': 'Shoes',  # Lace-up Shoes
            '136359': 'Shoes',  # Loafers
            '136360': 'Sanadals, Sliders & Flip Flops',  # Sandals
            '136361': 'Sneakers & Trainers',  # Low-Tops
            '136362': 'Bags',  # Backpacks
            '136363': 'Bags',  # Holdalls
            '136364': 'Bags',  # Messenger Bags
            '136370': 'Belts & Braces',  # Braces
            '136371': 'Glasses',  # Glasses & Frames
            '136372': 'Gloves and Scarfs',  # Gloves
            '136373': 'Glasses',  # Sunglasses
            '136374': 'Bags',  # Wash Bags
            '136375': 'Wallets & Purses',  # Wallets & Billfolds
            '136377': 'Undefined',  # Phone Cases & Technology TODO
            '136381': 'Undefined',  # Umbrellas TODO
            '136394': 'T-shirts',  # T-Shirts
            '136395': 'T-shirts',  # Vests & Tank Tops
            '136396': 'Hoodies & Sweatshirts',  # Knitted Sweaters
            '136397': 'Hoodies & Sweatshirts',  # Sweatshirts
            '136398': 'Hoodies & Sweatshirts',  # Hoodies
            '136399': 'Hoodies & Sweatshirts',  # Cardigans
            '136400': 'Jackets & Coats',  # Biker Jackets
            '136401': 'Jackets & Coats',  # Lightweight Jackets
            '136402': 'Jackets & Coats',  # Blazers
            '136403': 'Jackets & Coats',  # Denim Jackets
            '136404': 'Jackets & Coats',  # Hooded Jackets
            '136405': 'Jackets & Coats',  # Leather Jackets
            '136406': 'Jackets & Coats',  # Military Jackets
            '136407': 'Jackets & Coats [W]',  # Down Jackets
            '136408': 'Jackets & Coats',  # Shirt Jackets
            '136409': 'Jackets & Coats',  # Sport Jackets & Wind Breakers
            '136410': 'Jackets & Coats',  # Suit & Dinner Jackets
            '136411': 'Jackets & Coats',  # Waistcoats & Gilets
            '136412': 'Jackets & Coats',  # Double Breasted & Peacoats
            '136413': 'Jackets & Coats',  # Hooded Coats
            '136414': 'Jackets & Coats',  # Leather Coats
            '136415': 'Jackets & Coats',  # Military Coats
            '136416': 'Jackets & Coats',  # Down Coats
            '136417': 'Jackets & Coats',  # Parkas & Duffle Coats
            '136418': 'Jackets & Coats',  # Single-Breasted Coats
            '136419': 'Jackets & Coats',  # Trench Coats & Macs
            '136420': 'Jeans & Trousers',  # Bootcut Jeans
            '136421': 'Jeans & Trousers',  # Cropped Jeans
            '136422': 'Jeans & Trousers',  # Drop-Crotch Jeans
            '136423': 'Jeans & Trousers',  # Relaxed-Fit Jeans
            '136424': 'Jeans & Trousers',  # Regular & Straight-Leg Jeans
            '136425': 'Jeans & Trousers',  # Skinny Jeans
            '136426': 'Jeans & Trousers',  # Slim-Fit Jeans
            '136427': 'Jeans & Trousers',  # Tapered Jeans
            '136428': 'Jeans & Trousers',  # Wide-Leg Jeans
            '136429': 'Jackets & Coats',  # Denim Jackets
            '136430': 'Shirts',  # Denim Shirts
            '136431': 'Shorts',  # Denim Shorts
            '136432': 'Jeans & Trousers',  # Chinos
            '136433': 'Jeans & Trousers',  # Cropped Pants
            '136434': 'Jeans & Trousers',  # Drop Crotch Pants
            '136435': 'Jeans & Trousers',  # Leggings
            '136436': 'Jeans & Trousers',  # Loose Fit Pants
            '136437': 'Jeans & Trousers',  # Regular-Fit & Straight Leg Pants
            '136438': 'Jeans & Trousers',  # Skinny Pants
            '136439': 'Jeans & Trousers',  # Tailored Pants
            '136440': 'Jeans & Trousers',  # Tapered Pants
            '136441': 'Jeans & Trousers',  # Sweatpants
            '136442': 'Jeans & Trousers',  # Wide Leg Pants
            '136443': 'Shorts',  # Bermuda Shorts
            '136444': 'Shorts',  # Cargo Shorts
            '136445': 'Shorts',  # Khaki Shorts
            '136446': 'Shorts',  # Deck Shorts
            '136447': 'Shorts',  # Denim Shorts
            '136448': 'Shorts',  # Drop-Crotch Shorts
            '136449': 'Shorts',  # Tailored Shorts
            '136450': 'Shorts',  # Track & Running Shorts
            '136451': 'Jackets & Coats',  # Formal Suits
            '136452': 'Jackets & Coats',  # Dinner Suits
            '136453': 'Jackets & Coats',  # Suit Jackets
            '136455': 'Jackets & Coats',  # Jumpsuits
            '136457': 'Loungewear',  # Loungewear
            '136458': 'Loungewear',  # Sleepwear
            '136459': 'Socks',  # Socks
            '136460': 'Underwear',  # Briefs & Boxers
            '136461': 'Activewear',  # Beach Accessories
            '136463': 'Swimming stuff',  # Swimming Trunks
            '136465': 'Swimming stuff',  # Swim & Board Shorts
            '136466': 'Tops [W]',  # Tunic Tops & Kaftans[W]
            '136467': 'Shoes [W]',  # Mules[W]
            '136468': 'Jackets & Coats',  # Bomber Jackets
            '136481': 'Jackets & Coats [W]',  # Single Breasted Coats[W]
            '136484': 'Shoes [W]',  # Ballerina Shoes[W]
            '136485': 'Shoes [W]',  # Lace-up shoes[W]
            '136487': 'Shoes',  # Monk Shoes
            '136488': 'Skirts [W]',  # Fitted Skirts[W]
            '136489': 'Sneakers & Trainers',  # Hi-Tops
            '136497': 'Jackets & Coats [W]',  # Oversized Coats[W]
            '136498': 'Shoes',  # Oxford Shoes
            '136499': 'Shoes',  # Derby Shoes
            '137116': 'Activewear',  # Activewear
            '137117': 'Activewear [W]',  # Activewear[W]
            '137118': 'Activewear [W]',  # Sport Jackets[W]
            '137119': 'Activewear [W]',  # Sport Shorts[W]
            '137120': 'Activewear [W]',  # Sport Trousers[W]
            '137121': 'Activewear [W]',  # Sport Tops[W]
            '137122': 'Activewear [W]',  # Performance Jackets[W]
            '137123': 'Activewear [W]',  # Sport Parkas[W]
            '137124': 'Activewear [W]',  # Sport Gilets[W]
            '137125': 'Activewear [W]',  # Running Shorts[W]
            '137126': 'Activewear [W]',  # Compression Shorts[W]
            '137127': 'Activewear [W]',  # Sport Track Pants[W]
            '137128': 'Activewear [W]',  # Performance Leggings[W]
            '137129': 'Activewear [W]',  # Compression Tights[W]
            '137130': 'Activewear [W]',  # Compression Tops[W]
            '137131': 'Activewear [W]',  # Sport T-Shirts[W]
            '137132': 'Activewear [W]',  # Sport Tank Tops[W]
            '137133': 'Activewear [W]',  # Sport Sweatshirts & Hoodies[W]
            '137134': 'Activewear [W]',  # Skiwear[W]
            '137135': 'Activewear [W]',  # Ski Tops[W]
            '137136': 'Activewear [W]',  # Ski Bottoms[W]
            '137137': 'Activewear [W]',  # Ski Accessories[W]
            '137138': 'Activewear',  # Sport Jackets
            '137139': 'Activewear',  # Sport Shorts
            '137140': 'Activewear',  # Sport Tops
            '137141': 'Activewear',  # Sport Trousers
            '137142': 'Activewear',  # Skiwear
            '137143': 'Activewear',  # Performance Jackets
            '137144': 'Activewear',  # Sport Parkas
            '137145': 'Activewear',  # Sport Gilets
            '137146': 'Activewear',  # Running Shorts
            '137147': 'Activewear',  # Compression Shorts
            '137148': 'Activewear',  # Sport T-Shirts
            '137149': 'Activewear',  # Sport Tank Tops
            '137150': 'Activewear',  # Compression Tops
            '137151': 'Activewear',  # Sport Sweatshirts & Hoodies
            '137152': 'Activewear',  # Sport Track Pants
            '137153': 'Activewear',  # Performance Leggings
            '137154': 'Activewear',  # Compression Tights
            '137155': 'Activewear',  # Ski Tops
            '137156': 'Activewear',  # Ski Bottoms
            '137157': 'Activewear',  # Ski Accessories
            '137165': 'Activewear',  # Surf & Swimwear
            '137166': 'Activewear [W]',  # Surf & Swimwear[W]
            '137168': 'Bags [W]',  # Bag Accessories[W]
            '137170': 'Bags [W]',  # Mini Bags[W]
            '137174': 'Sneakers & Trainers',  # Sneakers
            '137188': 'Bags [W]',  # Belt Bags[W]
            '137189': 'Bags [W]',  # Bucket Bags[W]
        }

    def resolve(self, categories, item_id):
        resolved = set()
        for category in categories:
            cat = self.category_dict.get(category, 'Undefined')
            if cat is not 'Undefined':
                resolved.add(cat)

        if len(resolved) == 1:
            return resolved.pop()
        elif len(resolved) == 0:
            self.logger.info('Non of the item ' + str(item_id) + ' categories are defined : ' + str(categories))
        elif len(resolved) > 1:
            self.logger.info('Item ' + str(item_id) + ' has ambiguous category list : ' + str(categories))
        return 'Undefined'


class SJSResolver():
    def __init__(self):
        self.logger = logging.getLogger('category_resolver')
        handler = logging.FileHandler('logs/sjs_categories.log')
        self.logger.addHandler(handler)
        self.category_dict = {
            'Jackets': 'Jackets & Coats',
            'Vests': 'T-shirts',
            'Blazers': 'Jackets & Coats',
            'Lightweight Jackets': 'Jackets & Coats',
            'Military Jackets': 'Jackets & Coats',
            'Denim Jackets': 'Jackets & Coats',
            'Softshell Jackets': 'Jackets & Coats',
            'Tops': 'Hoodies & Sweatshirts',
            'Crewneck Sweatshirts': 'Hoodies & Sweatshirts',
            'Zip Up Hooded Sweatshirts': 'Hoodies & Sweatshirts',
            'Pullover Hooded Sweatshirts': 'Hoodies & Sweatshirts',
            'Zip Up Sweatshirts': 'Hoodies & Sweatshirts',
            'Shirts': 'Shirts',
            'Long Sleeves Shirts': 'Shirts',
            'Short Sleeves Shirts': 'Shirts',
            'T-Shirts': 'T-shirts',
            'Long Sleeves T-Shirts': 'T-shirts',
            'Short Sleeves T-Shirts': 'T-shirts',
            'Polo Shirts': 'T-shirts',
            'Tank Tops': 'T-shirts',
            'Pants': 'Jeans & Trousers',
            'Trousers': 'Jeans & Trousers',
            'Chino Pants': 'Jeans & Trousers',
            '5-Pocket Pants': 'Jeans & Trousers',
            'Sweatpants': 'Jeans & Trousers',
            'Overalls': 'Undefined',  # TODO
            'Cargo Pants': 'Jeans & Trousers',
            'Track Pants': 'Jeans & Trousers',
            'Workpants': 'Jeans & Trousers',
            'Tights': 'Jeans & Trousers',
            'Shorts': 'Shorts',
            'Sweatshorts': 'Shorts',
            'Outerwear': 'Jackets & Coats',
            'Coats': 'Jackets & Coats',
            'Down Vests': 'T-shirts',
            'Anorak Jackets': 'Jackets & Coats',
            'Parkas': 'Jackets & Coats',
            'Coach Jackets': 'Jackets & Coats',
            'Bomber Jackets': 'Jackets & Coats',
            'Down Jackets': 'Jackets & Coats',
            'Leather Jackets': 'Jackets & Coats',
            'Shearling Jackets': 'Jackets & Coats',
            'Knitwear': 'Hoodies & Sweatshirts',
            'Cardigans': 'Hoodies & Sweatshirts',
            'Crewneck Knitwear': 'Hoodies & Sweatshirts',
            'V-Neck Knit': 'Hoodies & Sweatshirts',
            'Knit Vests': 'Hoodies & Sweatshirts',
            'Turtlenecks': 'Hoodies & Sweatshirts',
            'Underwear': 'Underwear',
            'Briefs & Boxers': 'Underwear',
            'Socks': 'Socks',
            'Trunks': 'Swimming stuff',
            'Sneakers': 'Sneakers & Trainers',
            'Slip On': 'Sneakers & Trainers',
            'Low Top': 'Sneakers & Trainers',
            'High Top': 'Sneakers & Trainers',
            'Boots': 'Boots',
            'Chelsea Boots': 'Boots',
            'Laced Boots': 'Boots',
            'Shearling Lined Shoes': 'Shoes',
            'Sandals': 'Sanadals, Sliders & Flip Flops',
            'Slippers': 'Sanadals, Sliders & Flip Flops',
            'Shearling Lined Slippers': 'Sanadals, Sliders & Flip Flops',
            'Loafers': 'Shoes',
            'Lace Ups': 'Shoes',
            'Bags': 'Bags',
            'Totes': 'Bags',
            'Belt Bags': 'Bags',
            'Backpacks': 'Bags',
            'Duffle Bags': 'Bags',
            'Wash Bags': 'Bags',
            'Messenger Bags': 'Bags',
            'Bucket Bags': 'Bags',
            'Belts': 'Belts & Braces',
            'Hats': 'Hats & Caps',
            'Jewellery': 'Not really useful stuff',
            'Keychains': 'Not really useful stuff',
            'Scarves & Gloves': 'Gloves and Scarfs',
            'Sunglasses': 'Glasses',
            'Wallets & Pouches': 'Wallets & Purses',
            'Wallets': 'Wallets & Purses',
            'Cardholders': 'Wallets & Purses',
            'Document Holders': 'Wallets & Purses',
            'Pouches': 'Wallets & Purses',
            'Watches': 'Not really useful stuff',
        }

    def resolve(self, categories, item_id):
        # TODO