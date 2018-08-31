#! /usr/bin/env python3

'''
About:
	This script is fucking dope
	It handles a shitton of legwork required for developing a database
When to use it:
	- When you update models.py
	- When you fuck up the data in the database
Usage:
	./refreshdb.py <db_name> <psql_user>
	- for example, $ ./refreshdb.py superfresh david
	- psql_user is whatever user you want to use for postgres
Notes:
	- THIS SCRIPT DELETES ALL DATA MIGRATIONS
	- Make sure you know what a data migration is, and
	  that you know what discordapp/migrations/ is for
	  before running this
'''

from os import system
from sys import argv, exit

if len(argv) != 3:
	print("\nUsage: refreshdb.py <db_name> <psql_user>")
	exit(1)

db = argv[1]

system("dropdb {}".format(db))
system("createdb {}".format(db))
system("rm -rf discordapp/migrations/00*")
system("./manage.py makemigrations")
system("./manage.py migrate")
system('psql -U davidmaness -d {} -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO david; GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO david;"'.format(db))
system("./manage.py loaddata initial_data_fixture.json")
print("Database {} refreshed.".format(db))
