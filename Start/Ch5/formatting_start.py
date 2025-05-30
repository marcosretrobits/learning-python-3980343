
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now()

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
# print(now.strftime("Year: %Y %y"))
# print(now.strftime("%a %A %b %B"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
# print(now.strftime("Locale %c"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("aaa %I %M %S"))