# Check if a key exist in a dictionary, if it does increase the value by one if it does not create a new key and give a value of 1


def incre(dct, key):
    if key not in dct.keys():
        dct[key] = 1
        return dct

    else:
        dct[key]=dct.get(key,0)+1
        return dct

my_dict = {
    "name": 4,
    "age": 3,
    1: 2
}

print(incre(my_dict, 'me'))