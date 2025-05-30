#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Exists:", path.exists("textfile.txt"))
print("is file:", path.isfile("textfile.txt"))
print("is dir:", path.isdir("textfile.txt"))

# Work with file paths
print("Path:", path.realpath("textfile.txt"))
print("Path & name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"{td.total_seconds()}")