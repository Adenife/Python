# Write a program that removes all the occurrences of a specified string from a text file. 
# Your program should prompt the user to enter a filename and the string to be removed.

filename = input('Enter file name: ')


with open(filename, 'r') as f:
    for line in f:
        formatted = line.replace("e", "")
        print(formatted)