# simple recurssion
def countdown(x):
    if x == 0:
        print('Done')
        return

    else:
        print(x, '...')
        countdown(x-1)

countdown(5)


# factorial
def factorial(x):
    if x == 0:
        return 1

    else:
        return x * factorial(x-1)

print(factorial(5))

# power
def power(num, pwr):
    if pwr == 0:
        return 1

    else:
        return num * power(num, pwr-1)

print(power(5,2))

# find maximum number

def find_max(elements):
    if len(elements) == 1:
        return elements[0]

    op1 = elements[0]
    op2 = find_max(elements[1:])

    if op1 > op2:
        return op1
    else:
        return op2

num = [2,6,5,4,7,6,8,5,3,7,10]
print(find_max(num))