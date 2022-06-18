import scrapy
from scrapy.crawler import CrawlerProcess
from random import randrange
import html2text

h = html2text.HTML2Text()
h.ignore_links = True


targetURLs = [
    "https://www.allrecipes.com/sitemaps/recipe/1/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/2/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/3/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/4/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/5/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/6/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/7/sitemap.xml",
    "https://www.allrecipes.com/sitemaps/recipe/8/sitemap.xml",
]

class Playbook(scrapy.Spider):
    name = "PostcodesSpider"

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'Data_New.csv',
        # 'CONCURRENT_REQUESTS': '1',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'ROBOTSTXT_OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8-sig'
    }

    def start_requests(self):
        for url in targetURLs:
            yield scrapy.Request(url=url,
                             callback=self.parse, dont_filter=True,
                             headers={
                                 'USER-AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                               "like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                             },
                             )

    def parse(self, response):
        data = response.text
        data = data.split("<loc>")
        data = data[1:]
        data = [d.split("</loc>")[0].strip() for d in data]
        recipesURLs = data
        # recipesURLs = response.css("loc::text").extract()
        # print(recipesURLs)
        for recipe in recipesURLs:
            yield scrapy.Request(url=recipe,
                                 callback=self.parse2, dont_filter=True,
                                 headers={
                                     'USER-AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                                   "like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                                 },
                                 )

    def parse2(self, response):
        name = response.css("h1::text").extract_first()
            
        metaInfo = response.css("div.recipe-meta-item").extract()
        metaInfoExtracted = []
        
        categories = response.css("span.breadcrumbs__title::text").extract()

        MainCategory = categories[2]
        try:
            SubCategory = categories[3]
        except:
            SubCategory = ""
        try:
            SubCategory_2 = categories[4]
        except:
            SubCategory_2 = ""

        prep = ""
        cookingTime = ""
        total = ""
        serving = ""
        yield_ = ""

        for item in metaInfo:
            itemData = h.handle(item)

            key = itemData.split(":")[0].replace("*", "").strip()
            value = itemData.split(":")[-1].replace("*", "").strip()
            # print([key, value])



            if "prep" in key.lower():
                prep = value
            elif "cook" in key.lower():
                cookingTime = value
            elif "total" in key.lower():
                total = value
            elif "serving" in key.lower():
                serving = value
            elif "yield" in key.lower():
                yield_ = value


        ingredients = response.css("span.ingredients-item-name::text").extract()
        ingredients = [x.strip() for x in ingredients]
        ingredients = [x.replace("\n", ", ") for x in ingredients]
        ingredients = [x for x in ingredients if x != ""]

        try:
            ingredient_1 = ingredients[0]
        except:
            ingredient_1 = ""
        
        try:
            ingredient_2 = ingredients[1]
        except:
            ingredient_2 = ""

        try:
            ingredient_3 = ingredients[2]
        except:
            ingredient_3 = ""

        try:
            ingredient_4 = ingredients[3]
        except:
            ingredient_4 = ""

        try:
            ingredient_5 = ingredients[4]
        except:
            ingredient_5 = ""
        
        try:
            ingredient_6 = ingredients[5]
        except:
            ingredient_6 = ""

        try:
            ingredient_7 = ingredients[6]
        except:
            ingredient_7 = ""

        try:
            ingredient_8 = ingredients[7]
        except:
            ingredient_8 = ""

        try:
            ingredient_9 = ingredients[8]
        except:
            ingredient_9 = ""


        try:
            ingredient_10 = ingredients[9] 
        except:
            ingredient_10 = ""


        try:
            ingredient_11 = ingredients[10]
        except:
            ingredient_11 = ""


        try:
            ingredient_12 = ingredients[11]
        except:
            ingredient_12 = ""


        try:
            ingredient_13 = ingredients[12]
        except:
            ingredient_13 = ""


        try:
            ingredient_14 = ingredients[13]
        except:
            ingredient_14 = ""


        try:
            ingredient_15 = ingredients[14]
        except:
            ingredient_15 = ""


        try:
            ingredient_16 = ingredients[15]
        except:
            ingredient_16 = ""


        try:
            ingredient_17 = ingredients[16]
        except:
            ingredient_17 = ""


        try:
            ingredient_18 = ingredients[17]
        except:
            ingredient_18 = ""


        try:
            ingredient_19 = ingredients[18]
        except:
            ingredient_19 = ""


        try:
            ingredient_20 = ingredients[19]
        except:
            ingredient_20 = ""


        try:
            ingredient_21 = ingredients[20]
        except:
            ingredient_21 = ""


        try:
            ingredient_22 = ingredients[21]
        except:
            ingredient_22 = ""


        try:
            ingredient_23 = ingredients[22]
        except:
            ingredient_23 = ""


        try:
            ingredient_24 = ingredients[23]
        except:
            ingredient_24 = ""


        try:
            ingredient_25 = ingredients[24]
        except:
            ingredient_25 = ""


        try:
            ingredient_26 = ingredients[25]
        except:
            ingredient_26 = ""


        try:
            ingredient_27 = ingredients[26]
        except:
            ingredient_27 = ""


        try:
            ingredient_28 = ingredients[27]
        except:
            ingredient_28 = ""


        try:
            ingredient_29 = ingredients[28]
        except:
            ingredient_29 = ""


        try:
            ingredient_30 = ingredients[29]
        except:
            ingredient_30 = ""

        yield {
            'Category': MainCategory, 'Subcategory_1': SubCategory, 'Subcategory_2': SubCategory_2, 'Name': name, 'Prep': prep, 'Cooking Time': cookingTime, 'Total': total, 'Serving': serving, 'Yield': yield_, 'URL': response.url, 
            'Ingredient_1': ingredient_1, 'Ingredient_2': ingredient_2, 'Ingredient_3': ingredient_3, 'Ingredient_4': ingredient_4, 'Ingredient_5': ingredient_5, 'Ingredient_6': ingredient_6, 'Ingredient_7': ingredient_7, 'Ingredient_8': ingredient_8, 'Ingredient_9': ingredient_9,
            'Ingredient_10': ingredient_10, 'Ingredient_11': ingredient_11, 'Ingredient_12': ingredient_12, 'Ingredient_13': ingredient_13, 'Ingredient_14': ingredient_14, 'Ingredient_15': ingredient_15, 'Ingredient_16': ingredient_16, 'Ingredient_17': ingredient_17, 
            'Ingredient_18': ingredient_18, 'Ingredient_19': ingredient_19, 'Ingredient_20': ingredient_20, 'Ingredient_21': ingredient_21, 'Ingredient_22': ingredient_22, 'Ingredient_23': ingredient_23, 'Ingredient_24': ingredient_24, 'Ingredient_25': ingredient_25,
            'Ingredient_26': ingredient_26, 'Ingredient_27': ingredient_27, 'Ingredient_28': ingredient_28, 'Ingredient_29': ingredient_29, 'Ingredient_30': ingredient_30
        }


process = CrawlerProcess()
process.crawl(Playbook)
process.start()