# This program asks a user for an input of a positive number
# If the number is odd multiply by 3 and add 1 
# If it is even, divide by 2 
# If the number is 1, end the program

# References
# http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf
# Retrieved 27/03/21 @ 19.03

# Author: Katie O'Brien 



number = int(input(" Please input a positive integer: "))

while number <= 0:
    print ("Please enter a number greater than 0! ")
    number = int (input ("please enter a positive integer: "))
# the first section asks the user to input a real number, and ensures the program will run only with a 
# positive number

print (number) # prints the number selected

while number != 1:  # ensures the program stops at 1
    
    if number % 2 == 0: # if the number is divisible by 2 with no remainer (ie even)
        print (number // 2)  # print number divided by 2 
        number = number // 2  # number is now number divided by 2 

    elif number % 2 == 1:  # otherwise, if the number is odd 
        print (number * 3  + 1)  # print number * 3 + 1 
        number = number * 3 + 1  # number is now number multiplied by 3 + 1 

# once the number is 1 the program has no other statements to work with and ends  



