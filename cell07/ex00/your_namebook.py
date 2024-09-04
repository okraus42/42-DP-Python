#!/usr/bin/python3
import sys

def array_of_names(people):
	return_list = []
	for key, value in people.items():
		return_list.append(key.capitalize() + " " + value.capitalize())
	return return_list

if len(sys.argv) > 1:
	exit(2)

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))