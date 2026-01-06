"""
Advent of Code, 2025. Day 1, part 1.

"""

with open("example", "r") as file:
    f = file.read().splitlines()

for i in f:
    if i[0] == "L":
        print("left")
    elif i[0] == "R":
        print("right")
