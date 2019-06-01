# -*- coding:UTF-8 -*-
import json
from algocodes.items import QuestionItem
import scrapy
from scrapy.http import Request
import re
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from algocodes.items import ComicItem

class WxchaSpider(scrapy.Spider):
    name = 'comic'

    start_urls = ['http://www.wxcha.com/zt/list_biaoqing_1.html']


    def parse(self, response):
        # follow links to author pages
        base_url = 'http://www.wxcha.com/zt/list_biaoqing_{0}.html'
        pages = response.xpath('//div[@class="pages"]/a')
        print('page: ', pages)
        for item in range(pages):
            new_url = base_url.format(item)
            yield Request(new_url, callback=self.parse_cur_page)

    def parse_cur_page(self, response):
        items = response.xpath('//div[@class="right960"/ul/li]')
        print('index: ', items)
        for item in items:
            url = item.xpath('./@href').extract_first()
            title = item.xpath('./@title').extract_first()
            new_url = base_url + url
            yield Request(new_url, callback=self.parse_detail, meta={'title':title})

    def parse_detail(self, response):
        base_url = 'http://www.manhuatai.com'
        items = response.xpath('//div[@class="mhlistbody"]/ul[@id="topic1"]/li/a')
        title = response.meta['title']
        for item in items:
            href = item.xpath('./@href').extract_first()
            chapter = item.xpath('./@title').extract_first()
            text = item.xpath('.//text()').extract_first()
            item = self.parse_pic(title, chapter, text, base_url + href)
            yield item

    def parse_pic(self, title, chapter, text, chapter_url):
        # import pdb; pdb.set_trace()
        r_p = r'<option value="(.*?)",*?>第(\d*?/\d*?)页<'
        url_p = r'<img src="(.*?)" onerror'
        pages = []
        item = ComicItem()
        item['comic_title'] = title
        item['comic_chapter'] = text
        try:
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            # 不载入图片，爬页面速度会快很多
            dcap["phantomjs.page.settings.loadImages"] = False
            driver = webdriver.PhantomJS(desired_capabilities=dcap)
            driver.get(chapter_url)
            text=driver.page_source
            pages=re.findall(r_p,text)
            page_url=re.findall(url_p, text)[0]
            item['comic_baseurl'] = page_url
        except Exception:
            print('parse error: ', title, chapter)
            pages = []
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        finally:
            driver.quit()
            print('Got {l} pages in chapter {ch}'.format(l=len(pages),ch=chapter))
            item['comic_page'] = len(pages)
            return item
