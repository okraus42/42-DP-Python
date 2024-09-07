#!/usr/bin/python3
import sys

def famous_births(people):
	for value in dict(sorted(people.items(), key=lambda item: (int((item[1])['date_of_birth'])))).values(): print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")

if len(sys.argv) > 1:
	exit(2)

#dictionary with value dictionary
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)