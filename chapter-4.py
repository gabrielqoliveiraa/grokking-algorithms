
# Chapter4

import math

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def recursiveSumCountItemsList(list):
    if list == []:
        return 0
    return list[0] + recursiveSumCountItemsList(list[1:])

def recursiveCountItems(list):
    if list == []:
        return 0
    return 1 + recursiveCountItems(list[1:])

def recursiveMaxValue(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        sub_max = recursiveMaxValue(list[1:])
        return list[0] if list[0] > sub_max else sub_max


def binarySearch(list, target: int):
    min = 0
    max = len(list)
    while min <= max:
        middle = math.floor((min + max)/2)
        print(min, max)
        if list[middle] > target:
            max = middle - 1
        if list[middle] < target:
            min = middle + 1
        if min == max:
            return -1
        if list[middle] == target:
            break
    return middle

def recursiveBinarySearch(list, min, max, target):
    if(max >= min):
        midIndex = (max + min) // 2
        middle = list[midIndex]
        if middle == target:
            return midIndex
        elif middle > target:
            return recursiveBinarySearch(list, min, midIndex - 1, target)
        else: 
            return recursiveBinarySearch(list, midIndex + 1, max, target)
    else:
        return None

list = [1,2,4,7, 10, 11, 15]
print(recursiveBinarySearch(list, 0, len(list), 10))


