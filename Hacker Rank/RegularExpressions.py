# \d(numbers) \D(letters)
import re

#validating email
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()

if(re.search(pattern, user_input)):
    print(f'{user_input} is a Valid Email')
else:
    print(f'{user_input} is not a Valid Email')

pattern2 = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3"
user_input2 = input()

new_user_input = re.sub(pattern2, new_pattern, user_input2)
print(new_user_input)