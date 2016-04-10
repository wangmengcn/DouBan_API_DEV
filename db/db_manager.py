#-*- coding: UTF-8 -*-
from pymongo import MongoClient


class Douban_db:

    def __init__(self, host=None, port=None):
        if host is None:
            self.host = "localhost"
        else:
            self.host = host
        if port is None:
            self.port = 27017
        else:
            self.port = port

    def insert_info(self, dbname, colname, jsons):
        client = MongoClient(host=self.host, port=self.port)
        db = client[(dbname)]
        col = db[str(colname)]
        colum = 1
        for item in jsons:
            col.insert_one(item)
            colum += 1
        print "完成%d条数据插入" % colum
