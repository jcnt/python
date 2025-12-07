d = {}

d["a"] = 1

c = d.get("a")
print(d)
print(c)

if type(d.get("b")) == int:
    d["b"] += 1
else:
    d["b"] = 1
