#Understanding the basics of this Django project

##Be sure to run the following for global dependencies on a Unix system:
## $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

1. We need to install our global dependencies.
	- $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
	- $sudo su - postgres
		- this gives admin access to the OS user
	- $ pip install virtualenv
		- this installs our virtual environment program
		- requires pip


2. We need to install our app dependencies.
	- $ . env/bin/activate
		- this activates the virtual environment in which we will install our app dependencies.
		- the virtual environment needs to be active while the local instance of the app is running.
		- to exit the virtual environment, enter $ deactivate.
	- $ pip install -r requirements.py
		- this will install each of the python and django dependencies listed in requirements.py

3. Dedicate a terminal window for running the local server.
	- Ensure that discordproject/settings.py is configured to run locally.
		- Make sure the NON-PROD instance of the database variable is uncommented.
		- make sure DEBUG is set to True
	- Run $ python manage.py runserver
	- View the app at localhost:8000


./discordproject
	- this is the "project folder" for our app.
	- inside contains important files, like settings.py
	- there's also the urls.py file, which links endpoints (urls) to views (the django term for backend functions, like rendering a page)

./discordproject/settings.py
	- this is where the main configuration for the application happens.
	- we set a lot of django variables here, like which database engine to run
	- we also set other stuff that I'll get to later I guess.

./
