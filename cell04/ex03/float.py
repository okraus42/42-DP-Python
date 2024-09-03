#!/usr/bin/python3
import sys

str = input("Give me a number: ")

try:
	num = float(str)
except ValueError:
	print("Invalid input.", file=sys.stderr)
	exit()
if num.is_integer():
	print("This number is an integer.")
else:
	print("This number is a decimal.")