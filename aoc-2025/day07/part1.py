"""
Advent of Code, 2025. Day 7, part 1.

"""

with open("input", "r") as file:
    source = file.read().split("\n")

source.remove("")
manifold = []
counter = 0

for line in source:
    manifold.append(list(line))

beamlist = []
beamlist.append(manifold[0].index("S"))
print(beamlist)

print()
for i in manifold:
    print(i)

for i in range(1, len(manifold)):
    for j in range(len(manifold[i])):
        if j in beamlist and manifold[i][j] == "^":
            print("MATCH", i, j)
            beamlist.remove(j)
            if j - 1 not in beamlist:
                beamlist.append(j - 1)
            if j + 1 not in beamlist:
                beamlist.append(j + 1)
            counter += 1

print(beamlist)
print("final answer:", counter)
