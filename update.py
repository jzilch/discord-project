#! /usr/bin/env python3

import os

os.system("git fetch upstream")
os.system("git checkout master")
os.system("git merge upstream/master")
os.system("git checkout develop")
os.system("git merge upstream/develop")
