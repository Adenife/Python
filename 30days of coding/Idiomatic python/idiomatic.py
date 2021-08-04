# Write a function that prompts the user for their name and then greets them. If after processing 
# the string you're left with an empty string, the function should replace the empty string with "World" in the output.

# name = input("Enter your name: \n").strip().title()
# if name:
#     print(f"Welcome {name}")
# else:
#     print("World")

def greeter():
	name = input("Please enter your name: ").strip().title()
	print(f"Hello, {name or 'World'}!")

greeter()


# Write a function to determine whether or not a string contains exclusively ASCII letters.
from string import ascii_letters

def is_ascii_letters(test_string):
	return all(character in ascii_letters for character in test_string)

print(is_ascii_letters("D"))



# Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). 
# Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.
import random

population = range(1, 101)
numbers = [random.sample(population, 15) for _ in range(3)]

for number_set in numbers:
	number_set.sort(reverse=True)
	del number_set[5:]

print(numbers)