"""
Advent of Code, 2025. Day 2, part 1.

"""

with open("example", "r") as file:
    f = file.read().split(",")


for ranges in f:
    curr = ranges.split("-")
    l = [item for item in range(int(curr[0]), int(curr[1]) + 1)]
    print(l)
