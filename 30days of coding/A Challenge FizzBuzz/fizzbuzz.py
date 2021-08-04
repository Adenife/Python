# a simple program to play the fizzbuzz game

for usr_input in range(1, 16):
    if usr_input % 3 == 0 and usr_input % 5 == 0:
        print("FizzBuzz")
    elif usr_input % 3 == 0:
        print("Buzz")
    elif usr_input % 5 == 0:
        print("Fizz")
    else:
        print(usr_input)