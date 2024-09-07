#!/usr/bin/python3
import sys

def shrink(s: str): print(s[:8])

def enlarge(s: str): print(s + 'z' * (8 - len(s)))

if len(sys.argv) < 2:
	print("none")
	exit(2)

for str in sys.argv[1:]:
	if (len(str) > 8):
		shrink(str)
	elif (len(str) < 8):
		enlarge(str)
	else:
		print(str)
