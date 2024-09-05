#!/usr/bin/python3
from sys import argv as a

print (*a[:0:-1] if len(a) > 2 else ["none"], sep="\n")