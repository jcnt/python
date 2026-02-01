"""
Advent of Code, 2025. Day 7, part 2.

"""

with open("input", "r") as file:
    source = file.read().split("\n")

source.remove("")
manifold = []
pathcount = []

for line in source:
    manifold.append(list(line))

pathcount = [0 for i in range(len(manifold[0]))]
pathcount[manifold[0].index("S")] = 1
print(pathcount)

print()
for i in manifold:
    print(i)

for i in range(1, len(manifold)):
    for j in range(len(manifold[i])):
        if manifold[i][j] == "^":
            print("MATCH", i, j)
            pathcount[j + 1] += pathcount[j]
            pathcount[j - 1] += pathcount[j]
            pathcount[j] = 0
            print(pathcount)
            print(manifold[i])

print("final answer: ", sum(pathcount))
