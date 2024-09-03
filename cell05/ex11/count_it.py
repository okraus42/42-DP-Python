#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
	print("none")
	exit(2)
print("parameters:", len(sys.argv) - 1)
for str in sys.argv[1:]:
	print(f"{str}: {len(str)}")