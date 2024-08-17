# This program prompts the user for a year.  The month and day of a birthday are defined as constants. 
# The program then calculates the day of the week for the birthday in the given year.

MONTH = 5
DAY   = 5

import datetime

year = int(input("Enter year: "))

futureDate = datetime.datetime(year, MONTH, DAY)

print("In",year,"my birthday falls on a",futureDate.strftime("%A"))
