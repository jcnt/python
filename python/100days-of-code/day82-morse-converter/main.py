# assignment porgram for python scripting
# get a string from input and translate it to morse signs.

import csv
import os

with open("morse.csv", newline="") as file:
    data = csv.reader(file)
    morse = list(data)


def mreturn(c):
    for i in range(36):
        if c == morse[i][0]:
            return morse[i][1]


g = mreturn("C")
print(g)
