import scrapy


class ZitateSpider(scrapy.Spider):
    name = 'zitate'
    start_urls = [
        'http://www.zitate.de/autor/Adams%2C+Scott',
        'http://www.zitate.de/autor/Anonym'
    ]

    def parse(self, response):
        author = response.url.rstrip('/').split('/')[-1]
        quotes = response.css(
            '.quote-box .quoteinner .quoteleftinner p::text').extract()
        self.log('author: {}'.format(author))
        for quote in quotes:
            yield {'author': author, 'quote': quote}
