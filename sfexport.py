# -*- coding: utf-8 -*-
import sqlite3
import re
import time
import random
import sys
import datetime
import os

conn = sqlite3.connect(r"sf.green.orm.db")
c = conn.cursor()
d = conn.cursor()
e = conn.cursor()
c.execute("SELECT * FROM `CHAPTER`")

for row in c:
    print(row)
    if not os.path.exists('./{}'.format(row[1])):
        os.makedirs('./{}'.format(row[1]))   
    d.execute('SELECT * FROM `VOLUME` WHERE `_id`={} LIMIT 1'.format(row[2]))
    for volume in d:
        if not os.path.exists('./{}/{}-{}'.format(row[1], row[2], volume[1])):
            os.makedirs('./{}/{}-{}'.format(row[1], row[2], volume[1]))  
    e.execute('SELECT * FROM `CHAPTER_CONTENT` WHERE `_id`={} LIMIT 1'.format(row[0])) 
    for chapter in e:
        print(chapter[2])
        path = './{}/{}-{}/{}-{}.txt'.format(row[1], row[2], volume[1], row[0], row[5])
        fo = open(path, "w", encoding='utf-8')
        print("Writing file " + path)
        fo.write(chapter[2])
        fo.close()
