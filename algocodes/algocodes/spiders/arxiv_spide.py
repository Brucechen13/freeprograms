# -*- coding:UTF-8 -*-
import json
from algocodes.items import ArxivItem
import scrapy
from scrapy.http import Request
import time

class ArxivSpider(scrapy.Spider):
    name = 'arxiv'

    start_urls = ['https://arxiv.org/list/cs/pastweek?show=100&skip='+str(i)
                  for i in range(0, 900, 100)]

    def parse(self, response):
        base_url = 'https://arxiv.org'
        items = response.css('dt')#.extract()
        for item in items:
            urls = item.xpath('.//span/a/@href').extract()
            new_url = base_url + urls[0]
            item = {'pdf':base_url+urls[1]}
            yield Request(new_url, callback=self.parse_detail, meta=item)

    def parse_detail(self, response):
        #id, title, content, acc, submit, level
        item = ArxivItem()
        item['arxiv_pdfurl'] = response.meta['pdf']
        item['arxiv_title'] = ' '.join(response.xpath('//h1/span').xpath('./parent::*').xpath('./text()').extract())
        item['arxiv_auther'] = ' '.join(response.xpath('//div[@class="authors"]//text()').extract())
        item['arxiv_content'] = ' '.join(response.xpath('//blockquote//text()').extract())
        item['arxiv_subject'] = ' '.join(response.xpath('//span[@class="primary-subject"]//text()').extract())
        s = ' '.join(response.xpath('//div[@class="dateline"]//text()').extract())
        tmp_s = s
        if len(s.split(',')) == 1:
            s = s[14:s.find(')')]
        else:
            s = s.split(',')[1].strip()
            s = s[13:s.find('(t')]
        try:
            day = time.strptime(s.strip(),"%d %b %Y")
        except:
            day = time.strptime(tmp_s,"%d %b %Y")
            print(tmp_s)
        item['arxiv_time'] = time.strftime("%Y-%m-%d %H:%M:%S", day)
        yield item
