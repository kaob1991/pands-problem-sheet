# This program reads what day of the week it is and outputs one of 2 statements 
# Depending on whether it is a weekday or weekend using datetime 

#References:
# https://jakevdp.github.io/WhirlwindTourOfPython/
# Retrieved 01/04/21 @ 17:00
# https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python
# Retrieved 14/02/21 @ 14:00
# https://docs.python.org/3/library/datetime.html
# Retrieved 14/02/21 @ 14.00

#Author: Katie O'Brien 


import datetime # allows work with dates as objects

weekday_number = datetime.datetime.today().weekday()
# This creates a variable with a value of 0-6 (via weekday()) based on the datetime.today function


if weekday_number <5: # Ie, between Monday (0) and Friday (4)
    print ("Yes, unfortunately today is a weekday.") # Prints response

else: # Otherwise, ie if number is either 5 or 6 (Sat/Sun)
    print("It is the weekend, yay!") # Prints response