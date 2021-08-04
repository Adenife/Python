# Write a program that writes 100 integers created randomly into a file. Integers are separated 
# by a space in the file. Read the data back from the file and display the sorted data. 
# Your program should prompt the user to enter a filename. 

from random import randint
import csv


num = int(input('Enter the amount of numbers to print: '))
lower = int(input('Enter the lower bound of random numbers to print: '))
upper = int(input('Enter the upper bound of random numbers to print: '))
filename = input('Enter file name: ')


numbers = []
for i in range(num):
    numbers.append(randint(lower, upper))


with open(filename, 'w') as f:
    for num in numbers:
        f.write('%i ' %num)


with open(filename, 'r') as f:
    nums = sorted(f.readlines())
    for num in nums:
        me = num.split(' ')

    me.pop()
    new = [int(i) for i in me]
    print(sorted(new))