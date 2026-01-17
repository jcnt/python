"""
Advent of Code, 2025. Day 4, part 2.

"""

with open("input", "r") as file:
    f = file.read().split("\n")
    g = file.readlines()
f.remove("")

result = 0
pcan = []
for string in f:
    pcan.append(list(string))


def printcan():
    for i in pcan:
        print(i)


printcan()
didsomething = True

while didsomething:
    didsomething = False
    for row in range(len(pcan)):
        for item in range(len(pcan[row])):
            if pcan[row][item] == "@":
                print("yes", row, item)
                counter = 0
                for i in range(row - 1, row + 2):
                    for j in range(item - 1, item + 2):
                        if i >= 0 and i < len(pcan[row]) and j >= 0 and j < len(pcan):
                            if i == row and j == item:
                                print("this is me")
                            else:
                                print(i, j, pcan[i][j], row, item)
                                if pcan[i][j] == "@":
                                    counter += 1
                if counter < 4:
                    result += 1
                    pcan[row][item] = "x"
                    didsomething = True


printcan()
print(result)
