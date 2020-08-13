#!/usr/bin/env python3
"""  Clarkopotamus  """

# imports always go at the top of your code
import requests
import json
import random

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object
    #print( r.json().get("all") )
    #print( dir(r) )
    catFacts = r.json().get("all")
    #Get first fact and name
    #print(f"{catFacts[0]['user']['name']['last']}, {catFacts[0]['user']['name']['first']}")
    #print(f"{catFacts[0]['text']}")
    # find catFact with highest amount of upvotes
    cat_idx = 0
    current_idx = 0
    max_upvotes = 0
    for catfact in catFacts:
        if catfact['upvotes'] > max_upvotes:
            max_upvotes = catfact['upvotes']
            cat_idx = current_idx
        current_idx += 1
    print(f"{catFacts[cat_idx]['text']}, Upvotes: {catFacts[cat_idx]['upvotes']}")

    #randoCatIdx = random.randint(0, len(catFacts)-1)
    #print(f"Rando Cat:\n{catFacts[randoCatIdx]['text']}")
    print(f"{random.choice(catFacts)['text']}")
main()

