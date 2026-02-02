"""
Advent of Code, 2025. Day 8, part 1.

"""

source = []
dist_db = {}
conn_pairs = []

with open("example", "r") as file:
    for line in file:
        source.append(line.strip().split(","))


def get_distance(a, b):
    return (
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

print(dist_db)
sdict = sorted(dist_db.items(), key=lambda item: item[1])

for k in sdict:
    a = int(k[0].split(",")[0])
    b = int(k[0].split(",")[1])
