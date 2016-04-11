#-*- coding: UTF-8 -*-
# 通过豆瓣标签来获取详细信息

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
import requests
import json
import time
from tag_collection import get_tags
import os
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir+'/ruler')
sys.path.append(basedir+'/db')
from db_manager import Douban_db
import spider_rule

category = ''
db = Douban_db()


def get_info(category):
    # 获取对应的请求规则
    ruler = spider_rule.get_rule(category)
    for ru in ruler:
        print ru
    info = range(1, 7)
    col = 1
    interval = ruler[0]
    count = ruler[1]
    info_tag = ruler[2]

    # 获取要进行请求的URL
    tagurl = get_url(category)

    tags = get_tags(category)

    for tag in tags:
        if col not in info:
            jsoninfo = get_data(tagurl, tag, count, interval, info_tag)
            db.insert_info(category, col, jsoninfo)
        col += 1


def get_url(category):
    url = ''

    if category == "movie":
        url = 'https://api.douban.com/v2/movie/search?'
    elif category == "book":
        url = 'https://api.douban.com/v2/movie/search?'
    elif category == "music":
        url = 'https://api.douban.com/v2/music/search?'
    else:
        print "还未添加此类别"

    return url


def get_data(url, tag, count, sleep, subject):
    flag = True
    start = 0
    infos = []
    while flag:
        # print start
        infourl = url+"tag="+tag+"&start="+str(start)+"&count="+str(count)
        print infourl
        httpinfo = requests.get(infourl)
        jsoninfo = json.loads(httpinfo.text, encoding="utf-8")
        if jsoninfo[subject] != []:
            for item in jsoninfo[subject]:
                infos.append(item)
        else:
            flag = False
        start += count
        time.sleep(sleep)
    return infos


