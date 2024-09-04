#!/usr/bin/python3
import sys

def average(students):
	scores = list(students.values())
	if len(scores) > 0:
		return sum(scores) / len(scores)
	else:
		return 0

if len(sys.argv) > 1:
	exit(2)

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")