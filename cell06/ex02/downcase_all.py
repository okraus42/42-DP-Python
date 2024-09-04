#!/usr/bin/python3
import sys

def downcase_it(s: str) -> str:
	return s.lower()

if len(sys.argv) < 2:
	print("none")
	exit(2)

for str in sys.argv[1:]:
	print(downcase_it(str))
