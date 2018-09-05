#! /usr/bin/env python3

from os import system

system("python manage.py dumpdata discordapp > discordapp/fixtures/initial_data_fixture.json")
print("\nDONE: Dumped \"superfam\" database!\nFind it in discordapp/fixtures/initial_data_fixture.json.\n")
