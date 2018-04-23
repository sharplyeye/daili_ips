# -*- coding: utf-8 -*-
import scrapy
from daili_ips.items import DailiIpsItem
import requests


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def start_requests(self):
        res = []
        for i in range(1, 2):
            url = 'http://www.xicidaili.com/nn/%d' % i
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            res.append(req)
        return res

    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]  # 去掉标题行
        items = []
        for tr in trs:
            pre_item = DailiIpsItem()
            pre_item['ip'] = tr.xpath('td[2]/text()').extract()[0]
            pre_item['port'] = tr.xpath('td[3]/text()').extract()[0]
            pre_item['position'] = tr.xpath('string(td[4])').extract()[0].strip()
            pre_item['type'] = tr.xpath('td[6]/text()').extract()[0]
            pre_item['speed'] = tr.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            pre_item['last_check_time'] = tr.xpath('td[10]/text()').extract()[0]
            items.append(pre_item)
            # proxies={type:pre_item['ip']+pre_item['port']}
            # try:
            #     # 设置代理链接百度  如果状态码为200 则表示该代理可以使用 然后交给流水线处理
            #     if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
            #         print('success %s' % pre_item['ip'])
            #
            #         return items
            # except:
            #     print('fail %s'%pre_item['ip'])
        return items
