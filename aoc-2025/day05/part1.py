"""
Advent of Code, 2025. Day 5, part 1.

"""

with open("input", "r") as file:
    f = file.read().split("\n")

f.remove("")
fresh = []
ingredient = []
counter = []

for i in f:
    if "-" in i:
        ranges = i.split("-")
        iranges = [int(ranges[0]), int(ranges[1])]
        fresh.append(iranges)

    else:
        if i != "":
            ingredient.append(int(i))

for item in ingredient:
    for fritem in fresh:
        if item >= fritem[0]:
            if item <= fritem[1]:
                counter.append(item)

print(counter, "counter")
print("final", len(set(counter)))
