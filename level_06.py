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

# z_list = [x.filename for x in z.infolist()]

filename = '90052'
re_ptn = re.compile(r'\d+')
comments = list()

while True:
    with z.open(filename + '.txt', 'r') as txt:
        content = txt.read().decode('utf-8')
        print(content)
        comments.append(z.getinfo(filename + '.txt').comment.decode('utf-8'))

        match = re_ptn.search(content)
        if match == None:
            break
        filename = match.group()
for i in comments:
    print(i, end="")
