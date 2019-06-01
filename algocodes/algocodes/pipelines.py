# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from algocodes.items import QuestionItem, ArxivItem, ComicItem
from algocodes.sql import Sql
import os
import requests


class AlgocodesPipeline(object):
    def process_item(self, item, spider):
        return item

class CodesPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, QuestionItem):
            Sql.insert_problem(item['ques_id'], item['ques_title'], item['ques_content'], item['ques_acc'], item['ques_submit'], item['ques_level'])
        elif isinstance(item, ArxivItem):
            Sql.insert_paper(item['arxiv_title'], item['arxiv_auther'], item['arxiv_content'], item['arxiv_time'],
                             item['arxiv_subject'], item['arxiv_pdfurl'])
        elif isinstance(item, ComicItem):
            path = '/data/' + item['comic_title'] + '/' + item['comic_chapter']
            if not os.path.exists(path):
                os.makedirs(path)
            for page in range(1, item['comic_page']+1):
                pic_url = item['comic_baseurl'].replace('%2F1.jpg', '%2F'+ str(page) +'.jpg')
                res = requests.get(pic_url)
                if(res.status_code != 200):
                    print('parse error ', item['comic_baseurl'], pic_url)
                    return
                with open(os.path.join(path, str(page)+'.jpg'), 'wb') as f:
                    f.write(res.content)

