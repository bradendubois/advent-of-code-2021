"""
Normally I would clean up my solutions a bit, as an exercise to see how short
or efficient a solution I can reach. Since this initial solution managed to
reach the top 100 for both parts, I've decided to leave it as-is for preservation.
The only change made is one condition added to preserve the part-1 answer's correctness,
though it's marked.
"""

from collections import defaultdict
from sys import stdin
from itertools import product

data = [x.strip() for x in stdin.readlines()]
n = [[int(x) for x in line] for line in data]

flashes = 0

# for _ in range(100):

DDDD = 0
while True:
    DDDD += 1

    n = [[x + 1 for x in line] for line in n]
    cur = 0
    s = set()
    for i in range(10):
        for j in range(10):
            if n[i][j] > 9:
                s.add((i, j))

    f = set()
    while s:
        y, x = s.pop()
        if (y, x) in f:
            continue
        f.add((y, x))
        if DDDD <= 100: # addition of this condition is the only change I made
            flashes += 1
        cur += 1
        for dy, dx in product([-1, 0, 1], [-1, 0, 1]):
            if dy == 0 and dx == 0:
                continue
            py = y + dy
            px = x + dx

            if not (0 <= py < 10 and 0 <= px < 10):
                continue
            
            n[py][px] += 1
            if n[py][px] > 9:
                s.add((py, px))

    while f:
        y, x = f.pop()
        n[y][x] = 0


    if cur == 100:
        print(DDDD)
        break


print(flashes)


