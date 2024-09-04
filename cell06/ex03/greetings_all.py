#!/usr/bin/python3
import sys

def greetings(name = 'noble stranger'):
	if isinstance(name, str):
		print(f"Hello, {name}.")
	else:
		print("Error! It was not a name.", file=sys.stderr)

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
