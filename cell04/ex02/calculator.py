#!/usr/bin/python3
import sys

str1 = input("Give me the first number: ")
str2 = input("Give me the second number: ")

try:
	num1 = int(str1)
	num2 = int(str2)
except ValueError:
	try:
		num1 = float(str1)
		num2 = float(str2)
	except ValueError:
		try:
			num1 = complex(str1)
			num2 = complex(str2)
		except ValueError:
			print("Invalid input.", file=sys.stderr)
			exit()
print("Thank you!")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if isinstance(num2, int):
	if (num2 != 0):
		print(f"{num1} / {num2} = {int(num1 / num2)}")
	else:
		print(f"{num1} / {num2} = KA-BOOM!")
elif isinstance(num2, float):
	if (num2 != 0.0):
		print(f"{num1} / {num2} = {float(num1 / num2)}")
	else:
		print(f"{num1} / {num2} = KA-BOOM!")
else:
	if (num2 != 0j):
		print(f"{num1} / {num2} = {num1 / num2}")
	else:
		print(f"{num1} / {num2} = KA-BOOM!")
print(f"{num1} * {num2} = {num1 * num2}")