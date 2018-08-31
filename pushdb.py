#! /usr/bin/env python3

'''
Run this without any arguments to replace the server database with your local one.
Process:
	Step 1. Delete the database on the server
	Step 2. Push the local database up to the server

Notes:
	- Reponse must be a capital Y for it to work.
'''

from os import system
from sys import argv, exit
from time import sleep

# hardcoded for easy changing
db = "superfam"
remote_db = "postgresql-flat-22036"
heroku_app = "discord-project"

print("\nWARNING.\nYou are about to push the local version of database '{}' to the server.\n".format(db))
sleep(2)
response = input("Is that what you want?\n(Y/n)\n")

if response == "Y":
    # Step 1
	system("heroku pg:reset --confirm {}".format(heroku_app))
    # Step 2
	system("heroku pg:push {} {} --app {}".format(db, remote_db, heroku_app))
	print("Done.")
else:
	print("\nCancelled.")
	exit(1)
