# This program is for obtaining a person's BMI from 2 user inputs

# References:
# http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf
# Retrieved 27/03/21 @ 19.03

# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# Retrieved 05/03/21 @ 16:59

# https://jakevdp.github.io/WhirlwindTourOfPython/
# Retrieved 01/04/21 @ 17:00

# Author: Katie O'Brien

weight = float(input("Please enter your weight in kg's: ")) # asks for weight

cm_height = float(input('Please enter your height in centimeters: ')) # asks for height

 
meter_height = cm_height/100 # divides cm height by 100 to get height in meters

bmi = (weight/(meter_height*meter_height)) # bmi is weight divided by meter squared

 
bmi_new = "{:.2f}".format(bmi) # {:.2f} displays the answer with only 2 decimal places after the answer

print('Your BMI is: ' + str (bmi_new)) # prints the answer and converts bmi to string from float 