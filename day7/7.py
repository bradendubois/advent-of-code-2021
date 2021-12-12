from collections import defaultdict
from sys import stdin

data = [x.strip() for x in stdin.readlines()]
n = [int(x) for x in data[0].split(",")]

m1 = m2 = 99999999999

def diff(x, i):
    n = abs(x - i)
    return n * (n + 1) // 2

for i in range(min(n), max(n)+1):

    t1 = sum(map(lambda v: abs(v - i), n))
    if t1 < m1:
        m1 = t1

    t2 = sum(map(lambda v: diff(v, i), n))
    if t2 < m2:
        m2 = t2

print(m1)
print(m2)
