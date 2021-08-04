items = ['banana', 'mango', 'cashew', 'mango', 'pineapple', 'apple', 'banana', 'banana',
        'mango', 'cashew', 'apple', 'banana', 'mango', 'mango', 'pineapple']

counter = dict()

for key in items:
    if (key in counter.keys()):
        counter[key] += 1
    else:
        counter[key] = 1


print(counter)