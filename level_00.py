"""
level_00.py
www.pythonchallenge.com/pc/def/0.html
"""

url = r'www.pythonchallenge.com/pc/def/0.html'

new_url = url.replace('0', str(2 ** 38))

print(new_url)

