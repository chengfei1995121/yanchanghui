# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors

class MySQLyanchangPipeline(object):
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
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item)
        #d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    #将每行更新或写入数据库中
    def _do_upinsert(self, conn, item):
           
            """sql="select * from infotable where 事件名称='%s'" % (item['title'])
            n=conn.execute(sql)
            if n:
                print "yes"
            else:"""
            sql = "insert into infotable(事件名称,开始日期,结束日期,举办城市,主要影响成人,是否是演唱会,是否影响社会大众,最大影响全市,事件历史悠久程度,事件热度) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            params = (item['title'],item['stime'],item['etime'],item['city'],item['chengren'],item['yc1'],item['dazong'],item['shi'],item['lishi'],item['hot'])
            conn.execute(sql,params)
    #异常处理
    """def _handle_error(self, failue, item, spider):
    	log.err(failure)"""