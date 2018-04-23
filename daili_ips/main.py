# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 22:28
# @Author  : sharply
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Email   :18391122555@139.com
from scrapy import cmdline


def main():
    cmdline.execute(['scrapy36','crawl','xici'])



if __name__=="__main__":
    main()