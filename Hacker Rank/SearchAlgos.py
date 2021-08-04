#Random search algorithm
import random

def search_it(elements, number):
    check = random.choice(elements)
    # return check
    if check == number:
        return check


#Linear search
def find_it(elements, number):
    for index, element in enumerate(elements):
        if element == number:
            return index


#Binary search
def do_binary_search(elements, number, left, right):
    if left <= right:
        middle = left + (right - 1) // 2
        if elements[middle] == number:
            return middle
        elif elements[middle] < number:
            return do_binary_search(elements, number, middle + 1, right)
        else:
            return do_binary_search(elements, number, left, middle-1)

    else:
        return -1




num = [2,6,5,4,7,6,8,5,3,7,10]

print(do_binary_search(num, 6, 0, len(num)-1))
print(find_it(num, 6))