"""
Advent of Code, 2025. Day 1, part 1.

"""

with open("input", "r") as file:
    f = file.read().splitlines()

dial = 50
count = 0

for i in f:
    if i[0] == "L":
        dial = dial - int(i[1:]) % 100
        if dial == 0:
            count += 1
        if dial < 0:
            dial += 100
        print("L", i[1:], dial, count)
    elif i[0] == "R":
        dial += int(i[1:]) % 100
        if dial == 100:
            dial = 0
            count += 1
        if dial > 100:
            dial = dial % 100
            if dial == 0:
                count += 1
        print("R", i[1:], dial, count)

print(count)
