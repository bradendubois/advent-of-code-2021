from sys import stdin

data = stdin.readlines()

# depth_aim is "depth" from p1, "aim" from p2
depth_aim = depth2 = x = 0

for i in data:
    line = i.split(" ")
    direction = line[0]
    amount = int(line[1])

    if direction == "down":
        depth_aim += amount
    elif direction == "up":
        depth_aim -= amount
    elif direction == "forward":
        x += amount
        depth2 += depth_aim * amount

print(x * depth_aim)
print(x * depth2)
