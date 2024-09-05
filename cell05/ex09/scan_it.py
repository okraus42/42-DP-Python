#!/usr/bin/python3
from sys import argv as a
import re

print("none" if len(a) != 3 else len(re.findall(a[1], a[2])) if len(re.findall(a[1], a[2])) and len(a[1]) else "none")
