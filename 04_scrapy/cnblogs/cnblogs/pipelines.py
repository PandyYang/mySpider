# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5

import pymysql
import pymysql.cursors


class CnblogsPipeline:
    def process_item(self, item, spider):
        return item


class JsonWithEncodingCnblogsPipeline(object):
    """
    写入json文件
    """
    def __init__(self):
        self.file = codecs.open('cnblogs.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MySQLStoreCnblogsPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )

        dbpoll = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpoll)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    def _do_upinsert(self, conn, item, spider):

        # 获取link的md5值
        linkmd5id = self._get_linkmd5id(item)
        # print linkmd5id
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        conn.execute("""select * from cnblogsinfo where linkmd5id = "%s"
        """, (linkmd5id,))
        ret = conn.fetchone()

        if ret:
            conn.execute("""update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s""", (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id))
        else:
            conn.execute("""
                        insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
                        values(%s, %s, %s, %s, %s, %s)
                    """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now))

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['link'].encode(encoding='UTF-8')).hexdigest()

    def _handle_error(self, failue, item, spider):
        spider.logger.error('mysql error ： %s' % failue)