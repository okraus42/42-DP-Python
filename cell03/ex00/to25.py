#!/usr/bin/python3
import sys

print("Enter a number less than 25")
str = input()

try:
	num = int(str)
	if num <= 25:
		while num <= 25:
			print(f"Inside the loop, my variable is {num}")
			num += 1
	else:
		print("Error", file=sys.stderr)
except ValueError:
	print("Invalid input.", file=sys.stderr)
	