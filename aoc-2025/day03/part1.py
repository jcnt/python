"""
Advent of Code, 2025. Day 3, part 1.

"""

with open("input", "r") as file:
    f = file.read().split("\n")

f.remove("")
result = 0

for i in f:
    clist = list(i)
    #    print(clist)
    first = max(clist[0:-1])
    #    print(first)
    ifirst = clist.index(first)
    second = max(clist[ifirst + 1 :])
    #    print(second)
    result += int(first) * 10 + int(second)

print(result)
