# -*- coding:UTF-8 -*-
import json
from algocodes.items import QuestionItem
import scrapy
from scrapy.http import Request

class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'

    start_urls = ['https://leetcode.com/api/problems/algorithms/']


    def parse(self, response):
        # follow links to author pages
        base_url = 'https://leetcode.com/graphql?query=query%20getQuestionDetail(%24titleSlug%3A%20String!)%20%7B%0A%20%20isCurrentUserAuthenticated%0A%20%20question(titleSlug%3A%20%24titleSlug)%20%7B%0A%20%20%20%20questionId%0A%20%20%20%20questionFrontendId%0A%20%20%20%20questionTitle%0A%20%20%20%20translatedTitle%0A%20%20%20%20questionTitleSlug%0A%20%20%20%20content%0A%20%20%20%20translatedContent%0A%20%20%20%20difficulty%0A%20%20%20%20stats%0A%20%20%20%20allowDiscuss%0A%20%20%20%20contributors%0A%20%20%20%20similarQuestions%0A%20%20%20%20mysqlSchemas%0A%20%20%20%20randomQuestionUrl%0A%20%20%20%20sessionId%0A%20%20%20%20categoryTitle%0A%20%20%20%20submitUrl%0A%20%20%20%20interpretUrl%0A%20%20%20%20codeDefinition%0A%20%20%20%20sampleTestCase%0A%20%20%20%20enableTestMode%0A%20%20%20%20metaData%0A%20%20%20%20enableRunCode%0A%20%20%20%20enableSubmit%0A%20%20%20%20judgerAvailable%0A%20%20%20%20infoVerified%0A%20%20%20%20envInfo%0A%20%20%20%20urlManager%0A%20%20%20%20article%0A%20%20%20%20questionDetailUrl%0A%20%20%20%20libraryUrl%0A%20%20%20%20companyTags%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20slug%0A%20%20%20%20%20%20translatedName%0A%20%20%20%20%7D%0A%20%20%20%20topicTags%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20slug%0A%20%20%20%20%20%20translatedName%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20interviewed%20%7B%0A%20%20%20%20interviewedUrl%0A%20%20%20%20companies%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20slug%0A%20%20%20%20%7D%0A%20%20%20%20timeOptions%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20name%0A%20%20%20%20%7D%0A%20%20%20%20stageOptions%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20name%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20subscribeUrl%0A%20%20isPremium%0A%20%20loginUrl%0A%7D%0A&operationName=getQuestionDetail&variables=%7B%22titleSlug%22%3A%22{0}%22%7D'
        res_dt = json.loads(response.text)
        for item in res_dt['stat_status_pairs']:
            new_url = base_url.format(item['stat']['question__title_slug'])
            yield Request(new_url, callback=self.parse_detail, meta=item)

    def parse_detail(self, response):
        #id, title, content, acc, submit, level
        item = QuestionItem()
        content = json.loads(response.text)
        item['ques_id'] = response.meta['stat']['question_id']
        item['ques_title'] = response.meta['stat']['question__title']
        item['ques_content'] = content['data']['question']['content']
        item['ques_acc'] = response.meta['stat']['total_acs']
        item['ques_submit'] = response.meta['stat']['total_submitted']
        item['ques_level'] = response.meta['difficulty']['level']
        yield item
