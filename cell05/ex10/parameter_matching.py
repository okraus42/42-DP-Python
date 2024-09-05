#!/usr/bin/python3
from sys import argv as a

print("none" if len(a) != 2 else "Good job!" if input("What was the parameter? ") == a[1] else "Nope, sorry...")
