# program to check if a credit card number is valid or invalid

card_number = input("Enter your credic card number: \n>")

# convert the card number to a list
card_number = list(card_number.strip())
# print(card_number)


# writing the luhn algorithm to check the validity of a card

# remove the last digit (use the pop function to store the digit somewhere)
checking_digit = card_number.pop(-1)
# print(card_number)

# reverse the remaining digits
card_number.reverse()
# print(card_number)

# take the digits in the even position and double them
new_card_number = []
for index, number in enumerate(card_number):
    # check to see if the number is at an even index
    if index % 2 == 0:
        # doube the number if it is at an even index
        double_it = int(number)*2
        # if after doubling, number is greater than 9, subtract 9 from it
        if double_it > 9:
            num = double_it - 9
            new_card_number.append(num)
        else:
            new_card_number.append(double_it)
    else:
        new_card_number.append(int(number))

# print(new_card_number)

# sum up all digits including the checking number
final_sum = sum(new_card_number) + int(checking_digit)
# print(final_sum)

# check to see if sum is divisible by 10, then it is valid
if final_sum % 10 == 0:
    print("The card number is valid!")
else:
    print("Invalid card number!!!")