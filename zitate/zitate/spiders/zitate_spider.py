import urlparse

import scrapy


class ZitateSpider(scrapy.Spider):
    name = 'zitate'
    start_urls = [
        'http://www.zitate.de/autor/Adams%2C+Scott',
        'http://www.zitate.de/autor/Allen%2C+Woody',
    ]

    def parse(self, response):
        author = response.url.rstrip('/').split('/')[-1]
        quotes = response.css(
            '.quote-box .quoteinner .quoteleftinner p::text').extract()
        self.log('author: {}'.format(author))
        for quote in quotes:
            yield {'author': author, 'quote': quote}

        cur_page_number = get_page_number(response.url)

        next_page = response.css('.next a::attr(href)').extract_first()
        next_page_number = None
        if next_page is not None:
            next_page_number = get_page_number(next_page)

        # there is always a "next" link, it references to current page
        # if there are no following pages left
        if next_page_number != cur_page_number:
            yield response.follow(next_page, callback=self.parse)


def get_page_number(url):
    'Return the value for the parameter `page` in a URL like `?page=PAGE`'
    page_numbers = urlparse.parse_qs(urlparse.urlparse(url).query).get('page')
    if page_numbers is not None:
        return page_numbers[0]
    return ''
