# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZitateItem(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()
