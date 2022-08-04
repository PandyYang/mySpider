import scrapy


class QuotesSpider(scrapy.Spider):
    # 标识蜘蛛。它在一个项目中必须是唯一的，即不能为不同的爬行器设置相同的名称。
    name = "quotes"

    """
    必须返回请求的可迭代(您可以返回请求列表或编写生成器函数)，爬行器将从该请求开始爬行。后续请求将从这些初始请求中相继生成。
    也可以不用实现start_requests, 在name下方定义start_urls即可.此列表将由的默认实现使用 start_requests() 要为爬行器创建初始请求
    """
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    """
    将被调用以处理为每个请求下载的响应的方法。Response参数是 TextResponse 它保存页面内容，并具有进一步有用的方法来处理它。
    这个 parse() 方法通常解析响应，将抓取的数据提取为字典，还查找要遵循的新URL并创建新请求 (Request )。
    """
    def parse(self, response, **kwargs):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # 追踪下一个页面
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)