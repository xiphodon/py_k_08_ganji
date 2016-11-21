#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/18 17:14
# @Author  : GuoChang
# @Site    : 
# @File    : get_link_from_category.py
# @Software: PyCharm

# 获取某个分类中的所有item链接
from bs4 import BeautifulSoup
import requests
import random
import pymongo
import get_category
import time

client = pymongo.MongoClient('localhost', 27017)
ganjiDB = client['ganjiDB']
url_list = ganjiDB['url_list']
item_info = ganjiDB['item_info']
test_url_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Connection': 'keep-alive'
}

proxy_list = [
    # 'http://202.171.253.72:80',
    # 'http://118.180.15.151:8102',
    # 'http://122.72.32.73:80',
    # 'http://218.106.205.145:8080'
    # 'http://101.53.101.172:9999',
    # 'http://115.28.2.233:8088',
    # 'http://124.88.67.17:82',
    # 'http://183.131.76.27:8888',
    # 'http://119.254.84.90:80',
    # 'http://122.225.253.125:808',
    'http://124.88.67.63:80'
    # 'http://202.171.253.72:80'
]


def get_random_proxy_ip():
    proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
    proxy = {'http': proxy_ip}
    # proxies = {'http': 'http://122.72.33.138:80'}
    return proxy


def get_all_link_from_one_category(url, pages=50):
    url_pages = ["{}{}{}/".format(url, "o", str(pages))]

    for each_url in url_pages:
        try:
            web_data = requests.get(each_url, headers=headers, proxies=get_random_proxy_ip())
            # web_data = requests.get(each_url, headers=headers)
            soup = BeautifulSoup(web_data.text, "lxml")
            # print(soup)
            if soup.find("div", "noinfo"):
                pass
            else:
                link_list = soup.select("tr.zzinfo > td.t > a.t")
                print(link_list)
                for each in link_list:
                    link = each.get("href").split("?")[0]
                    url_list.insert_one({"url": link})
                    test_url_list.append(link)
        except:
            pass


def get_item_info_from_url(url):
    web_data = requests.get(url, headers=headers, proxies=get_random_proxy_ip())
    soup = BeautifulSoup(web_data.text, "lxml")
    # print(soup)
    if not soup.find("span", ".soldout_btn"):
        title = soup.select(".info_titile")[0]
        price = soup.select(".price_now > i")[0]
        addr = soup.select(".palce_li > span > i")[0]
        item_detail = list(map(lambda x: x.text, soup.select("span.qlabel > span")))
        ower_name = soup.select(".personal_name")[0]
        look_time = soup.select(".look_time")[0]
        want_person = soup.select(".want_person")[0]
        print(title, price, addr, item_detail, ower_name, look_time, want_person)
        data = {
            "title": title.text.strip(),
            "price": price.text.strip(),
            "addr": addr.text,
            "item_detail": item_detail,
            "ower_name": ower_name.text,
            "look_time": look_time.text,
            "want_person": want_person.text,
            "url": url
        }
        # print(data)
        item_info.insert_one(data)
    else:
        pass


# for each in get_category.category_list_respones.split():
#     try:
#         # 获取当前类型下指定页面以内的所有链接
#         get_all_link_from_one_category(each, pages=50)
#     except:
#         pass

# print(test_url_list)
# for each in test_url_list:
#     try:
#         get_item_info_from_url(each)
#     except:
#         pass
# if len(test_url_list) > 0:
#     get_item_info_from_url(test_url_list[0])
