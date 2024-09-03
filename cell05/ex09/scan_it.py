#!/usr/bin/python3
import sys
import re

if len(sys.argv) != 3:
	print("none")
	exit(2)
x = re.findall(sys.argv[1], sys.argv[2])
if x:
	print(len(x))
else:
	print("none")