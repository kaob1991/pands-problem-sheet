# This program asks a user for an input of a positive number
# If the number is odd multiply by 3 and add 1 
# If it is even, divide by 2 
# If the number is 1, end the program

# Author: Katie O'Brien 


#The first section asks the user to input a real number, and ensures the program will run only with a 
# positive number 

number = int(input(" Please input a positive integer: "))
while number <= 0:
    print ("Please enter a number greater than 0! ")
    number = int (input ("please enter a positive integer: "))

print (number) #prints the number selected

while number != 1:  #ensures the program stops at 1
    
    if number % 2 == 0: #If the number is divisible by 2 with no remainer (ie even)
        print (number // 2)  #print number divided by 2 
        number = number // 2  # number is now number divided by 2 

    elif number % 2 == 1:  # Otherwise, if the number is odd 
        print (number * 3  + 1)  #Print number * 3 + 1 
        number = number * 3 + 1  #Number is now number multiplied by 3 + 1 

# Once the number is 1 the program has no other statements to work with and ends  



