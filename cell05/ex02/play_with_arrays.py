#!/usr/bin/python3
import sys

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr1)
arr2 = [element + 2 for element in arr1 if element > 5]
print(arr2)