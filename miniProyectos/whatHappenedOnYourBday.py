#!/usr/bin/env python3
import json
import subprocess
import random 

def getUserInfo():
    print("Want to know an interesting event that happened on your birthday...?")
    date = input("Enter your birthday below (mm/dd format):\n")
    year = input("Now enter the year of your birth:\n")
    choice = input("Enter\n(1) for an event on the exact day of your birth\n"
            "(2) for an event on your birthday with a random year\n"
            "(3) for earliest searchable event on your birthday\n")
    
    return (date,year,int(choice))

def printEvent(event):
    year = event["year"]
    text = event["text"]
    print(f"On this day of year {year}")
    print(text)

def getRandomYearEvent(events):
    randomIndice = random.randint(0,len(events)-1)
    printEvent(events[randomIndice])

def getExactYearEvent(events,year):
    foundEvent = False
    for event in events:
        if event["year"] == year:
            printEvent(event)
            foundEvent = True
            break
    if not foundEvent:
        print("Sorry but we didn't find an event for that particular day.")


def getEarliestEvent(events):
    printEvent(events[0])

def getEvents(date):
    # open a new child process to use curl on the history api
    proc = subprocess.Popen(["curl", "-s", "http://history.muffinlabs.com/date/"+date], stdout=subprocess.PIPE)
    # send output to out
    (out, err) = proc.communicate()
    return json.loads(out)["data"]["Events"]


def main():
    date, year, choice = getUserInfo()
    events = getEvents(date)

    if choice == 1:
        getExactYearEvent(events,year)
    elif choice == 2:
        getRandomYearEvent(events)
    elif choice == 3:
        getEarliestEvent(events)

main()
