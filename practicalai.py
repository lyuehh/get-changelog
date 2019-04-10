# -*- coding: utf-8 -*-
import scrapy


class PracticalaiSpider(scrapy.Spider):
    name = 'practicalai'
    #  allowed_domains = ['http://changelog.com']
    start_urls = ['http://changelog.com/practicalai/']

    def parse(self, response):
        for item in response.css('.news_item'):
            yield {
                'title': item.css('.news_item-header .news_item-title a::text').extract_first(),
                'url':  item.css('.news_item-header .news_item-title a::attr(href)').extract_first(),
                'link': item.css('.news_item-toolbar .news_item-toolbar-play_button::attr(href)').extract_first()
            }

        next = response.css('.load_more a::attr(href)').extract_first()
        print('-------')
        print(next)
        if next is not None:
            yield response.follow(next, self.parse)
            #  yield scrapy.Request(next)

