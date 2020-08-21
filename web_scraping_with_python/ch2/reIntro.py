#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'html.parser')

images = bsObj.find_all("img", {"src" : re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
    
