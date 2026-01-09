"""
Advent of Code, 2025. Day 1, part 2.

"""

with open("input", "r") as file:
    f = file.read().splitlines()

dial = 50
count = 0

for i in f:
    if i[0] == "L":
        if dial == 0:
            count -= 1
        mround = int(i[1:]) // 100
        if mround > 0:
            print("___MROUND___", mround)
            count += mround
        dial = dial - int(i[1:]) % 100
        if dial == 0:
            count += 1
        if dial < 0:
            dial += 100
            count += 1
        print("L", i[1:], dial, count)
    elif i[0] == "R":
        mround = int(i[1:]) // 100
        if mround > 0:
            count += mround
            print("___MROUND___", mround)
        dial += int(i[1:]) % 100
        if dial >= 100:
            dial = dial - 100
            count += 1
        print("R", i[1:], dial, count)

print(count)
