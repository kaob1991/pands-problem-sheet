# Program to create a function that will use the Newton-Raphson method of obtaining 
# A square root of a number using repeated iterations 

# References:
# https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python
# Retrieved 05/03/21 @ 16:40
# https://medium.com/swlh/finding-a-functions-roots-with-python-590eca0d22a5
# Retrieved 05/03/21 @ 16:40
# https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
# Retrieved 05/03/21 @ 16:41
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# Retrieved 05/03/21 @ 16.59

# Author: Katie O'Brien 

def sqrt (n): # creating a function to get our square root
    x = n # sets x to n
    y = 1.00 # iteration initialisation
    e = .00000001 # accuracy after decimal place
    while x-y>e: # while x minus y is greater that e 
        x = (x + y)/ 2 # x equals x plus y divided by 2
        y = n/x # y equals n divided by x

    f = ("%.1f" % x) # this is reducing the number of decimal places displayed to 1
    print ("The square root of {} is approx {}. ".format (n,f)) 
        # prints the square root using input number and answer 

n = float(input("Please enter a positive number : ")) # sets n as a float input from user 
sqrt (n) # uses the sqrt function on n


