"""
Advent of Code, 2025. Day 6, part 1.

"""

mline = []
tline = []
counter = 1

with open("example", "r") as file:
    source = file.read().split("\n")

source.remove("")

for i in source:
    print(i)
print("---------------")

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
