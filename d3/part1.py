#!/bin/python
import re

def main():    
    file = "data.txt"

    with open(file, 'r') as f:
        data = f.read() 

    regexp = "mul\(([0-9]{1,3},[0-9]{1,3})\)"
    matches = re.findall(regexp, data)

    total = 0
    for m in matches:
        nums = m.split(',')
        total += (int(nums[0]) * int(nums[1]))

    print(total)

if __name__ == "__main__":
    main()
