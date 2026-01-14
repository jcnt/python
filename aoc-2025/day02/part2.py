"""
Advent of Code, 2025. Day 2, part 2.

"""

with open("input", "r") as file:
    f = file.read().split(",")

counter = []
sum = 0

for ranges in f:
    cr = ranges.split("-")
    olist = list(range(int(cr[0]), int(cr[1]) + 1))

    #    print(olist)
    maxlen = len(cr[1])

    for code in olist:
        scode = str(code)
        lcode = len(scode)
        for i in range(2, lcode + 1):
            #            print(code, i)
            if lcode % i == 0:
                tl = []
                #                print(code, lcode, i, "yes")
                for j in range(0, lcode, (int(lcode / i))):
                    tl.append(scode[j : j + int(lcode / i)])
                #        print(tl)
                for k in range(0, len(tl)):
                    # counts how many times the 0. element in the list if it's the same
                    # as the length of the list => all elements are the same
                    res = tl.count(tl[0]) == len(tl)
                    #        print(tl, res)
                    if res == True:
                        counter.append("".join(tl))

# print(set(counter))

for s in set(counter):
    sum += int(s)

print(sum)
