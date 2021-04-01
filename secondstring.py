# This program reads a string and outputs every second letter in reverse order 

# References: 
# https://jakevdp.github.io/WhirlwindTourOfPython/
# Retrieved 01/04/21 @ 17:00
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# Retrieved 4/02/21 @ 18:00
# http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf
# Retrieved 27/03/21 @ 19.03
# https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python
# Retrieved 4/02/21 @ 18:20

#Author: Katie O'Brien 

input_string = input("Please enter a sentence: ") # asks user to input a sentence 

output_backwards = input_string[::-1]
# this reverses the string starting at position 0 and reversing one character each time


every_2nd_letter = output_backwards[::2]
# this outputs the reversed sentence by telling Python to start at pos 0 and return every other character 


print(every_2nd_letter) # prints result