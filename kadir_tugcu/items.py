# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KadirTugcuItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    answer = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    publish_date = scrapy.Field()