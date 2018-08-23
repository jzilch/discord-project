# Understanding the basics of this Django project

### Follow these steps to be able to help develop this app:
###	* Use Brew in place of apt-get on Mac Osx

1. First we need to install our global dependencies.
	- $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
	- $sudo su - postgres
		- this gives admin access to the OS user
	- $ pip install virtualenv
		- this installs our virtual environment program
		- requires pip


2. Next we need to install our app dependencies.
	- $ . env/bin/activate
		- this activates the virtual environment in which we will install our app dependencies.
		- the virtual environment needs to be active while the local instance of the app is running.
		- to exit the virtual environment, enter $ deactivate.
	- $ pip install -r requirements.txt
		- this will install each of the python and django dependencies listed in requirements.txt

3. Now we should dedicate a terminal window for running the local server.
	- Ensure that discordproject/settings.py is configured to run locally.
		- Make sure the NON-PROD instance of the database variable is uncommented.
		- make sure DEBUG is set to True
	- Run $ python manage.py runserver
	- View the app at localhost:8000


### Here is a brief rundown of the app directory.

#### ./discordproject/
	- this is the "project folder" for our app.
	- inside contains important files, like settings.py
	- there's also the urls.py file, which links endpoints (urls) to views (the django term for backend functions, like rendering a page)

#### ./discordproject/settings.py
	- this is where the main configuration for the application happens.
	- we set a lot of django variables here, like which database engine to run
	- we also set other stuff that I'll get to later I guess.

#### discordapp/
	- this is our "app folder".
	- inside contains the "meat" of our project, such as
		- html / css / javascript
		- compressed image files
		- other juicy shit

#### requirements.txt
	- run $ pip install -r requirements.txt to install all of these dependencies into your current environment.
	- you can $ pip freeze > requirements.txt;  to create a new version of requirements.txt with all your currently installed dependencies.
