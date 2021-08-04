# a program to check if a number is prime or not
number = int(input("Enter a nuber to check if it is prime or not: \n>"))
divisor = 2

while divisor < number:
    if number % divisor == 0:
        print(f"{number} is not a prime number")
    divisor += 1

else:
    print(f"{number} is a prime number")



# Program to create a guessing game
number = 100
usr_guess = input("Enter a number between 1 and 100: \n>")

while usr_guess != number:
	if usr_guess > number:
		print("Too high!")
	else:
		print("Too low!")

	usr_guess = int(input("Enter a number: "))

print("You guessed correctly!")



# program to print out every character in the word python without the o
word = 'python'

for py in word:
    if py == 'o':
        continue
    print(py)



# print prime numbers between 1 and 100
primes = []

for dividend in range(2, 101):
	for divisor in range(2, dividend):
		if dividend % divisor == 0:
			break
	else:
		primes.append(str(dividend))

print(", ".join(primes))