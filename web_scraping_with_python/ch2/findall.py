#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
 
princeCount = bsObj.findAll(text="the prince")
print(len(princeCount))
