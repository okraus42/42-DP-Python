#!/usr/bin/python3
import sys

def find_the_redheads(people):
	return list((dict(filter(lambda person: person[1] == "red", people.items()))).keys())

if len(sys.argv) > 1:
	exit(2)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))