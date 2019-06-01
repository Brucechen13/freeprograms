# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlgocodesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuestionItem(scrapy.Item):
    ques_title = scrapy.Field()
    ques_id = scrapy.Field()
    ques_content = scrapy.Field()
    ques_acc = scrapy.Field()
    ques_submit = scrapy.Field()
    ques_level = scrapy.Field()

class ArxivItem(scrapy.Item):
    arxiv_title = scrapy.Field()
    arxiv_content = scrapy.Field()
    arxiv_auther = scrapy.Field()
    arxiv_time = scrapy.Field()
    arxiv_subject = scrapy.Field()
    arxiv_pdfurl = scrapy.Field()

class ComicItem(scrapy.Item):
    comic_title = scrapy.Field()
    comic_chapter = scrapy.Field()
    comic_page = scrapy.Field()
    comic_baseurl = scrapy.Field()
