"""
Advent of Code, 2025. Day 5, part 2.

"""

with open("example", "r") as file:
    f = file.read().split("\n")

print(f)

fresh = []
current = 0
counter = 0

for i in f:
    if "-" in i:
        start = i.split("-")[0]
        end = i.split("-")[1]
        l = [int(start), int(end)]
        fresh.append(l)

fresh.sort()
print("fresh items:", fresh)

for l in fresh:
    if l[0] >= current:
        print("counter", counter, "current", current, "start", l[0], "end", l[1])
        counter += l[1] - l[0] + 1
        current = l[1]
    elif l[1] >= current:
        print("counter", counter, "current", current, "start", l[0], "end", l[1])
        counter += l[1] - current
        current = l[1]
    else:
        print("counter", counter, "current", current, "start", l[0], "end", l[1])


print("final answer:", counter)
