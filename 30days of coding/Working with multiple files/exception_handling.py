# program to show how to use exceptions in python
from math import fsum
try:
    grades = input("Enter all your grades seperated by a comma: \n")
    grades = [int(grade) for grade in grades.split(",")]
    print(grades)
except ValueError:
    print("Your grades should be integers")


try:
    with open("nife.txt", "r") as f:
        me = f.read()
        print(me)
except FileNotFoundError:
    print("File does not exist")