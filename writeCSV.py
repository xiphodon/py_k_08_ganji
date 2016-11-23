#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/23 16:07
# @Author  : GuoChang
# @Site    : 
# @File    : writeCSV.py
# @Software: PyCharm

import csv

class writerCSV:
    fields = ('title', 'addr', 'url', 'price', 'look_time', 'want_person', 'ower_name')
    def __init__(self,filename):
        self.writer = csv.writer(open(filename, 'w',encoding='utf-8'))
        self.writer.writerow(self.fields)

    def __call__(self, *args, **kwargs):
        self.writer.writerow(args[0],)