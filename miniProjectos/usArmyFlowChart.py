#!/usr/bin/env python3
"""

   Hunter Clark - Army FlowChart Implementation

"""

# id : ["text", "answerYesOrDefaultID", "answerNoID", "asksForInputBoolean"]
flowChartData = {
    "0000" : ["Does the damn thing work? [y/n]\n", "0001", "0010", False],
    "0001" : ["Don't f*ck with it", None, None, True],
    "0010" : ["Did you f*ck with it? [y/n]\n", "0011","0111",False],
    "0011" : ["You dumb shit!", "0100", None, True],
    "0100" : ["Does anyone know? [y/n]\n", "0110", "0101", False],
    "0101" : ["Hide It", "1010","None",True],
    "0110" : ["You poor bastard!", "1000",None, True],
    "0111" : ["Will you catch hell? [y/n]\n", "0110","1001", False],
    "1000" : ["Can you blame a private? [y/n]\n", "1010", "0110", False],
    "1001" : ["Shit-can it!", "1010", None, True],
    "1010" : ["No Problemo!", None, None, True]
}



def main():
    id = "0000"
    yesOrDefault = 1
    no = 2
    inputCheck = 3
    finished = False
    
    while not finished:
        if id is None:
            break

        if not flowChartData[id][3]:
            choice = input(flowChartData[id][0])
            if choice != "y" and choice != "n" or flowChartData[id][inputCheck]:
                print("What is your malfunction soldier?! Enter the correct response next time!!")
                continue
            id = (flowChartData[id][no],
                    flowChartData[id][yesOrDefault]) [choice == "y"]
        else:
            print(flowChartData[id][0])
            id = flowChartData[id][yesOrDefault]

main()
