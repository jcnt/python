"""
Advent of Code, 2025. Day 2, part 1.

"""

with open("example", "r") as file:
    f = file.read().split(",")

counter = []

for ranges in f:
    cr = ranges.split("-")
    l = list(range(int(cr[0]), int(cr[1]) + 1))

    maxlen = len(cr[1])

    print(l, maxlen)

    for code in l:
        scode = str(code)
        for i in range(2, int(maxlen / 2) + 2):
            lcode = len(scode)
            if lcode % i == 0:
                tl = []
                print(code, lcode, i, "yes")
                for j in range(0, lcode, (int(lcode / i))):
                    tl.append(scode[j : j + int(lcode / i)])
                print(tl)
                for k in range(len(tl)):
                    if tl[0] == tl[k]:
                        print("yes")

print(counter)
