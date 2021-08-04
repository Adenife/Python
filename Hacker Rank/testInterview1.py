# get the numbers between the highest and lowest that is divisible by 3 and return the sum

def sln(lst):
    low = min(lst)
    high = max(lst)

    new_list = []

    sl = list(sorted(lst))

    for i in sl:
        if i >= low and i<= high and i%3==0:
            new_list.append(i)

    return sum(new_list)


print(sln([1,2,3,4,5,6,9,10]))