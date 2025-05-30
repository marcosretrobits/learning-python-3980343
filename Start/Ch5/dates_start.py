#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
# print("oggi:", today)

# print out the date's individual components
# print("data:",today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("week day", today.weekday())

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print("Adesso:", today)

# Get the current time
t = datetime.time(datetime.now())
print(t)