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


def run():
    c = open('fake1.csv', 'ab')
    w = csv.writer(c)

    csvFile = open('names.csv', 'rb')
    r = csv.reader(csvFile)
    names = [row for row in r]

    csvFile = open('address2.csv', 'rb')
    r = csv.reader(csvFile)
    address = [row for row in r]

    csvFile = open('phones.csv', 'rb')
    r = csv.reader(csvFile)
    phones = [row for row in r]

    len_names = len(names)
    len_address = len(address)
    len_phones = len(phones)
    w.writerow(('name', 'phone', 'add'))
    for i in range(1000000):
        name = names[random.randint(0, len_names-1)][0]
        phone = phones[random.randint(0, len_phones-1)][0]
        add = address[random.randint(0, len_address-1)][0]

        print name
        print phone
        print add
        w.writerow((name, phone, add))
        c.flush()

if __name__ == '__main__':
    run()