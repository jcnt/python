"""
Advent of Code, 2025. Day 2, part 1.

"""

with open("example", "r") as file:
    f = file.read().split(",")


for ranges in f:
    cr = ranges.split("-")
    l = list(range(int(cr[0]), int(cr[1]) + 1))
    print(l)
