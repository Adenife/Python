#Bubble sort
def bubble_sort(elements):
    n = len(elements)

    for i in range(n):
        #a flag that allows the loop to terminates early if there is nothing more to sort
        already_sorted = True

        #look at each element one by one and compare then swap where necessary
        for j in range(n - i - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

                #since we had to perform a swap, we set the flag to show we still have elements to check
                already_sorted = False

        if already_sorted:
            break

    return elements


#insertion sort
def insertion_sort(elements):
    #loop from the second element in the array to the last element
    for i in range(1, len(elements)):
        # the element we want to position in the correct place
        key_item = elements[i]
        
        #initialise the variable that will be used to find the correct position of the element referenced by key_item
        j = i - 1

        # run through the lis of items(in the left portion of the array) and find the correct position of the element reference by key_item
        # do this only if key_item is smaller than its adjacent values
        while j >= 0 and elements[j] > key_item:
            # shift the value one position to the left and reposition j to point to the next element (from right to left)
            elements[j+1] = elements[j]
            j -= 1

        # when you finish shifting the elements, you can position key_item in its correct location
        elements[j+1] = key_item

    return elements 


num = [2,6,5,4,7,6,8,5,3,7,10]
print(bubble_sort(num))
print(insertion_sort(num))