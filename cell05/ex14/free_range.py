#!/usr/bin/python3
import sys

if len(sys.argv) != 3:
	print("none")
	exit(2)

try:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])

except ValueError:
	print("Invalid values", file=sys.stderr)
	exit(2)

if (num2 - num1 > 10000):
	print("You are crazy!!!")
else:
	print(list(range(num1, num2 + 1)))
	