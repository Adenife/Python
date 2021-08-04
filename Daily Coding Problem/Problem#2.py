# A program to create a new list from an old list where the new list is the sum of every other
# number except from the particular item

numbers = [1,3,5,2]

def new_creation(numbers):
    new_list = []

    for number in numbers:
        new_list.append(sum(numbers)-number)

    return new_list

from functools import reduce
from operator import mul

product = reduce(mul, numbers)
new_list = [product//i for i in numbers]
        
print(new_creation(numbers))
print(new_list)