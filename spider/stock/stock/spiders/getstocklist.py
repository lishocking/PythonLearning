# -*- coding: utf-8 -*-
import scrapy
from stock.items import StockItem
from urllib.parse import urlparse
from urllib.parse import urljoin
import pdb
filename="d:/stockdata/stocklist_scrapy.txt"


class GetStockListSpider(scrapy.Spider):
    name = "getstocklist"
    allowed_domains = ["quote.eastmoney.com/"]
    start_urls = ['http://quote.eastmoney.com/stock_list.html']
    
    def parse(self, response):
        #pdb.set_trace()
        f=open(filename,'w')
        for stock_exchange in response.xpath('//div[@class="sltit"]'):

            for title,url in zip(stock_exchange.xpath('following-sibling::ul[1]/li/a[1]/text()').extract(),\
                                    stock_exchange.xpath('following-sibling::ul[1]/li/a[1]/@href').extract(),\
                                    ):
                    print(title,url)

                    name=title.split("(")[0]
                    code=title.split("(")[1][0:-1]
                    stock_exchange_name= stock_exchange.xpath('./a/@name').extract()[0]
                    print(stock_exchange_name)
                    if stock_exchange_name == "sh":
                        f.write(code+".ss.csv"+"\n")
                    elif stock_exchange_name=="sz":
                        f.write(code+".sz.csv"+"\n")
    

        f.close()

