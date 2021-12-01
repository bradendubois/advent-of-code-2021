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
    a = sum(data[i:i+3])
    b = sum(data[i+1:i+4])

    if b > a:
        t += 1

print(t)
