#! /usr/bin/env python3

import os

print("Fetching upstream")
os.system("git fetch upstream")
print("Updating master with upstream changes")
os.system("git checkout master")
os.system("git merge upstream/master")
print("Updating develop with upstream changing")
os.system("git checkout develop")
os.system("git merge upstream/develop")
print("Updated local repository.\nNow on develop.")
