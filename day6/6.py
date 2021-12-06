from collections import defaultdict
from sys import stdin

data = [x.strip() for x in stdin.readlines()]
n = [int(x) for x in data[0].split(",")]

v = {i: n.count(i) for i in range(9)}

for _ in range(256):

    if _ == 80:
        print(sum(v.values()))

    new = defaultdict(int)

    for i in range(9):
        if i == 0:
            new[8] += v[0]
            new[6] += v[0]
        else:
            new[i-1] += v[i]
    
    v = new

print(sum(v.values()))
