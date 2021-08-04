numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def square(n):
    return n ** 2

def even(n):
    return n % 2 == 0

def multiply(x, y):
    return x * y


#map applies the function to each element in the iliterable
squares = list(map(square, numbers))
print(squares)

#filter removes values in a list that does not meet a specified requirement
evens = list(filter(even, numbers))
print(evens)

from functools import reduce

#reduce applies th function to all elements and returns the sum 
product = reduce(multiply, numbers)
print(product)

#lambda functions are one line statements that allows generic operations to be performed
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x%2 == 0, numbers))
product = reduce(lambda x,y: x*y, numbers)  