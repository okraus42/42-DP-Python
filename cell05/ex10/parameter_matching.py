#!/usr/bin/python3
import sys
import re

if len(sys.argv) != 2:
	print("none")
	exit(2)
str = input("What was the parameter? ")
if str == sys.argv[1]:
	print("Good job!")
else:
	print("Nope, sorry...")