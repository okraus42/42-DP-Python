#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
	print("none")
	exit(2)

y = 0
while y <= 10:
	x = 0
	print(f"Table de {y}:", end='')
	while x <= 10:
		res = x * y
		print(f" {res}", end='')
		x += 1
	y += 1
	print()