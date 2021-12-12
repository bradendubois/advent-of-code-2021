from collections import defaultdict
from sys import stdin

data = [x.strip() for x in stdin.readlines()]

l = ["[", "(", "{", "<"]
r = ["]", ")", "}", ">"]

inv = []
inc = []

for line in data:
    s = []
    bad = False
    for c in line:
        if c in r and len(s) == 0:
            inv.append(c)
            bad = True
            break
        
        if c in l:
            s.append(c)
            continue
        LE = s.pop()

        if LE == "[" and c != "]" or LE == "{" and c != "}" or LE == "(" and c != ")" or LE == "<" and c != ">":
            inv.append(c)
            bad = True
            break
            

    if len(s) != 0 and not bad:
        inc.append(s)

r = dict([(")", 3), ("]", 57), ("}", 1197), (">", 25137)])
print(sum(map(lambda x: r[x], inv)))

t2 = []
r = dict([("(", 1), ("[", 2), ("{", 3), ("<", 4)])
for line in inc:
    t = 0
    while line:
        c = line[-1]
        line = line[:-1]
        t *= 5
        t += r[c]
    t2.append(t)

print(sorted(t2)[len(t2) // 2 ])
