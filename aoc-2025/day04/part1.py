"""
Advent of Code, 2025. Day 4, part 1.

"""

with open("input", "r") as file:
    f = file.read().split("\n")

f.remove("")
print(f)

result = 0


for row in range(len(f)):
    for item in range(len(f[row])):
        print(row, item)
        print(f[row][item])
        if f[row][item] == "@":
            counter = 0
            for i in range(row - 1, row + 2):
                for j in range(item - 1, item + 2):
                    if i >= 0 and i < len(f[row]) and j >= 0 and j < len(f):
                        if i == row and j == item:
                            print("this is me")
                        else:
                            print(i, j, f[i][j], row, item)
                            if f[i][j] == "@":
                                counter += 1
            print("counter", counter, "\n")
            if counter < 4:
                result += 1

print("final result = ", result)
