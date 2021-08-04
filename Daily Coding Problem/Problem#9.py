def find_max(numbers):
    incl = 0
    excl = 0

    for i in numbers:
        new_excl = excl if excl>incl else incl

        incl = excl + i
        excl = new_excl

    return (excl if excl>incl else incl)


number = [2,4,6,2,5]
print(find_max(number))