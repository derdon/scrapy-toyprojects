from setuptools import setup

URL = (
    'https://gitlab.informatik.uni-bremen.de/'
    'sliedtke/scrapy-toyprojects/tree/master/zitate')

setup(
    name='quotecrawler',
    version='0.1',
    description='Quote Crawler; uses the German site zitate.de',
    author='Simon Liedtke',
    author_email='sliedtke@uni-bremen.de',
    url=URL,
    packages=['zitate'],
)
