#!/usr/bin/env python3
import requests
import json
import wget

def api_pull():
    choice = input("What Pokemon would you like a picture of? ")
    pokemon = choice.strip().lower()
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    return url

def json_conv(poke_api):
    try:
        r = requests.get(poke_api)
        return r.json()
    except:
        return "sprites : { front_default : https://www.example.com } "


def api_slice(json2python):
    poke_pic = json2python['sprites']['front_default']
    return poke_pic

def wget_pic(image_link):
    out_file = "./pokemon.png"
    pic = wget.download(image_link, out=out_file)

def main():
    wget_pic(api_slice(json_conv(api_pull())))

main()
