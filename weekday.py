# This program reads what day of the week it is and outputs one of 2 statements 
# Depending on whether it is a weekday or weekend 

#Author: Katie O'Brien 

import datetime #Allows work with dates as objects

weekdayNumber = datetime.datetime.today().weekday()
# This creates a variable with a value of 0-6 (via weekday()) based on the datetime.today function
#Information regarding this piece of code was retrieved from
# https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python
# (Retrieved 14/02/21 @ 14:00)

if weekdayNumber <5: # Ie, between Monday (0) and Friday (4)
    print ("Yes, unfortunately today is a weekday.")

else:
    print("It is the weekend, yay!")