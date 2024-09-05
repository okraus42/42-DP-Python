#!/usr/bin/python3
from sys import argv

if len(argv) < 2:
	print("none")
	exit(2)
for str in argv[1:]:
	if not str.endswith("ism"):
		print(f"{str}ism")