from collections import defaultdict
from sys import stdin
from itertools import product

data = [x.strip() for x in stdin.readlines()]

g = defaultdict(set)

for line in data:
    l, r = line.split("-")
    g[l].add(r)
    g[r].add(l)

q = [[["start"], False]]

b1 = b2 = 0
while q:
    
    cur, b = q.pop()
    adj = g[cur[-1]]

    if cur[-1] == "end":
        if not b:
            b1 += 1
        else:
            b2 += 1
        continue

    for item in adj:
        if item == "start":
            continue
        if all(x >= 'A' and x <= 'Z' for x in item):
            q.append([cur + [item], b])
        elif item not in cur:
            q.append([cur + [item], b])
        elif not b:
            q.append([cur + [item], True])

print(b1)
print(b1 + b2)
