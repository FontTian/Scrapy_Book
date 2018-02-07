import scrapy

class ganji(scrapy.Spider):

    name = 'ganji'
    # name 每个爬虫的唯一标识ga
    start_urls = ['http://jn.ganji.com/fang1/o1p1',]

    def parse(self, response):
        for fang in response.xpath('//div[contains(@class,"ershoufang-list")]'):
            title = fang.xpath('./dl/dd[contains(@class,"title")]/a/text()').extract()
            addr = " ".join(fang.xpath('./dl/dd[contains(@class,"address")]/span/a/text()').extract())
            size = fang.xpath('./dl/dd[contains(@class,"size")]/@data-area').extract()
            url = 'http://jn.ganji.com/'+str(fang.xpath('./dl/dd[contains(@class,"title")]/a/@href').extract()[0])
            price = fang.xpath('./dl/dd[contains(@class,"info")]/div/span[contains(@class,"num")]/text()').extract()[0]
            yield {
                'title':title,
                'addr':addr,
                'url':url,
                'size':size,
                'price':price
            }

        # 提取下一页的链接
        next_page = response.xpath("//li/a[@class = 'next']/@href").extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_url, callback=self.parse)