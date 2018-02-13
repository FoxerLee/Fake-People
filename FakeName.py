# -*- coding: utf-8 -*-
from lxml import html
import csv
import datetime
import requests


def run():

    c = open('names.csv', 'ab')
    w = csv.writer(c)
    for i in range(4000):
        res = requests.get('http://www.gaoshukai.com/lab/0014/cn.php')
        # res.encoding = 'gb2312'

        tree = html.fromstring(res.text)
        trs = tree.xpath('//*[@id="main"]/ul/li')

        for tr in trs:
            name = tr.xpath('./text()')[0].encode('utf8')
            name = name[3:-3]
            w.writerow((name, ))
            print name

        print datetime.datetime.now()


if __name__ == '__main__':
    run()