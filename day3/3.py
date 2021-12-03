from sys import stdin

data = [x.strip() for x in stdin.readlines()]

epsilon = ""
gamma = ""

for i in range(len(data[0])):

    zero = len([x for x in data if x[i] == "0"])
    ones = len(data) - zero

    epsilon += "1" if zero > ones else "0"
    gamma += "0" if zero > ones else "1"

print(epsilon, gamma, int(epsilon, base=2) * int(gamma, base=2))

# part 2

oxygen = ""
co2 = ""

data_o = [x.strip() for x in data]
data_c = [x.strip() for x in data]

for i in range(len(data[0])):

    zero_o = [x for x in data_o if x[i] == "0"]
    ones_o = [x for x in data_o if x[i] == "1"]
    data_o = ones_o if len(ones_o) >= len(zero_o) else zero_o

    if len(data_o) == 1 and oxygen == "":
        oxygen = data_o.pop()

    zero_c = [x for x in data_c if x[i] == "0"]
    ones_c = [x for x in data_c if x[i] == "1"]
    data_c = ones_c if len(zero_c) > len(ones_c) else zero_c

    if len(data_c) == 1 and co2 == "":
        co2 = data_c.pop()

print(int(oxygen, 2) * int(co2, 2))
