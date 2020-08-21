#!/usr/bin/env python3
import requests
import json
import wget

api_key = ""

def loadApiKey():
    global api_key
    try:
        with open("/../../nasa_api_key",'r') as keyFile:
            api_key = keyFile.readline().rstrip()
    except IOError as e:
        raise Exception("Could not read file") from e

def getUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    data = r.json()
    return data

def getSpacePic(url,title):
    wget.download(url, out=f"./{title.replace(' ', '_')}.gif")

def main():
    global api_key
    loadApiKey()
    #print("This program provides a text description and link to a gorgeous picture from the Hubble telescope!")
    date = "2013-03-13"#input("Enter a date in format of YYYY-MM-DD (FYI, the APOD API doesn't go earlier than Jun 16, 1995)\n")
    url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}"

    data = getUrl(url)
    date = data['date']
    title = data['title']
    descr = data['explanation']
    url = data['url']

    print(f"\n{date}\n----------\n\n{title}\n\n{descr}\n\n")

    print("Fetching image...")
    getSpacePic(url,title)

if __name__ == "__main__":
    main()
