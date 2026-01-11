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
        for i in range(1, int(maxlen / 2) + 1):
            print(i)

            #            lcode = len(str(code))
            #            print("lcode", lcode)
            #            if lcode % i == 0:
            #                tl = []
            #                for j in range(0, lcode, int(lcode / i)):
            #                    tl.append(str(code)[j : j + int(lcode / i)])
            #                    print("tl", tl)
            #                print(tl)
            #                isEqual = True
            #                for k in range(1, len(tl)):
            #                    if tl[0] != tl[k]:
            #                        isEqual = False
            #                print(isEqual)
            #                if isEqual == True:
            #                    counter += code
            #
print(counter)
