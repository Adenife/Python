# Write a program that counts the number of characters, words and lines in a file; words are separated by a white space. 
# Your program should prompt the user to enter a filename, and then print the total number of characters, total number of 
# words and total number of lines in that file. Hint: the file is assumed to be stored in your current working directory. 

import os


def counter(filename):
    words = 0
    lines = 0
    characters = 0


    with open(filename, 'r') as f:
        for line in f:
            line = line.strip(os.linesep)

            word = line.split()

            lines = lines + 1
            words = words + len(word)
            characters = characters + sum(1 for c in line if c not in (os.linesep, ' '))

        print(f'Number of lines: {lines}')
        print(f'Number of words: {words}')
        print(f'Number of characters: {characters}')


filename = input('Enter file name: ')
counter(filename)