print("##################")
print("  MYPY PHONE BOOK ")
print("##################")


print("1 : Add New Entry \n2 : Delete Entry \n3 : Update Entry \n4 : Lookup Number \n5 : Quit")
operation = input("\nEnter Operation > ")


phone_book = {}

while True:
    if int(operation) == 1:
        name = input("Enter Contact Name: ")
        number = input("Ënter Contact Phone Number: ")

        phone_book[name.upper()] = number
        print(f"Successfully Added {name} to Contacts!")

    elif int(operation) == 2:
        user_to_delete = input("Enter Name of Contact to Delete: ")

        if user_to_delete.upper() in phone_book.keys():
            del phone_book[user_to_delete.upper()]
            print(f"Successfully Deleted {user_to_delete.upper()} from Contacts!")
        else:
            print("User not Found!!")

    elif int(operation) == 3:
        user_to_update = input("Enter Name of Contact to Update: ")
        new_contact_number = input("Enter Contact New Number: ")

        if user_to_update.upper() in phone_book.keys():
            phone_book[user_to_update.upper()] = new_contact_number
            print(f"Successfully Updated {user_to_update.upper()} in Contacts!")
        else:
            print("User not Found!!")

    elif int(operation) == 4:
        user_to_lookup = input("Enter Name of Contact to Lookup: ")

        if user_to_lookup.upper() in phone_book.keys():
            user_details = phone_book[user_to_lookup.upper()]
            print(f"Name: {user_to_lookup.upper()} \nPhone Number: {user_details}")
        else:
            print("User not Found!!")

    elif int(operation) == 5:
        print("Thank You For Using MYPY PHONE BOOK")
        break

    else:
        print("Wrong Input!!!")
   
    print("1 : Add New Entry \n2 : Delete Entry \n3 : Update Entry \n4 : Lookup Number \n5 : Quit")
    operation = input("\nEnter Operation > ")