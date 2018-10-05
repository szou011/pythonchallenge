import requests
import pickle

f = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')

p = pickle.loads(f.content)

for line in p:
    for x, y in line:
        print(x * y, end="")
    print("")
