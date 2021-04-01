# This program reads in a large text file and outputs the number of "e"s it contains 
# The program will take the filename in from an arguement on the command line
# As per the brief I am using moby dick 

# References:

# https://www.gutenberg.org/files/2701/old/moby10b.txt
    # Retrieved 05/03/21 @ 17:15
 
# https://www.sanfoundry.com/python-program-read-file-counts-number/
    # Retrieved 05/03/21 @ 18:19

# https://www.tutorialsteacher.com/python/sys-module
    # Retrieved 27/03/21 @ 18:15

#https://jakevdp.github.io/WhirlwindTourOfPython/
    # Retrieved 01/04/21 @ 17:00

# Author: Katie O'Brien 

import sys # module to manipulate the Python runtime environment

k = 0 # base for appending the number of e's in file
filename = sys.argv [1] # returns a list of command line arguments passed to a Python script

with open (filename, "r") as f: # opens the mobydick.txt file
    for line in f: # takes each line in mobydick file
        words = line.split() # takes each word by splitting the line
        for i in words: # seperates the words out
            for letter in i:
                if letter == "e": # asks if the letter is "e"
                    k = k + 1 # if it is, appends to k and increases the value by 1
print (k) # prints the result
