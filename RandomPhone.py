# -*- coding: utf-8 -*-
import json
import re
import os
from lxml import html
import csv
import datetime
import mysql.connector
from multiprocessing import Process
import random
import requests


def run():
    # 中国移动 17
    header_cm = ['139', '138', '137', '136', '135', '134', '147', '150', '151', '152', '157', '158', '159', '182', '183', '187', '184']
    # 中国联通 8
    header_cu = ['130', '131', '132', '155', '156', '185', '186', '145']
    # 中国电信 5
    header_ctc = ['133', '153', '181', '180', '189']

    c = open('phones.csv', 'ab')
    w = csv.writer(c)
    for i in range(1500000):
        rand = str(random.randint(0, 99999999))

        for i in range(8-len(rand)):
            rand = '0' + rand

        header = header_cm[random.randint(0, 16)]
        # header = header_cu[random.randint(0, 7)]
        # header = header_ctc[random.randint(0, 4)]
        phone = header + rand

        w.writerow((phone,))

        print phone
        # print datetime.datetime.now()



if __name__ == '__main__':
    run()