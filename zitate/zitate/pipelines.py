# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class ZitateSQLitePipeline(object):
    def __init__(self, dbname):
        self.dbname = dbname
        self.db = None  # start database connection only if necessary

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('DATABASE_NAME'))

    def open_spider(self, spider):
        self.db = sqlite3.connect(self.dbname)

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        # make sure the table exists in the database, create if necessary
        self.db.execute(
                'CREATE TABLE IF NOT EXISTS zitate (author text, zitat text);')
        self.db.executemany('INSERT INTO zitate VALUES (?, ?)', item.items())
        self.db.commit()
        return item
