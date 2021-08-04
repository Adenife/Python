# A program to check if any 2 numbers in a list is equals to a given number

def check(numbers, value):
    for num in numbers:
        if value - num in numbers:
            return True
        return False

number = [9, 15, 3, 7]
k = 12

print(check(number, k))