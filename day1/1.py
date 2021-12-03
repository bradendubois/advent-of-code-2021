from sys import stdin

data = [int(x) for x in stdin.readlines()]

# Part 1

t = 0

for i in range(len(data)-1):
    if data[i+1] > data[i]:
        t += 1

print(t)

# Part 2

t = 0

for i in range(len(data)-3):
    if data[i+3] > data[i]:
        t += 1

print(t)
