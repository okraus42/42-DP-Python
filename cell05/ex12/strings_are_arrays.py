#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
	print("none")
	exit(2)
z = 0
for char in sys.argv[1]:
	if char == 'z':
		z += 1
if z == 0:
	print("none")
else:
	print("z" * z)