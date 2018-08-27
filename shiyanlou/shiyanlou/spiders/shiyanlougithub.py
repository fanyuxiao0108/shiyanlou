# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepositoryItem

class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for user in response.css('li.col-12'):
            item = RepositoryItem({
                'name': user.xpath('.//a/text()').extract_first().strip(),
                'update_time': user.xpath('.//relative-time/@datetime').extract_first()
                })

            yield item
