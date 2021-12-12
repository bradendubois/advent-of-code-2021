from collections import defaultdict
from sys import stdin

data = [x.strip() for x in stdin.readlines()]

t1 = t2 = 0

for line in data:

    start = {x: letters.copy() for x in letters}

    wires, result = line.split(" | ")
    wires = wires.split(" ")
    display = result.split(" ")

    w2 = [i for i in wires if len(i) == 2].pop()
    w4 = [i for i in wires if len(i) == 4].pop()
    
    s2 = set(w2)
    s4 = set(w4)

    x = ""
    for num in display:
        l = len(num)

        if l == 2:
            t1 += 1
            x += "1"
        elif l == 3:
            t1 += 1
            x += "7"
        elif l == 4:
            t1 += 1
            x += "4"
        elif l == 7:
            t1 += 1
            x += "8"
        
        elif l == 5:
            if len(set(num) & s4) == 2:
                x += "2"
            elif len(set(num) & s2) == 2:
                x += "3"
            else:
                x += "5"
        elif l == 6:
            if len(set(num) & s2) == 1:
                x += "6"
            elif len(set(num) & s4) == 4:
                x += "9"
            else:
                x += "0"

        else:
            print("uh oh what did i do")

    t2 += int(x)

print(t1)
print(t2)
