from string import ascii_uppercase as letters

try:
    from urllib.parse import urlparse, parse_qs, unquote_plus
except ImportError:
    from urlparse import urlparse, parse_qs, unquote_plus

import scrapy

from zitate.items import ZitateItem


class ZitateSpider(scrapy.Spider):
    name = 'zitate'
    start_urls = [
        'http://www.zitate.de/autoren'
    ]

    def parse_author(self, response):
        'Parse pages like /autor/Engelhardt%2C+Nicole'
        author = get_author(response.url)
        quotes = response.css(
            '.quote-box .quoteinner .quoteleftinner p::text').extract()
        for quote in quotes:
            yield ZitateItem(author=author, quote=quote)

        cur_page_number = get_page_number(response.url)
        next_page = response.css('.next a::attr(href)').extract_first()
        next_page_number = None
        if next_page is not None:
            next_page_number = get_page_number(next_page)

        # there is always a "next" link, it references to current page
        # if there are no following pages left
        if next_page_number != cur_page_number:
            yield response.follow(next_page, callback=self.parse)

    def parse(self, response):
        'Collect all links to authors and parse them via parse_author'
        css_format = '#fragment-{} .row .span4 ul li a::attr(href)'
        css_codes = [css_format.format(letter) for letter in letters]
        for css in css_codes:
            authors = response.css(css)
            for author in authors:
                yield response.follow(author, callback=self.parse_author)


def get_author(url):
    return unquote_plus(urlparse(url).path.split('/')[-1])


def get_page_number(url):
    'Return the value for the parameter `page` in a URL like `?page=PAGE`'
    page_numbers = parse_qs(urlparse(url).query).get('page')
    if page_numbers is not None:
        return page_numbers[0]
    return ''
