#! /usr/bin/env python3

# read the comments below and follow their directions so you can use this script

''' DOCUMENTATION

About:
	This script is fucking handy
	It handles a shitton of legwork required for developing a database
When to use it:
	- When you need to create the local database for the first time
	- When you update models.py
	- When you fuck up the data in the database
Usage:
	- change the ROOT_USER and CURRENT_USER variables below
	- delete the if ROOT_USER statement so the script doesn't exit
	- run $ ./refreshdb.py
Notes:
	- THIS SCRIPT DELETES ALL DATA MIGRATIONS
	- Make sure you know what a data migration is, and
	  that you know what discordapp/migrations/ is for
	  before running this
'''

from os import system
from sys import argv, exit

DATABASE = "superfam"
ROOT_USER = "davidmaness"  # REPLACE THIS WITH YOUR PSQL ROOT USER
CURRENT_USER = "david"  # REPLACE THIS WITH YOUR CURRENTLY LOGGED IN PSQL USER

# delete these two lines so this will actually run :3
if ROOT_USER != "davidmaness":
	print("READ THIS FILE BEFORE RUNNING IT")
	exit(1)


# WARNING: don't touch anything below this
# -----------------------------------------------------------------------------
print("If this is hanging, remember to stop the local server.")
system("dropdb {}".format(DATABASE))
system("createdb {}".format(DATABASE))
system("rm -rf discordapp/migrations/00*")
system("./manage.py makemigrations")
system("./manage.py migrate")
system('psql -U {ROOT_USER} -d {DATABASE} -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {CURRENT_USER}; GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO {CURRENT_USER};"'.format(ROOT_USER=ROOT_USER, DATABASE=DATABASE, CURRENT_USER=CURRENT_USER))
system("./manage.py loaddata initial_data_fixture.json")
print("\nDONE: Database {} successfully refreshed!\n".format(DATABASE))
