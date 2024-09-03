#!/usr/bin/python3
import sys
import math

str = input("Give me a number: ")

try:
	num = float(str)
except ValueError:
	print("Invalid input.", file=sys.stderr)
	exit()
print(math.ceil(num))
