#!/usr/bin/python3
import sys

str = input()

try:
	num = int(str)
	if num != 0:
		print("This number is different from zero.")
	else:
		print("This number is equal to zero.")
except ValueError:
	try:
		num = float(str)
		if num != 0:
			print("This number is different from zero.")
		else:
			print("This number is equal to zero.")
	except ValueError:
		try:
			num = complex(str)
			# In Python, the letter 'j' denotes the imaginary unit.
			# 0+0j
			# 1+2j 
			if num != complex(0, 0):
				print("This number is different from zero.")
			else:
				print("This number is equal to zero.")
		except ValueError:
			print("Invalid input.", file=sys.stderr)
	