# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YanchangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    stime=scrapy.Field()
    address=scrapy.Field()
    city=scrapy.Field()
    yc1=scrapy.Field()
    chengren=scrapy.Field()
    etime=scrapy.Field()
    dazong=scrapy.Field()
    shi=scrapy.Field()
    lishi=scrapy.Field()
    hot=scrapy.Field()