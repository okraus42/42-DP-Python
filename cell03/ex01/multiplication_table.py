#!/usr/bin/python3
import sys

print("Enter a number")
str = input()

try:
	num = int(str)
except ValueError:
	print("Invalid input.", file=sys.stderr)
	exit(1)
for i in range(10):
	res = num * i
	print(f"{i} x {num} = {res}")