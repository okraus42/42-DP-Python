#!/usr/bin/python3
import sys

str = input()

try:
	num = int(str)
	if num > 0:
		print("This number is positive.")
	elif num < 0:
		print("This number is negative.")
	else:
		print("This number is both positive and negative.")
except ValueError:
	try:
		num = float(str)
		if num > 0:
			print("This number is positive.")
		elif num < 0:
			print("This number is negative.")
		else:
			print("This number is both positive and negative.")
	except ValueError:
		print("Invalid input.", file=sys.stderr)
	