#!/usr/bin/python3
import sys

str = input("Please tell me your age: ")

try:
	num = int(str)
	if num >= 0:
		print(f"You are currently {num} years old.")
		x = 10
		while (x <= 30):
			print(f"In {x} years, you'll be {x + num} years old.")
			x += 10
	else:
		print("Invalid age.", file=sys.stderr)
except ValueError:
	print("Invalid input.", file=sys.stderr)
	