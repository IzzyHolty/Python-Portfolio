# This program tells whether a given year is a leap year or not based on the revised Julian calendar rule.
# Information on Julian Revised Calendars can be found here - https://en.wikipedia.org/wiki/Revised_Julian_calendar#Implementation

import random
import sys
import os

#leap year checking function
def isleapyear(int):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0) or (year % 900 == 200 or 600)) :
        print(year, "is a leap year.")
        return True
    else :
        print(year, "is not a leap year.")
        return False

#validating user input

while True:
    try:
        year = int(input("What year would you like to test? "))
    except ValueError:
        print("That's not a year!")
        continue
    else:
        break

yearcheck = isleapyear(year)




