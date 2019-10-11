# -*- coding: utf-8 -*-
import scrapy


class OfertaSpider(scrapy.Spider):
    name = 'oferta'
    allowed_domains = ['www.amazon.es']
    start_urls = ['http://www.amazon.es/']

    def parse(self, response):
        pass
