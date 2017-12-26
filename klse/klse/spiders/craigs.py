import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quote3"

    def start_requests(self):
        urls = [
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=CLOSED-FUND',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=CONSTRUCTION',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=TRAD-SERV',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=INDUSTRIAL',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=CONSUMER',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=PROPERTIES',
            'http://www.malaysiastock.biz/Market-Watch.aspx?type=C&value=FINANCE',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            yield {
                'title': response.xpath('//table[@id="MainContent_tbStockWithAlphabet"]/tr/td/span/a/text()').extract(),
                #'sector': response.xpath('//table/tr/td[@class="filteringSelection2"]/a/text()').extract(),
                #'alphabet': response.xpath('//table/tr/td[@class="filteringSelection"]/a/text()').extract(),
            }