""""
level_04.py
"""

import re
import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
urldict = {'nothing':12345}
loop_setter = True
pattern_nothing = re.compile(r'\d+')
nothing = ''

while loop_setter:
    if requests.get(url, params=urldict).ok:
        content = requests.get(url, params=urldict).text
        print(content)
        if pattern_nothing.search(content):
            nothing = pattern_nothing.search(content).group()
        else:
            nothing = input('input your number: ')
            if nothing == "":
                loop_setter = False
        urldict['nothing'] = nothing
    else:
        loop_setter = False
