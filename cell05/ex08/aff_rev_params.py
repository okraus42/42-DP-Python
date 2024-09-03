#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
	print("none")
	exit(2)
x = len(sys.argv) - 1
while x > 0:
	print(sys.argv[x])
	x -= 1