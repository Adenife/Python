# a program to show how functions work in python

# a simple calculator using functions
def add(x, y):
    ans = x + y
    print(f"{x} + {y} = {ans}")

def sub(x, y):
    ans = x - y
    print(f"{x} - {y} = {ans}")

def div(x, y):
    if y == 0:
        print(f"{y} cannot be a denominator")
    else:
        ans = x / y
        print(f"{x} / {y} = {ans}")

def mult(x, y):
    ans = x * y
    print(f"{x} * {y} = {ans}")

# take in input from user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

add(num1, num2)
sub(num1, num2)
div(num1, num2)
mult(num1, num2)


# function to print a dictionary
def print_show_info(dict_value):
        print(f"{dict_value['title']} ({dict_value['initial_release']}) - {dict_value['seasons']}")

tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }

print_show_info(tv_show)


def print_show_info(dict_value):
    for stuffs in dict_value:
        print(f"{stuffs['title']} ({stuffs['initial_release']}) - {stuffs['seasons']}")
        
series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

print_show_info(series)


# check if a word is a palindrome
usr_word = input("Enter a word or a sentence to check if it is a palindrome: \n>").lower()

# def check_palindrome(word):
#     reversed_word = list(word)
#     reversed_word.reverse()

#     if "".join(reversed_word) == word:
#         print(f"{word} is a palindrome")
#     else:
#         print(f"{word} is not a palindrome")

def check_palindrome(test_string):
	if test_string.lower() == test_string[::-1].lower():
		print(f"{test_string} is a palindrome.")
	else:
		print(f"{test_string} is not a palindrome.")

check_palindrome(usr_word)



# check if a sentence is a palindrome
import re

def check_palindrome(test_string):
	letters_only = re.sub("[^a-z]+", "", test_string.casefold())

	if letters_only == letters_only[::-1]:
		print(f"'{test_string}' is a palindrome.")
	else:
		print(f"'{test_string}' is not a palindrome.")

check_palindrome(usr_word)




# finding the longest words in a sentence
base_string = input("Enter a word or a sentence to check if it is a palindrome: \n>")
word_list = base_string.split(" ")
processed_words = [re.sub("[^A-Za-z]+", "", word) for word in word_list]

max_word_length = len(max(processed_words, key=len))
longest_words = [word for word in processed_words if len(word) == max_word_length]

print(longest_words)