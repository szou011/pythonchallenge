"""
level_07.py
"""

import requests
import re
from PIL import Image

jpg_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

try:
    open('oxygen.png', 'r')
except FileNotFoundError:
    with open('oxygen.png', 'wb') as f:
        f.write(requests.get(jpg_url).content)

next_str = ""

with Image.open('oxygen.png') as jpg:
    for i in range(0, jpg.width, 7):
        point = jpg.getpixel((i, 48))
        if point[0] == point [1] == point[2]:
            next_str = next_str + chr(point[0])

print(next_str)

match_next_string = map(int, re.findall('\d+', next_str))

print(list(map(chr, match_next_string)))
