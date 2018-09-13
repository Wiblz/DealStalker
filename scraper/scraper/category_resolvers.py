
class FarfetchResolver:
    def __init__(self):
        self.category_dict = {
            135970 : 'Bags',  # Bags
            135971 : 'Bags [W]', # Bags[W]
            135972 : 'Undefined', # Accessories TODO
            135973 : 'Undefined', # Accessories[W] TODO
            135974 : 'Undefined', # Lifestyle TODO
            135979 : 'Dresses [W]', # Dresses[W]
            135981 : 'Jeans & Trousers [W]', # Pants[W]
            135983 : 'Tops [W]', # Tops[W]
            135985 : 'Skirts [W]', # Skirts[W]
            135996 : 'Sanadals, Sliders & Flip Flpos', # Slippers
            135998 : 'Bags', # Clutch Bags
            135999 : 'Bags [W]', # Clutch Bags[W]
            136000 : 'Belts & Braces', # Belts
            136001 : 'Belts & Braces [W]', # Belts[W]
            136002 : 'Gloves and Scarfs', # Scarves
            136003 : 'Gloves and Scarfs [W]', # Scarves[W]
            136004 : 'Ties', # Ties & Bow Ties
            136006 : 'Hats & Caps', # Hats
            136010 : 'Ambiguous', # Keyrings & Chains TODO
            136011 : 'Not really useful stuff [W]', # Keyrings & Chains[W]
            136014 : 'Undefined', # Laptop Bags & Briefcases TODO
            136032 : 'Bags', # Tote Bags
            136033 : 'Bags [W]', # Tote Bags[W]
            136034 : 'Bags', # Shoulder bags
            136035 : 'Bags [W]', # Shoulder Bags[W]
            136043 : 'Undefined', # Denim[W] TODO
            136045 : 'Shorts [W]', # Shorts[W]
            136069 : 'Hair accessories [W]', # Hair Accessories[W]
            136071 : 'Lingerie & Nightwear & Kimonos [W]', # Lingerie[W]
            136089 : 'Jeans & Trousers [W]', # Leggings[W]
            136091 : 'T-shirts [W]', # T-Shirts & Jersey Shirts[W]
            136093 : 'Tops [W]', # Polo Tops[W]
            136099 : 'Shirts [W]', # Shirts[W]
            136101 : 'Tops [W]', # Blouses[W]
            136103 : 'Skirts [W]', # A-Line Skirts[W]
            136105 : 'Skirts [W]', # Asymmetric & Draped Skirts[W]
            136107 : 'Skirts [W]', # High-Waisted Skirts[W]
            136137 : 'Hoodies & Sweatshirts [W]', # Vests & Tank Tops[W]
            136147 : 'Undefined', # Cardigans[W] TODO
            136149 : 'Hoodies & Sweatshirts [W]', # Sweaters[W]
            136157 : 'Hoodies & Sweatshirts [W]', # Hoodies[W]
            136175 : 'Jeans & Trousers [W]', # Skinny Jeans[W]
            136177 : 'Jeans & Trousers [W]', # Bootcut Jeans[W]
            136179 : 'Jeans & Trousers [W]', # Straight-Leg Jeans[W]
            136181 : 'Jeans & Trousers [W]', # Wide-Leg Jeans[W]
            136183 : 'Jeans & Trousers [W]', # Flares & Bell Bottom Jeans[W]
            136185 : 'Jeans & Trousers [W]', # Boyfriend Jeans[W]
            136187 : 'Jeans & Trousers [W]', # Tapered Jeans[W]
            136189 : 'Dresses [W]', # Day Dresses[W]
            136191 : 'Dresses [W]', # Evening Dresses[W]
            136193 : 'Dresses [W]', # Cocktail & Party Dresses[W]
            136212 : 'Undefined', # Vintage[W] TODO
            136214 : 'Undefined', # Vintage Bags[W] TODO
            136225 : 'Dresses [W]', # Sundresses[W]
            136226 : 'Jackets & Coats [W]', # Jackets[W]
            136227 : 'Jackets & Coats [W]', # Coats[W]
            136238 : 'Jackets & Coats [W]', # Capes[W]
            136239 : 'Jackets & Coats [W]', # Double Breasted & Peacoats[W]
            136240 : 'Jackets & Coats [W]', # Fur & Shearling Coats[W]
            136241 : 'Jackets & Coats [W]', # Leather Coats[W]
            136242 : 'Jackets & Coats [W]', # Military Coats[W]
            136243 : 'Jackets & Coats [W]', # Parkas[W]
            136244 : 'Jackets & Coats [W]', # Trench Coats & Raincoats[W]
            136245 : 'Undefined', # Knitwear[W] TODO
            136246 : 'Hoodies & Sweatshirts [W]', # Cardi-Coats[W]
            136247 : 'Hoodies & Sweatshirts [W]', # Cardigans[W]
            136248 : 'Dresses [W]', # Sweater Dresses[W]
            136249 : 'Jeans & Trousers [W]', # Knitted Leggings[W]
            136250 : 'Skirts [W]', # Knitted Skirts[W]
            136251 : 'Hoodies & Sweatshirts [W]', # Knitted Sweaters[W]
            136252 : 'Hoodies & Sweatshirts [W]', # Knitted Tops[W]
            136253 : 'Undefined', # Jumpsuits & All in ones[W] TODO
            136254 : 'Dresses [W]', # Jumpsuits[W]
            136255 : 'Dresses [W]', # Playsuits[W]
            136257 : 'Jeans & Trousers [W]', # Cropped Jeans[W]
            136258 : 'Jackets & Coats [W]', # Denim Jackets[W]
            136259 : 'Jeans & Trousers [W]', # Denim Leggings[W]
            136260 : 'Shirts [W]', # Denim Shirts[W]
            136261 : 'Shorts [W]', # Jean Shorts[W]
            136262 : 'Skirts [W]', # Denim Skirts[W]
            136263 : 'Jeans & Trousers [W]', # Cropped Pants[W]
            136264 : 'Jeans & Trousers [W]', # Flared & Bell-Bottom Pants[W]
            136265 : 'Jeans & Trousers [W]', # High Waisted Pants[W]
            136266 : 'Jeans & Trousers [W]', # Capri Pants[W]
            136267 : 'Jeans & Trousers [W]', # Skinny Pants[W]
            136268 : 'Jeans & Trousers [W]', # Slim Pants[W]
            136269 : 'Jeans & Trousers [W]', # Straight-Leg Pants[W]
            136270 : 'Jeans & Trousers [W]', # Slacks[W]
            136271 : 'Jeans & Trousers [W]', # Tapered Pants[W]
            136272 : 'Jeans & Trousers [W]', # Sweatpants[W]
            136273 : 'Jeans & Trousers [W]', # Palazzo Pants[W]
            136274 : 'Shorts [W]', # Short Shorts[W]
            136275 : 'Shorts [W]', # Knee-Length Shorts[W]
            136276 : 'Skirts [W]', # Pencil Skirts[W]
            136277 : 'Skirts [W]', # Pleated Skirts[W]
            136278 : 'Skirts [W]', # Straight Skirts[W]
            136279 : 'Skirts [W]', # Full Skirts[W]
            136285 : 'Underwear [W]', # Bodies[W] TODO
            136286 : 'Bra [W]', # Bras[W]
            136287 : 'Underwear [W]', # Panties[W] TODO
            136288 : 'Loungewear [W]', # Loungewear[W]
            136289 : 'Lingerie & Nightwear & Kimonos [W]', # Nightwear[W]
            136290 : 'Socks & Tights [W]', # Socks[W]
            136291 : 'Socks & Tights [W]', # Pantyhose & Stockings[W]
            136292 : 'Bra [W]', # Camisoles & Corsets[W]
            136293 : 'Undefined', # Beachwear[W] TODO
            136294 : 'Swimming wear [W]', # Bikinis[W]
            136295 : 'Dresses [W]', # Beach Dresses[W]
            136296 : 'Swimming wear [W]', # Beach Accessories[W]
            136298 : 'Undefined', # Beach Cover-Ups[W] TODO
            136300 : 'Swimming wear [W]', # Swimsuits[W]
            136302 : 'Boots [W]', # Boots[W]
            136303 : 'Shoes [W]', # BROGUES & OXFORDS[W]
            136304 : 'Sanadals, Sliders & Flip Flpos [W]', # ESPADRILLES[W]
            136305 : 'Sanadals, Sliders & Flip Flpos [W]', # Flip flops & Slides [W]
            136306 : 'Shoes [W]', # Loafers[W]
            136307 : 'Shoes [W]', # Pumps[W]
            136308 : 'Sanadals, Sliders & Flip Flpos [W]', # Sandals[W]
            136309 : 'Sanadals, Sliders & Flip Flpos [W]', # Slippers[W]
            136310 : 'Sneakers & Trainers [W]', # Sneakers[W]
            136311 : 'Bags [W]', # Backpacks[W]
            136312 : 'Undefined', # Luggage[W] TODO
            136315 : 'Bags [W]', # Messenger & Crossbody Bags[W]
            136321 : 'Glasses [W]', # GLASSES & FRAMES[W]
            136322 : 'Glasses [W]', # Sunglasses[W]
            136323 : 'Hats & Caps [W]', # Hats[W]
            136324 : 'Gloves and Scarfs [W]', # Gloves[W]
            136325 : 'Bags [W]', # Make Up Bags[W]
            136326 : 'Wallets & Purses [W]', # Wallets & Purses[W]
            136331 : 'Shirts', # Shirts
            136332 : 'T-shirts', # T-shirts & Vests
            136333 : 'Shirts', # Polo Shirts
            136334 : 'Hoodies & Sweatshirts', # Sweaters & Knitwear
            136335 : 'Jackets & Coats', # Jackets
            136336 : 'Jackets & Coats', # Coats
            136337 : 'Undefined', # Denim TODO
            136338 : 'Jeans & Trousers', # Pants
            136339 : 'Shorts', # Shorts
            136340 : 'Undefined', # Suits
            136341 : 'Undefined', # Underwear & Socks TODO
            136342 : 'Undefined', # Beachwear TODO
            136353 : 'Boots', # Boots
            136354 : 'Shoes', # Brogues
            136355 : 'Shoes', # Boat & Deck shoes
            136356 : 'Sanadals, Sliders & Flip Flpos', # Espadrilles
            136357 : 'Sanadals, Sliders & Flip Flpos', # Flip Flops & Slides
            136358 : 'Shoes', # Lace-up Shoes
            136359 : 'Shoes', # Loafers
            136360 : 'Sanadals, Sliders & Flip Flpos', # Sandals
            136361 : 'Sneakers & Trainers', # Low-Tops
            136362 : 'Bags', # Backpacks
            136363 : 'Bags', # Holdalls
            136364 : 'Bags', # Messenger Bags
            136370 : 'Belts & Braces', # Braces
            136371 : 'Glasses', # Glasses & Frames
            136372 : 'Gloves and Scarfs', # Gloves
            136373 : 'Glasses', # Sunglasses
            136374 : 'Undefined', # Wash Bags TODO
            136375 : 'Wallets & Purses', # Wallets & Billfolds
            136377 : 'Undefined', # Phone Cases & Technology TODO
            136381 : 'Undefined', # Umbrellas TODO
            136394 : 'T-shirts', # T-Shirts
            136395 : 'T-shirts', # Vests & Tank Tops
            136396 : 'Hoodies & Sweatshirts', # Knitted Sweaters
            136397 : 'Hoodies & Sweatshirts', # Sweatshirts
            136398 : 'Hoodies & Sweatshirts', # Hoodies
            136399 : 'Hoodies & Sweatshirts', # Cardigans
            136400 : 'Jackets & Coats', # Biker Jackets
            136401 : 'Undefined', # Lightweight Jackets TODO
            136402 : 'Undefined', # Blazers TODO
            136403 : 'Ambiguous', # Denim Jackets TODO
            136404 : 'Undefined', # Hooded Jackets TODO
            136405 : 'Undefined', # Leather Jackets TODO
            136406 : 'Undefined', # Military Jackets TODO
            136407 : 'Jackets & Coats [W]', # Down Jackets
            136408 : 'Undefined', # Shirt Jackets TODO
            136409 : 'Undefined', # Sport Jackets & Wind Breakers TODO
            136410 : 'Undefined', # Suit & Dinner Jackets TODO
            136411 : 'Undefined', # Waistcoats & Gilets TODO
            136412 : 'Jackets & Coats', # Double Breasted & Peacoats
            136413 : 'Jackets & Coats', # Hooded Coats
            136414 : 'Jackets & Coats', # Leather Coats
            136415 : 'Jackets & Coats', # Military Coats
            136416 : 'Jackets & Coats', # Down Coats
            136417 : 'Jackets & Coats', # Parkas & Duffle Coats
            136418 : 'Jackets & Coats', # Single-Breasted Coats
            136419 : 'Jackets & Coats', # Trench Coats & Macs
            136420 : 'Jeans & Trousers', # Bootcut Jeans
            136421 : 'Jeans & Trousers', # Cropped Jeans
            136422 : 'Jeans & Trousers', # Drop-Crotch Jeans
            136423 : 'Jeans & Trousers', # Relaxed-Fit Jeans
            136424 : 'Jeans & Trousers', # Regular & Straight-Leg Jeans
            136425 : 'Jeans & Trousers', # Skinny Jeans
            136426 : 'Jeans & Trousers', # Slim-Fit Jeans
            136427 : 'Jeans & Trousers', # Tapered Jeans
            136428 : 'Jeans & Trousers', # Wide-Leg Jeans
            136429 : 'Jackets & Coats', # Denim Jackets
            136430 : 'Shirts', # Denim Shirts
            136431 : 'Shorts', # Denim Shorts
            136432 : 'Jeans & Trousers', # Chinos
            136433 : 'Jeans & Trousers', # Cropped Pants
            136434 : 'Jeans & Trousers', # Drop Crotch Pants
            136435 : 'Jeans & Trousers', # Leggings
            136436 : 'Jeans & Trousers', # Loose Fit Pants
            136437 : 'Jeans & Trousers', # Regular-Fit & Straight Leg Pants
            136438 : 'Jeans & Trousers', # Skinny Pants
            136439 : 'Jeans & Trousers', # Tailored Pants
            136440 : 'Jeans & Trousers', # Tapered Pants
            136441 : 'Jeans & Trousers', # Sweatpants
            136442 : 'Jeans & Trousers', # Wide Leg Pants
            136443 : 'Shorts', # Bermuda Shorts
            136444 : 'Shorts', # Cargo Shorts
            136445 : 'Shorts', # Khaki Shorts
            136446 : 'Shorts', # Deck Shorts
            136447 : 'Shorts', # Denim Shorts
            136448 : 'Shorts', # Drop-Crotch Shorts
            136449 : 'Shorts', # Tailored Shorts
            136450 : 'Shorts', # Track & Running Shorts
            136451 : 'Undefined', # Formal Suits TODO
            136452 : 'Undefined', # Dinner Suits TODO
            136453 : 'Undefined', # Suit Jackets TODO
            136455 : 'Undefined', # Jumpsuits
            136457 : 'Loungewear', # Loungewear
            136458 : 'Loungewear', # Sleepwear
            136459 : 'Socks', # Socks
            136460 : 'Underwear', # Briefs & Boxers TODO
            136461 : 'Activewear', # Beach Accessories
            136463 : 'Swimming stuff', # Swimming Trunks
            136465 : 'Swimming stuff', # Swim & Board Shorts
            136466 : 'Tops [W]', # Tunic Tops & Kaftans[W]
            136467 : 'Shoes [W]', # Mules[W]
            136468 : 'Jackets & Coats', # Bomber Jackets
            136481 : 'Jackets & Coats [W]', # Single Breasted Coats[W]
            136484 : 'Shoes [W]', # Ballerina Shoes[W]
            136485 : 'Shoes [W]', # Lace-up shoes[W]
            136487 : 'Shoes', # Monk Shoes
            136488 : 'Skirts [W]', # Fitted Skirts[W]
            136489 : 'Sneakers & Trainers', # Hi-Tops
            136497 : 'Jackets & Coats [W]', # Oversized Coats[W]
            136498 : 'Shoes', # Oxford Shoes
            136499 : 'Shoes', # Derby Shoes
            137116 : 'Activewear', # Activewear
            137117 : 'Undefined', # Activewear[W] TODO
            137118 : 'Undefined', # Sport Jackets[W] TODO
            137119 : 'Undefined', # Sport Shorts[W] TODO
            137120 : 'Undefined', # Sport Trousers[W] TODO
            137121 : 'Undefined', # Sport Tops[W] TODO
            137122 : 'Undefined', # Performance Jackets[W] TODO
            137123 : 'Undefined', # Sport Parkas[W] TODO
            137124 : 'Undefined', # Sport Gilets[W] TODO
            137125 : 'Undefined', # Running Shorts[W] TODO
            137126 : 'Undefined', # Compression Shorts[W] TODO
            137127 : 'Undefined', # Sport Track Pants[W] TODO
            137128 : 'Undefined', # Performance Leggings[W] TODO
            137129 : 'Undefined', # Compression Tights[W] TODO
            137130 : 'Undefined', # Compression Tops[W] TODO
            137131 : 'Undefined', # Sport T-Shirts[W] TODO
            137132 : 'Undefined', # Sport Tank Tops[W] TODO
            137133 : 'Undefined', # Sport Sweatshirts & Hoodies[W] TODO
            137134 : 'Undefined', # Skiwear[W] TODO
            137135 : 'Undefined', # Ski Tops[W] TODO
            137136 : 'Undefined', # Ski Bottoms[W] TODO
            137137 : 'Undefined', # Ski Accessories[W] TODO
            137138 : 'Undefined', # Sport Jackets TODO
            137139 : 'Undefined', # Sport Shorts TODO
            137140 : 'Undefined', # Sport Tops TODO
            137141 : 'Undefined', # Sport Trousers TODO
            137142 : 'Undefined', # Skiwear TODO
            137143 : 'Undefined', # Performance Jackets TODO
            137144 : 'Undefined', # Sport Parkas TODO
            137145 : 'Undefined', # Sport Gilets TODO
            137146 : 'Undefined', # Running Shorts TODO
            137147 : 'Undefined', # Compression Shorts TODO
            137148 : 'Undefined', # Sport T-Shirts TODO
            137149 : 'Undefined', # Sport Tank Tops TODO
            137150 : 'Undefined', # Compression Tops TODO
            137151 : 'Undefined', # Sport Sweatshirts & Hoodies TODO
            137152 : 'Undefined', # Sport Track Pants TODO
            137153 : 'Undefined', # Performance Leggings TODO
            137154 : 'Undefined', # Compression Tights TODO
            137155 : 'Undefined', # Ski Tops TODO
            137156 : 'Undefined', # Ski Bottoms TODO
            137157 : 'Undefined', # Ski Accessories TODO
            137165 : 'Undefined', # Surf & Swimwear TODO
            137166 : 'Undefined', # Surf & Swimwear[W] TODO
            137168 : 'Bags [W]', # Bag Accessories[W]
            137170 : 'Bags [W]', # Mini Bags[W]
            137174 : 'Sneakers & Trainers', # Sneakers
            137188 : 'Undefined', # Belt Bags[W] TODO
            137189 : 'Undefined', # Bucket Bags[W] TODO
        }

    def resolve(self, category):
        # TODO Farfetch items often have more than 1 category. We have to use something more fancy here.
        if category in self.category_dict:
            return self.category_dict['category']
        else:
            return 'Undefined'
