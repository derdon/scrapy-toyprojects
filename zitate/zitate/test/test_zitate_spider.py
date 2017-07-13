from pytest import fixture

from zitate.spiders.zitate_spider import get_author, get_page_number


@fixture
def url_with_page_num(request):
    return 'http://www.zitate.de/autor/Allen%2C+Woody?page=2'


@fixture
def url_without_page_num(request):
    return 'http://www.zitate.de/autor/Allen%2C+Woody'


def test_get_author_with_page_num(url_with_page_num):
    assert get_author(url_with_page_num) == 'Allen, Woody'


def test_get_author_without_page_num(url_without_page_num):
    assert get_author(url_without_page_num) == 'Allen, Woody'


def test_get_page_number(url_with_page_num):
    assert get_page_number(url_with_page_num) == '2'


def test_get_page_number_none_given(url_without_page_num):
    assert get_page_number(url_without_page_num) == ''
