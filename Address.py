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

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

def address():
    file = open("dist/pca-code.json", 'rb')
    # line = file.readline()
    # datas = eval(line.decode('utf-8'))
    # print datas
    # c = open('address1.csv', 'ab')
    # w = csv.writer(c)
    while 1:
        line = file.readline()
        if not line:
            break
        datas = eval(line.decode('utf-8'))
        # datas = json.loads(line.decode('utf-8'), object_hook=JSONObject)

        # for name in datas['name']:
        #     print name
        for i in range(len(datas)):
            one = datas[i]['name']

            # print type(datas[i]['childs'])
            # childs = eval(datas[i]['childs'])

            for child in datas[i]['childs']:
                # child = eval(child)
                # print child['code']

                two = child['name']
                for miao in child['childs']:
                    # print miao['code']
                    # print miao['name']
                    three = miao['name']

                address = one + two
                    # address = one + two + three
                print address
                    # w.writerow((address, miao['code']))


def street():
    file = open("dist/streets.json", 'rb')

    c = open('address2.csv', 'ab')
    w = csv.writer(c)

    streets = []
    while 1:
        line = file.readline()
        if not line:
            break
        datas = eval(line.decode('utf-8'))

        for i in range(len(datas)):
            street = datas[i]['name']
            parent = datas[i]['parent_code']

            print street
            print parent

            streets.append([street, parent])

    csvFile = open('address1.csv', 'rb')
    r = csv.reader(csvFile)
    address = [row for row in r]

    for street in streets:
        parent = street[1]

        for add in address:
            if add[1] == parent:
                print add[0] + street[0]
                miao = add[0] + street[0]
                w.writerow((miao,))
                c.flush()


    c.close()



if __name__ == '__main__':
    address()
    # street()