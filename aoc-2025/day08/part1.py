"""
Advent of Code, 2025. Day 8, part 1.

"""

import math

source = []
dist_db = {}
conn_pairs = [[0, 0]]
a_loc = 0
b_loc = 0
exists = False
ncirc = 0

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
    if ncirc < 10:
        a = int(k[0].split(",")[0])
        b = int(k[0].split(",")[1])
        print(f"{ncirc} is {a} and {b}")
        ncirc += 1
        for i in range(len(conn_pairs)):
            if a in conn_pairs[i] and b not in conn_pairs[i]:
                a_loc = i
            elif b in conn_pairs[i] and a not in conn_pairs[i]:
                b_loc = i
            elif a in conn_pairs[i] and b in conn_pairs[i]:
                exists = True
        if a_loc != 0:
            conn_pairs[a_loc].append(b)
            print("appended", b, "into", conn_pairs[a_loc], "from", a, b)
            a_loc = 0
        elif b_loc != 0:
            conn_pairs[b_loc].append(a)
            print("appended", a, "into", conn_pairs[b_loc], "from", a, b)
            b_loc = 0
        else:
            if not exists:
                conn_pairs.append([a, b])
                print("new pair", a, b)
            else:
                exists = False

conn_pairs.remove([0, 0])
print(conn_pairs)
for i in conn_pairs:
    print(set(i))
