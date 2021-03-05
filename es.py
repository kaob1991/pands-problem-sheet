# This program reads in a large text file and outputs the number of "e"s it contains 

#Ref: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-7.php

# Retrieved 05/03/21 18:00

# https://docs.python.org/3/library/collections.html#collections.Counter.elements
# Retrieved 05/03/21 18: 05

# As per the brief I am using moby dick 
# Retrieved from: https://www.gutenberg.org/files/2701/old/moby10b.txt
# On 05/03/21 17:15
# 
# Author: Katie o'Brien 

import collections
import pprint


filename = "moby-dick.txt"

with open (filename, "r") as info:
    count = collections.Counter(info.read())
 
    Newvalue = pprint.pformat (count)

print(Newvalue)
    

#This one works but prints all characters
# Leaving it aside to do a 2nd program
#Will return to this one as its my preferred way of retrieving the answer 