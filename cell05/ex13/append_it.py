#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
	print("none")
	exit(2)
for str in sys.argv[1:]:
	if not str.endswith("ism"):
		print(f"{str}ism")