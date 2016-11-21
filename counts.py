#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/18 21:21
# @Author  : GuoChang
# @Site    : 
# @File    : counts.py
# @Software: PyCharm

# 爬取数据计数器

from get_link_from_category import *
import time
while True:
    print("url_list:" + str(url_list.find().count()))
    print("item_info:" + str(item_info.find().count()))
    time.sleep(5)