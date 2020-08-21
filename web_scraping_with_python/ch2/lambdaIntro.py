#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'html.parser')

tags1 = bsObj.find_all(lambda tag: len(tag.attrs) == 2)
tags2 = bsObj.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
tags3 = bsObj.find_all('',text='Or maybe he\'s only resting?')
#print(tags1)
#print(tags2)
print(tags3)
    
