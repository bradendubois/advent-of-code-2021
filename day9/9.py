from collections import defaultdict
from sys import stdin

data = [x.strip() for x in stdin.readlines()]

floor = [[int(x) for x in line] for line in data]

lows = []

for i in range(len(floor)):
    for j in range(len(floor[i])):
        adj = []
        if i > 0:
            adj.append(floor[i-1][j])
        if i < len(floor) - 1:
            adj.append(floor[i+1][j])
        if j > 0:
            adj.append(floor[i][j-1])
        if j < len(floor[i]) - 1:
            adj.append(floor[i][j+1])

        if all(x > floor[i][j] for x in adj):
            lows.append(floor[i][j])

print(len(lows) + sum(lows))


basins = defaultdict(set)
done = set()

def flood(y, x, basin):
    
    point = (y, x)
    done.add(point)
    if y < 0 or x < 0 or y == len(floor) or x == len(floor[0]):
        return

    if floor[y][x] == 9:
        return

    if point in basins[basin]:
        return

    basins[basin].add(point)
    flood(y-1, x, basin)
    flood(y+1, x, basin)
    flood(y, x-1, basin)
    flood(y, x+1, basin)

b = 0
for y in range(len(floor)):
    for x in range(len(floor[y])):
        if floor[y][x] == 9:
            continue
        if (y, x) in done:
            continue
        b += 1
        flood(y, x, b)
    
v = sorted([len(x) for x in basins.values()])
print(v[-1] * v[-2] * v[-3])
