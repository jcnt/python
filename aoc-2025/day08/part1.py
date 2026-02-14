"""
Advent of Code, 2025. Day 8, part 1.

"""

import math

source = []
dist_db = {}
conn_pairs = [[0, 0]]
counter = []
a_loc = 0
b_loc = 0
exists = False
ncirc = 0

with open("input", "r") as file:
    for line in file:
        source.append(line.strip().split(","))


def get_distance(a, b):
    return math.sqrt(
        (int(a[0]) - int(b[0])) ** 2
        + (int(a[1]) - int(b[1])) ** 2
        + (int(a[2]) - int(b[2])) ** 2
    )


# for num in range(len(source)):
#    print(num, source[num])

for i in range(0, len(source)):
    for j in range(i + 1, len(source)):
        distance = get_distance(source[i], source[j])
        dist_db[f"{i},{j}"] = distance

sdict = sorted(dist_db.items(), key=lambda item: item[1])
# print(sdict)

for k in sdict:
    a = int(k[0].split(",")[0])
    b = int(k[0].split(",")[1])
    print(f"{ncirc} is {a} and {b}")
    ncirc += 1
    for i in range(len(conn_pairs)):
        for j in conn_pairs[i]:
            if a == j:
                a_loc = i
            elif b == j:
                b_loc = i
    if a_loc != 0 and b_loc == 0:
        conn_pairs[a_loc].append(b)
        counter.append(b)
        print("appended", b, "into", conn_pairs[a_loc], "from", a, b)
        a_loc = 0
        exists = True
    elif b_loc != 0 and a_loc == 0:
        conn_pairs[b_loc].append(a)
        counter.append(a)
        print("appended", a, "into", conn_pairs[b_loc], "from", a, b)
        b_loc = 0
        exists = True
    elif b_loc != 0 and a_loc != 0:
        exists = True
        print(f"it exists and a in {a_loc} b in {b_loc}")
        if a_loc != b_loc:
            for subitem in conn_pairs[a_loc]:
                print(f"subitem is {subitem}")
                conn_pairs[b_loc].append(subitem)
                print(f"appended list is now {conn_pairs[b_loc]}")
            conn_pairs.pop(a_loc)
            print(f"appended the items of {a_loc} to {b_loc}")
        a_loc = 0
        b_loc = 0
    if not exists:
        conn_pairs.append([a, b])
        counter.append(a)
        counter.append(b)
        print("new pair", a, b)
    else:
        exists = False
    if ncirc == 1000:
        break

conn_pairs.remove([0, 0])
conn_pairs.sort(key=len, reverse=True)
print(conn_pairs)
print(len(conn_pairs[0]) * len(conn_pairs[1]) * len(conn_pairs[2]))
