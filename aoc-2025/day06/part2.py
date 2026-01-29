"""
Advent of Code, 2025. Day 6, part 2.

"""

mline = []
tline = []
fline = []
pcount = 0
mcount = 1

with open("input", "r") as file:
    source = file.read().split("\n")

source.remove("")

for i in source:
    print(i)

for char in range(len(source[0]) - 1, -1, -1):
    num = ""
    op = ""
    for line in source:
        if line[char] == "*" or line[char] == "+":
            op = line[char]
        elif line[char] != " ":
            num += line[char]
    if num != "":
        mline.append(num)
    if op != "":
        mline.append(op)

print(mline)

for i in mline:
    if i != "+" and i != "*":
        tline.append(i)
    else:
        for j in tline:
            if i == "+":
                pcount += int(j)
            if i == "*":
                mcount *= int(j)
        if mcount != 1:
            fline.append(mcount)
            mcount = 1
        if pcount != 0:
            fline.append(pcount)
            pcount = 0
        tline = []

print("final solution", sum(fline))
