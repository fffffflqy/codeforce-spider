# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SelfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id = scrapy.Field()
    user_rating = scrapy.Field()
    user_max_rating = scrapy.Field()
    user_Contribution = scrapy.Field()
    user_friends = scrapy.Field()
    user_mail = scrapy.Field()
    image_urls = scrapy.Field()
    image = scrapy.Field()


class FriendsItem(scrapy.Item):
    firend_user = scrapy.Field()
    firend_rating = scrapy.Field()
    firend_max_rating = scrapy.Field()
    firend_Contribution = scrapy.Field()
    firend_firends = scrapy.Field()
    image_urls = scrapy.Field()
    image = scrapy.Field()
