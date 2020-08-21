#!/usr/bin/env python3
import requests
import json

def getUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    data = r.json()
    return data

def main():
    url = f"http://api.open-notify.org/astros.json"
    data = getUrl(url)
    
    print(f"People in space: {data['number']}")
    for person in data['people']:
        print(f"{person['name']} on the {person['craft']}")

if __name__ == "__main__":
    main()
