# Create a program that sums all of the numbers entered by the user while ignoring any lines entered by the user that are not valid numbers. 
# Your program should display the current sum after each number is entered. It should display an appropriate error message after any invalid input, 
# and then continue to sum any additional numbers entered by the user. Your program should exit when the user enters a blank line. Ensure that your 
# program works correctly for both integers and floating point numbers. Hint: This exercise requires you to use exception without using files.

sum = 0
count = 0

while True:
    prompt = input("Enter a number: ")

    if prompt == "":
        break

    try:
        sum += float(prompt)
    except ValueError:
        print("Bad Number!!!")
        continue

    print(sum)

print(f'The sum of all numbers entered is {sum}')