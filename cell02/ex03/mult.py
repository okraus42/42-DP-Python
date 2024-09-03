#!/usr/bin/python3
import sys

print("Enter the first number:")
str1 = input()
print("Enter the second number:")
str2 = input()

try:
	num1 = int(str1)
	num2 = int(str2)
	res = num1 * num2
	print(f"{num1} x {num2} = {res}")
	if res > 0:
		print("The result is positive.")
	elif res < 0:
		print("The result is negative.")
	else:
		print("The result is both positive and negative.")
except ValueError:
	try:
		num1 = float(str1)
		num2 = float(str2)
		res = num1 * num2
		print(f"{num1} x {num2} = {res}")
		if res > 0:
			print("The result is positive.")
		elif res < 0:
			print("The result is negative.")
		else:
			print("The result is both positive and negative.")
	except ValueError:
		print("Invalid input.", file=sys.stderr)
	