# Write a program that displays a plot of the functions
# f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
 
# As range [0,4] is ambiguous (ie range will only run to 3, and as [] determines a list with 4 included,
# I have decided to use 3 as the upper limit of the scale)

# Reference: 
# https://www.w3schools.com/python/matplotlib_pyplot.asp
    # Retrieved 27/03/21 @ 17.49
#https://jakevdp.github.io/WhirlwindTourOfPython/
    # Retrieved 01/04/21 @ 17:00

# Author Katie O'Brien 

import matplotlib.pyplot as plt # import Matplotlib pyplot function
import numpy as np # import NumPy 
 
# function 1 
# f (x) = x
xpoints = np.array ([0,1,2,3]) # setting range as above
ypoints = xpoints # as f(x) = x; y is also equal to x

plt.plot (xpoints, ypoints,ls = "--", color = "g")
 # plotting result with linestyle as dashed, and colour as green


# function 2
# g(x) = x2
xpoints = np.array([0,1, 2, 3 ]) # setting range as above
ypoints = xpoints * xpoints # as per function x = x2; y therefore is x squared

plt.plot (xpoints, ypoints, ls = "--", color = "c")
# plotting result with linestyle as dashed, and colour as cyan"

# function 3
# h(x) = x3
xpoints = np.array ([0,1,2,3]) # setting range as above
ypoints = xpoints ** xpoints # as per function x = x3; y therefore is x cubed

plt.plot (xpoints, ypoints,ls = "--", color = "m")
# plotting result with linestyle as dashed and colour as magenta

plt.xlabel ("x-axis") # labelling x axis
plt.ylabel ("y-axis") # labelling y axis
plt.title ("Plot Task") # labelling title
plt. grid ("both",lw = "1", ls = ":", color = "k") 
# setting grid-lines for ease of viewing




plt.show() # shows the plot with variables as set above 




