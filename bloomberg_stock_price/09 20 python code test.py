import pandas as pd
import numpy as np
import time
import sklearn


print "My name is %s and weight is %d kg!" % ('Zara', 21)
## The dir() Function
## The dir() built-in function returns a sorted list of strings containing the names defined by a module.
import math
content = dir(math)
print content


################################## python I/O ################################
## The raw_input Function
#str = raw_input("Enter your input: ");
#print "Received input is : ", str




################### EXCEPTION ########################################

#### the assert statement
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)

### exception sytax
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()


# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz");
