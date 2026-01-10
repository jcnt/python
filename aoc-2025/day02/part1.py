"""
Advent of Code, 2025. Day 2, part 1.

"""

with open("input", "r") as file:
    f = file.read().split(",")

counter = 0

for ranges in f:
    cr = ranges.split("-")
    l = list(range(int(cr[0]), int(cr[1]) + 1))
    for code in l:
        scode = str(code)
        clen = len(str(code))
        if clen % 2 == 0:
            f = scode[0 : int(clen / 2)]
            s = scode[int(clen / 2) : clen]
            if f == s:
                counter += code

print(counter)
