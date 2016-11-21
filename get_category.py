#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/18 16:36
# @Author  : GuoChang
# @Site    : 
# @File    : get_category.py
# @Software: PyCharm

# 获取赶集网上海二手市场各个分类

from bs4 import BeautifulSoup
import requests

url = "http://sh.ganji.com"
second_hand_url = url + "/wu/"

category_list = []

def get_all_category():
    web_data = requests.get(second_hand_url)
    soup = BeautifulSoup(web_data.text, "lxml")
    # print(soup)
    category_url_list = soup.select("div.main li dt > a")
    for category_url in category_url_list:
        category_list.append(url + category_url.get("href"))

if __name__ == "__main__":
    get_all_category()
    for each in category_list:
        print(each)

category_list_respones = """
http://sh.ganji.com/shouji/
http://sh.ganji.com/shoujihaoma/
http://sh.ganji.com/shoujipeijian/
http://sh.ganji.com/bijibendiannao/
http://sh.ganji.com/taishidiannaozhengji/
http://sh.ganji.com/diannaoyingjian/
http://sh.ganji.com/wangluoshebei/
http://sh.ganji.com/shumaxiangji/
http://sh.ganji.com/youxiji/
http://sh.ganji.com/xuniwupin/
http://sh.ganji.com/jiaju/
http://sh.ganji.com/jiadian/
http://sh.ganji.com/zixingchemaimai/
http://sh.ganji.com/rirongbaihuo/
http://sh.ganji.com/yingyouyunfu/
http://sh.ganji.com/fushixiaobaxuemao/
http://sh.ganji.com/meironghuazhuang/
http://sh.ganji.com/yundongqicai/
http://sh.ganji.com/yueqi/
http://sh.ganji.com/tushu/
http://sh.ganji.com/bangongjiaju/
http://sh.ganji.com/wujingongju/
http://sh.ganji.com/nongyongpin/
http://sh.ganji.com/xianzhilipin/
http://sh.ganji.com/shoucangpin/
http://sh.ganji.com/baojianpin/
http://sh.ganji.com/laonianyongpin/
http://sh.ganji.com/gou/
http://sh.ganji.com/qitaxiaochong/
http://sh.ganji.com/xiaofeika/
http://sh.ganji.com/menpiao/
"""