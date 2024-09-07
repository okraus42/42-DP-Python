#!/usr/bin/python3
import sys

def add_one(x):	x += 1
	# return x

if len(sys.argv) > 1:
	exit(2)

y = 5

print (y)
add_one(y)
print (y)
# y = add_one(y)
# print (y)
