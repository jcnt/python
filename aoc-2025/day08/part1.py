"""
Advent of Code, 2025. Day 8, part 1.

"""

import math

source = []
dist_db = {}
conn_pairs = [[0, 0]]

with open("example", "r") as file:
    for line in file:
        source.append(line.strip().split(","))


def get_distance(a, b):
    return math.sqrt(
        (int(a[0]) - int(b[0])) ** 2
        + (int(a[1]) - int(b[1])) ** 2
        + (int(a[2]) - int(b[2])) ** 2
    )


for num in source:
    print(num)

for i in range(0, len(source)):
    for j in range(i + 1, len(source)):
        distance = get_distance(source[i], source[j])
        dist_db[f"{i},{j}"] = distance

sdict = sorted(dist_db.items(), key=lambda item: item[1])
print(sdict)

for k in sdict:
    a = int(k[0].split(",")[0])
    b = int(k[0].split(",")[1])
    print(a, b)
    for i in range(len(conn_pairs)):
        if a in conn_pairs[i]:
            conn_pairs[i].append(b)
        if b in conn_pairs[i]:
            conn_pairs[i].append(a)
        else:
            conn_pairs.append([a, b])
    print(conn_pairs)
