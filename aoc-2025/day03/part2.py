"""
Advent of Code, 2025. Day 3, part 2.

"""

with open("input", "r") as file:
    f = file.read().split("\n")

f.remove("")
result = 0

result = 0

for i in f:
    c_index = 0
    sub_result = 0
    for togo in range(11, -1, -1):
        c_list = list(i)
        if togo == 0:
            sublist = c_list[c_index:]
        else:
            sublist = c_list[c_index:-togo]
        c_max = max(sublist)
        c_index = sublist.index(c_max) + c_index + 1
        sub_result += int(c_max) * (10**togo)
    result += sub_result

print(result)
