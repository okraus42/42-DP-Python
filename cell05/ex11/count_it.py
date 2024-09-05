#!/usr/bin/python3
from sys import argv as a

print(*[f"parameters: {len(a[1:])}", *[f"{b}: {len(b)}" for b in a[1:]]] if len(a) >= 2 else ["none"], sep='\n')
#thanks gharazka