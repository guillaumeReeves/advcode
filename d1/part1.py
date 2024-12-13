#!/bin/python

file = "numbers.txt"

d1 = []
d2 = []
with open(file) as f:
    for line in f:
        ls = line.split()
        d1.append(int(ls[0]))
        d2.append(int(ls[1]))

d1.sort()
d2.sort()

total = 0;
for i in range(len(d1)):
    diff = abs(d1[i] -d2[i])
    total += diff

print(total)
