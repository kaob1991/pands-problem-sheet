# This program reads in a large text file and outputs the number of "e"s it contains 

# As per the brief I am using moby dick 

# Retrieved from: https://www.gutenberg.org/files/2701/old/moby10b.txt
# On 05/03/21 17:15
# 
 # ref https://www.sanfoundry.com/python-program-read-file-counts-number/
# Retrieved 05/03/21 18:19

# Author: Katie O'Brien 



k = 0
filename = "moby-dick.txt" 

with open (filename, "r") as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if letter == "e":
                    k = k + 1 
print (k)