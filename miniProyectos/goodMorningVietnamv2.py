#!/usr/bin/env python3
import requests
import json
import os

API_KEY = 'apiKey='+os.environ.get('API_KEY')
URL = 'http://newsapi.org/v2/'

def startMenu():
    print("Today's News, Hot Off The Digital Press")
    print("Pick a selection from below")
    print("(1) Top Headlines\n(2) BBC News\n(3) Reuters\n(4) Wired")
# in fish shell to set env variable for session -> set -x API_KEY 12312....1231
def getUrl(url, param, api_key):
    try:
        r = requests.get(url+param+api_key)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    data = r.json()
    return data

def main():
    global URL, API_KEY
    startMenu()
    choice = input()
    choices = {'1':'top-headlines?','2':'source=bbc-news?','3':'source=reuters?','4':'source=wired?'}
    
    if (arg := choices.get(choice)) is not None:
        print(arg)
        data = getUrl(URL,arg,API_KEY)
        for i in range(5):
            a = data['articles'][i]
            print(f"\nStory #{i}\nAuthor: {a['author']}\nTitle: {a['title']}\n{a['description']}")

main()
"""
    data = requests.get(url).json()
    print(f"Total Results: {data['totalResults']}")

    for i in range(5):
        a = data['articles'][i]
        print(f"\nStory #{i}\nAuthor: {a['author']}\nTitle: {a['title']}\n{a['description']}")
        """
