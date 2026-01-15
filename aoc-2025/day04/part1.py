"""
Advent of Code, 2025. Day 3, part 2.

"""

with open("example", "r") as file:
    f = file.read().split("\n")

print(f)

for row in range(len(f)):
    for item in range(len(f[row])):
        print(row, item)
        print(f[row][item])
        for i in range(row - 1, row + 2):
            for j in range(item - 1, item + 2):
                if i >= 0 and i < len(f[row]) and j >= 0 and j < len(f):
                    print(f[row][item], i, j, f[i][j], "\n")
