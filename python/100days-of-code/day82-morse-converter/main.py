# assignment porgram for python scripting
# Day 82: get a string from input and translate it to morse signs.

import csv
import os

with open("morse.csv", newline="", mode="r", encoding="UTF8") as file:
    data = csv.reader(file)
    #     morse = list(data)    # this would do a list of lists
    abcmorse = {rows[0]: rows[1] for rows in data}


def mreturn(c):
    morse = ""
    for i in range(len(c)):
        if c[i].upper() not in abcmorse:
            return f'Invalid character, "{c[i]}" does not have a Morse code...'
        morse += abcmorse[f"{c[i].upper()}"]
        morse += "   "
    return morse


running = True

while running:
    os.system("clear")
    uval = input("Please enter a string to get its Morse code: ")
    print("\nMorse code: ")
    print(mreturn(uval))
    again = input("\nNext string or Quit? N/Q: ")

    if again.upper() == "Q":
        running = False
        print("\nBye!\n")
