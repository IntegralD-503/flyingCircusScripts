#!/usr/bin/env python3
import re
import urllib.request

print("Where should we search?")
url=input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase: ")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

count = len(re.findall(searchFor, searchMe))
print(count)

