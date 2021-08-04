# a program to tryiut the split and join methods in python

# take in user full name in a single line
full_name = input("Enter your full name:\n")

# split the name and input into different variables
split_name = full_name.split(" ")
# print(split_name)

# assign the names to different variable
first_name = split_name[0]
last_name = split_name[-1]

print(f"My first name is {first_name} and my last name is {last_name}")



# join the list [1,2,3,4,5] using the seperator |
numbers = [1,2,3,4,5]

# convert the numbers to string
stringed_numbers = []

for number in numbers:
    stringed_numbers.append(str(number))

print("|".join(stringed_numbers))



# extract the texts from the list without the quotations
quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]

#  use slicing to extract the texts
for quote in quotes:
    print(quote[1:-1])



# process a user text and give the length accounting for whitespaces
text = input("Enter preferred texts: \n>")

# character count
stripped_text = text.strip()
print(len(stripped_text))

# word_count
print(len(stripped_text.split()))