"""
level_03.py
"""

import re
import requests

res = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

ptn_html = re.compile(r'<!--.*', re.DOTALL)

html = ptn_html.search(res.text).group()

ptn_re = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')

print(ptn_re.findall(html))
