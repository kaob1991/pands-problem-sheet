# Program to create a function that will use the Newton-Raphson method of obtaining 
# A square root of a number using repeated iterations 

# References:
# https://jakevdp.github.io/WhirlwindTourOfPython/
# Retrieved 01/04/21 @ 17:00
# https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python
# Retrieved 05/03/21 @ 16:40
# https://medium.com/swlh/finding-a-functions-roots-with-python-590eca0d22a5
# Retrieved 05/03/21 @ 16:40
# https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
# Retrieved 05/03/21 @ 16:41
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# Retrieved 05/03/21 @ 16.59

# Author: Katie O'Brien 

def sqrt (number): # creating a function to get our square root
    func_number = number # sets number within function  to number
    iterator = 1.00 # iteration initialisation
    accuracy = .00000001 # accuracy after decimal place
    while func_number-iterator>accuracy: # while number minus iterator is greater that accuracy 
        func_number = (func_number + iterator)/ 2 # number equals number plus iterator divided by 2
        iterator = number/func_number # iterator equals number divided by number within function

    square = ("%.1f" % func_number) # this is reducing the number of decimal places displayed to 1
    print ("The square root of {} is approx {}. ".format (number,square)) 
        # prints the square root using input number and answer 

number = float(input("Please enter a positive number : ")) # sets number as a float input from user 
sqrt (number) # uses the sqrt function on number


