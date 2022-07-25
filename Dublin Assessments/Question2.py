print("##############################")
print("  WELCOME TO THE DBS CONSOLE  ")
print("##############################")


user_name = input(r"Please enter your username: ")


splitted_text = user_name.split("\\")
print(f"Domain: {splitted_text[0]}")
print(f"Usrname: {splitted_text[1]}")