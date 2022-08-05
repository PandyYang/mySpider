import scrapy
from scrapy.selector import Selector
from scrapy.spiders import Rule
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from ..items import CnblogsItem


class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/richerdyoung/default.html?page=1"]

    rules = [
        Rule(
            LinkExtractor(allow=(r"/richerdyoung/default.html\?page=\d{1,}")), follow=True, callback='parse_item'
        )
    ]

    def parse(self, response, **kwargs):
        sel = Selector(response)
        base_url = get_base_url(response)
        post_title = sel.css('div.day div.postTitle')
        post_con = sel.css('div.postCon div.c_b_p_desc')
        items = []

        for index in range(len(post_title)):
            item = CnblogsItem()
            item['title'] = post_title[index].css('a').xpath('text()').extract()[0]
            item['link'] = post_title[index].css('a').xpath('@href').extract()[0]
            item['listUrl'] = base_url
            item['desc'] = post_con[index].xpath('text()').extract()[0]
            items.append(item)
        return items
