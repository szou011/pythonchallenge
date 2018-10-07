#! /usr/bin/python3

"""
level_06.py
"""

import requests
import zipfile
import re

try:
    open('channel.zip', 'r')
    pass
except FileNotFoundError:
    zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    r = requests.get(zip_url)

    with open('channel.zip', 'wb') as f:
        f.write(r.content)

z = zipfile.ZipFile('channel.zip')

z_list = [x.filename for x in z.infolist()]

# construt a dict to inclde txt file name and the next number

pair_dict = {}
re_ptn = re.compile(r'\d+')

for txtfile in z_list:
    with z.open(txtfile, 'r') as txt:
        try:
            pair_dict[txtfile] = re_ptn.search(txt.read().decode('utf-8')).group()
        except:
            pass

# start with 90052

start = '90052'
while True:
    print(pair_dict[start + '.txt'])
    start = str(pair_dict[start + '.txt'])

