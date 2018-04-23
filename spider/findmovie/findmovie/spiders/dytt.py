# -*- coding: utf-8 -*-
import scrapy
from findmovie.items import FindmovieItem
from urllib.parse import urlparse
from urllib.parse import urljoin
import pdb


class DyttSpider(scrapy.Spider):
    name = "dytt"
    allowed_domains = ["dytt8.net"]#,"ygdy8.net"]
#    start_urls = ['http://www.dytt8.net/']#,'http://www.ygdy8.net']#,'http://www.dytt8.net/html/gndy/dyzz/20170524/54065.html']
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
#        items=[]
#        for x in zip(response.xpath('//ul/a/text()').extract(),response.xpath('//ul/a/@href').extract()):
#            print(x)
#            item=FindmovieItem(name=x[0],url=urljoin('http://www.dytt8.net',x[1]))
#            items.append(item)
#        for text in response.xpath('//h1/font/text()').extract():
#                print(text)
#                item=FindmovieItem(name=text)
#                yield item

#        pdb.set_trace()

        for title,content,downloadurl in zip(response.xpath('string(//h1)').extract(),\
                                response.xpath('string(//div[@id="Zoom"]/td/p[1])').extract(),\
                                response.xpath('string(//div[@id="Zoom"]/td/table/tbody/tr/td)').extract()
                                ):
                item=FindmovieItem(name=title,description=content,url=downloadurl)
                print(title)
                if downloadurl!='':
                    yield item
        for url in response.xpath('//a/@href').extract():
                url_1=urlparse(url)
                if url_1.netloc=='' and url_1.scheme=='':
                    url=urljoin('http://www.dytt8.net',url)
                    yield scrapy.Request(url,callback=self.parse)
                elif url_1.scheme=='http':
                    yield scrapy.Request(url,callback=self.parse)
                #print(url)

