#!/usr/bin/env python3
import requests
import json
import os

API_KEY = '&apiKey='+os.environ.get('API_KEY')
URL = 'https://newsapi.org/v2/'

def startMenu():
    print("Today's News, Hot Off The Digital Press")
    print("Pick a selection from below")
    print("(1) Top Headlines\n(2) BBC News\n(3) Reuters\n(4) Wired")
# in fish shell to set env variable for session -> set -x API_KEY 12312....1231
def getUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    data = r.json()
    return data

def formatUrl(url, apiKey, query):
    result = ""
    if query == 'top-headlines':
        result = query + '?country=us'
    else:
        result = 'top-headlines?sources='+query
    return url+result+apiKey

def printNews(data):
    print(data['totalResults'])
    showMore = True
    idx = 0
    while showMore:
        for article in data['articles']:
            if idx % 5 == 0 and idx != 0:
                userInput = input("\nPress Enter to see more articles, or q to exit: ")
                if userInput == 'q':
                    showMore = False
                    break
            print(f"\nSource: {article['source']['name']}\nAuthor: {article['author']}\nTitle: {article['title']}\n{article['description']}")
            idx += 1
    print("\nWe hoped you liked news!")

def main():
    global URL, API_KEY
    startMenu()
    choice = input()
    choices = {'1':'top-headlines','2':'bbc-news','3':'reuters','4':'wired'}
    
    if (arg := choices.get(choice)) is not None:
        data = getUrl(formatUrl(URL,API_KEY,arg))
        printNews(data)

main()
