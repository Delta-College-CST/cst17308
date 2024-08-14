# This program demonstrates various date, time, and calendar functions
# builot into Python
# Reference:  https://www.w3schools.com/python/python_datetime.asp

#------------------------------------------------------#

from datetime import datetime

print(datetime.now())        # Write formal detailed date/time

print(datetime.now().month)  # Current month 

print(datetime.now().day)    # Current day

print(datetime.now().year)   # Current year

print(datetime.now().hour)   # Current hour

print(datetime.now().minute) # Current minute

print()

print(datetime.now().strftime("%a"))  # Day of week

print(datetime.now().strftime("%x"))  # Full date

print(datetime.now().strftime("%X"))  # Full time

print()

#------------------------------------------------------#

import calendar

print(calendar.month(2024, 12))

print()

#------------------------------------------------------#

