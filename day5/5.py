from sys import stdin
from collections import defaultdict

data = [x.strip() for x in stdin.readlines()]

floor = defaultdict(int)
diag = defaultdict(int)

for line in data:
    l, arr, r = line.split(" ")
    x1, y1 = [int(x) for x in l.split(",")]
    x2, y2 = [int(x) for x in r.split(",")]

    if x1 == x2:
        for i in range(min([y1, y2]), max([y1, y2]) + 1):
            floor[(x1, i)] += 1
    
    elif y1 == y2:
        for i in range(min([x1, x2]), max([x1, x2]) + 1):
            floor[(i, y1)] += 1

    else:
        lx, ly, rx, ry = (x1, y1, x2, y2) if x1 < x2 else (x2, y2, x1, y1)
        
        if ly < ry:
            while lx != rx+1:
                diag[(lx, ly)] += 1
                lx += 1
                ly += 1
        elif ly > ry:
            while lx != rx+1:
                diag[(lx, ly)] += 1
                lx += 1
                ly -= 1


straight = len(list(filter(lambda x: x >= 2, floor.values())))
print(straight)

for k, v in diag.items():
    floor[k] += v
diagonal = len(list(filter(lambda x: x >= 2, floor.values())))
print(diagonal)
