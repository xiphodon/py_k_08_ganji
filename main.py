#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/18 21:23
# @Author  : GuoChang
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from get_link_from_category import *
from multiprocessing import Pool
from get_category import *

# 主函数

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

# def get_all_links_from(channel):
#     for i in range(1,100):
#         get_links_from(channel,i)

def step_1():
    get_all_category()
    # pool = Pool(processes=6)
    pool = Pool()
    # pool.map(get_all_link_from_one_category,category_list_respones.split())
    pool.map(get_all_link_from_one_category, category_list)
    pool.close()
    pool.join()

def step_2():
    for each_url in [item['url'] for item in url_list.find()]:
        get_item_info_from_url(each_url)

if __name__ == '__main__':
    step_2()