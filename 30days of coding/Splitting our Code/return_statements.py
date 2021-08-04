# return the result of an exponentiate function
def expo(x, y):
    return x ** y


# process a string to lowercase
def processed_string(word):
    return word.lower().strip()



# take in a tuble and returns as a dictionary
def my_dict(tuples):
    name, nationality, age = tuples
    return {
		"name": name,
		"nationality": nationality,
		"age": age
	}



# return true or false if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

