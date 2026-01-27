"""
Advent of Code, 2025. Day 5, part 2.

"""

with open("input", "r") as file:
    f = file.read().split("\n")

print(f)

fresh = []
clist = [0, 0]
counter = []
fcount = 0

for i in f:
    if "-" in i:
        start = i.split("-")[0]
        end = i.split("-")[1]
        l = [int(start), int(end)]
        fresh.append(l)

fresh.sort()
print("fresh items:", fresh)

for l in fresh:
    newlist = l
    print("new", newlist, "curr", clist)
    if newlist[0] >= clist[0] and newlist[0] <= clist[1]:
        if newlist[1] > clist[1]:
            clist[1] = newlist[1]
    if newlist[0] > clist[1]:
        counter.append(clist)
        print("append success")
        clist = newlist

counter.remove([0, 0])
counter.append(clist)

for c in counter:
    fcount += c[1] - c[0] + 1


print("final answer:", fcount)
