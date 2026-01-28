"""
Advent of Code, 2025. Day 6, part 1.

"""

problem = []
counter = 0

with open("input", "r") as file:
    for line in file.readlines():
        problem.append(line.strip().split(" "))

for i in range(len(problem)):
    problem[i] = [e for e in problem[i] if e != ""]

for col in range(len(problem[0])):
    sub = []
    subcount = 1
    for line in range(len(problem)):
        sub.append(problem[line][col])
    if sub[-1] == "+":
        for num in range(len(sub) - 1):
            subcount += int(sub[num])
        subcount -= 1
    elif sub[-1] == "*":
        for num in range(len(sub) - 1):
            subcount *= int(sub[num])
    print(subcount)
    counter += subcount


print("final is: ", counter)
