#!/bin/python

def checkIncrease(a, b) -> bool:
    if(b > a):
        return True 

    return False

def isIncreasing(report) -> bool:
    for i in range(len(report)-1):
        if(checkIncrease(report[i], report[i+1]) == False):
            return False

    return True

def checkDecrease(a, b) -> bool:
    if(b < a):
        return True

    return False

def isDecreasing(report) -> bool:
    for i in range(len(report)-1):
        if(checkDecrease(report[i], report[i+1]) == False):
            return False

    return True

def checkSmallChange(report) -> bool:
    for i in range(len(report)-1):
        if(isSmallChange(report[i], report[i+1]) == False):
            return False

    return True

def isSmallChange(a, b) -> bool:
    change = abs(a-b)
    if(change <= 3 and change >= 1):
        return True

    return False

def isSafe(report) -> bool:
    if((isIncreasing(report) == False and isDecreasing(report) == False) or checkSmallChange(report) == False):
        return False


    return True

## create copy of list by removing each element once
def dampen(report) -> list:
    reports = []
    for i in range(len(report)):
        rc = report.copy()
        rc.pop(i)
        reports.append(rc)

    return reports

def checkWithProblemDampener(report) -> bool:
    ## Check the initial report first to avoid dampening if there is no need
    if(isSafe(report) == True):
        return True

    dampenedReports = dampen(report)
    for dreport in dampenedReports:
        if(isSafe(dreport) == True):
            return True

    return False


def main():    
    file = "data.txt"

    reports = []
    with open(file) as f:
        for line in f:
            ls = line.split()
            for i in range(len(ls)):
                ls[i] = int(ls[i])
    
            reports.append(ls)
    
    safe = 0
    for report in reports:
        if(checkWithProblemDampener(report) == True):
            safe += 1
    
    print(f"Total of {safe} safe reports")

if __name__ == "__main__":
    main()
