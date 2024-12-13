#!/bin/python

def getCount(num, d2) -> int:
    count = d2.count(num)
    return count * num

file = "data.txt"

d1 = []
d2 = []
with open(file) as f:
    for line in f:
        ls = line.split()
        d1.append(int(ls[0]))
        d2.append(int(ls[1]))

total = 0;
for i in d1:
    total += getCount(i, d2)

print(total)



