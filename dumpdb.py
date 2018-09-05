#! /usr/bin/env python3

'''
This script takes the current database with the name 'superfam' and dumps it to a JSON file located in discordapp/fixtures/

Everything is hardcoded so if you want to change anything, I'd recommend creating the variables outside of the system() call and doing string substitution so it can be easily changed. Even better, from sys import argv and use terminal parameters.
'''

from os import system

system("python manage.py dumpdata discordapp > discordapp/fixtures/initial_data_fixture.json")
print("\nDONE: Dumped \"superfam\" database!\nFind it in discordapp/fixtures/initial_data_fixture.json.\n")
