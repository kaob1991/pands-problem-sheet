# This program is for obtaining a person's BMI from a read 
# Author: Katie O'Brien

#https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#Retrieved 05/03/21 16:59

weight = float(input('Please enter your weight: '))
cmHeight = float(input('Please enter your height in centimeters: '))

# This is a bit messy so far, need to see if there is a neater way of doing it 
meterHeight = cmHeight/100
BMI = (weight/(meterHeight*meterHeight))

 
BMInew = "{:.2f}".format(BMI) #{:.2f} displays the answer with only 2 decimal places after the answer
print('Your BMI is: ' + str(BMInew))