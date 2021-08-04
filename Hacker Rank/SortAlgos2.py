# Quicksort

from random import randint

def quick_sort(elements):
    if len(elements) < 2:
        return elements

    low, same, high = [], [], []

    #select pivot element randomly
    pivot = elements[randint(0, len(elements) - 1)]

    for item in elements:
        # elements smaller than the pivot goes to the low list, elements that are higher goes to high list, elements that are equal goes to the same list
        if item < pivot:
            low.append(item)
        if item > pivot:
            high.append(item)
        if item == pivot:
            same.append(item)

    # return the sorted low list with the same list and the sorted high list
    return quick_sort(low) + same + quick_sort(high)

num = [2,6,5,4,7,6,8,5,3,7,10]
print(quick_sort(num))


# Timsort, hybrid sort (not complete. It implements the use of both inserion and merge sorts)

# def insertion_sort(elements, left=0, right=None):
#     if right is None:
#         right = len(elements) - 1

#     #loop from the element indicated by left until element indicated by right
#     for i in range(left+1, right+1):
#         # the element we want to position in the correct place
#         key_item = elements[i]
        
#         #initialise the variable that will be used to find the correct position of the element referenced by key_item
#         j = j - 1

#         # run through the lis of items(in the left portion of the array) and find the correct position of the element reference by key_item
#         # do this only if key_item is smaller than its adjacent values
#         while j >= left and elements[j] > key_item:
#             # shift the value one position to the left and reposition j to point to the next element (from right to left)
#             elements[j+1] = elements[j]
#             j -= 1

#         # when you finish shifting the elements, you can position key_item in its correct location
#         elements[j+1] = key_item

#     return elements

# def tim_sort(element):
#     min_run = 32
#     n = len(elements)

#     # start by slcing and sorting small portions of the input array. The size of these slices is defined by your min_run size
#     for i in range(0, n, min_run):
#         insertion_sort(array, i, min((i + min_run - 1), n - 1 ))

#     #  