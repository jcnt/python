"""
Advent of Code, 2025. Day 2, part 1.

"""

with open("example", "r") as file:
    f = file.read().split(",")

counter = 0

for ranges in f:
    cr = ranges.split("-")
    l = list(range(int(cr[0]), int(cr[1]) + 1))

    maxlen = len(cr[1])

    print(l, maxlen)

    for code in l:
        for i in range(2, int(maxlen / 2) + 2):
            lcode = len(str(code))
            if lcode % i == 0:
                tl = []
                print(code, lcode, i, "yes")
                for j in range(0, lcode, (int(lcode / i) + 1)):
                    print(j)
print(counter)
