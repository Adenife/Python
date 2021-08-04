# Given a list, find the first mising positive integer that does not exist in the array

numbers = [3,4,-1,1]

from collections import defaultdict

def missing(numbers):
    d = defaultdict(int)
    for i in numbers:
        d[i] = 1

    j = 1
    while True:
        if d[j] == 0:
            return j

        j += 1

print(missing(numbers))