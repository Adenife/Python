# a program to show how to import and use libraries in python

from fractions import Fraction
print(Fraction(2.25))


# find the sum of floating numbers (it is preferable to use the fsum module as opposed to the sum)
from math import fsum

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))


#  using the randint module
import random as ran
print(ran.randint(2,5))


# improve on the guess game earlier created in the series
usr_input = input("Enter q to quit program \nEnter a guess number: \n")

while usr_input != 'q':
    guess_num = ran.randint(0,100)
    
    if int(usr_input) > guess_num:
        print("Number is greater!!!")
    elif int(usr_input) < guess_num:
        print("Number is lesser!")
    else:
        print("Correct number")
        
    usr_input = input("Enter q to quit program \nEnter a guess number: \n")