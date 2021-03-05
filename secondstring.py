# This program reads a string and outputs every second letter in reverse order 

#Author: Katie O'Brien 

inputString = input("Please enter a sentence: ")

outputBackwards = inputString[::-1]
# This reverses the string starting at position 0 and reversing one character each time
# ref https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# Retrieved 4/02/21 18:00

every2ndLetter = outputBackwards[::2]
# This outputs the reversed sentence by telling Python to start at pos 0 and return every other character 
# ref https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python
# Retrieved 4/02/21 18:20

print(every2ndLetter)