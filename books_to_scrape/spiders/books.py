# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    # 爬虫名
    name = 'books'
    # 允许的域名范围
    allowed_domains = ['books.toscrape.com']
    # 起始爬去页面
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # 1.提取数据
        for sel in response.css('article.product_pod'):
            name = sel.xpath('./h3/a/@title').extract_first()
            price = sel.css('p.price_color::text').extract_first()
            rating = sel.css('p.star-rating').re_first('star-rating (\w+)')

            book = {'name': name,
                    'price': price,
                    'rating': rating}
            yield book
        # 2.提取链接，产生新的请求
        url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if url:
            # 合并url
            url = response.urljoin(url)
            request = scrapy.Request(url, self.parse)
            yield request