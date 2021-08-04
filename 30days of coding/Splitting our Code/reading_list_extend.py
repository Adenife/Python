# create a menu to display the different options available to a user
print("You are allowed to select the following actions:")
print("Select (a) to add a book to reading list. \nSelect (d) to display all books in your collection \nSelect (s) to search \nSelect (q) to quit")

option = input("\nEnter operation to perform: ").lower().strip()

# create functions for each operation

# add book to file
def add_book():
    book_title = input("Enter the title of the book: \n>")
    auth_name = input("Enter the name of the authur of the book: \n>")
    year_published = input("Enter the year the book was published \n>")

    with open("./Library.csv", 'a') as cursor:
        cursor.write(f"{book_title},{auth_name},{year_published}")
    print("Successfully Added to Library!!!")


# Display all the books in the list
def display_books():
    with open("./Library.csv", 'r') as cursor:
        the_books = cursor.readlines()

    headers = ["Title", "Name", "Year"]
    books = []
    for rows in the_books:
        book = rows.strip().split(",")
        bookks_final = dict(zip(headers, book))
        books.append(bookks_final)

    for book in books:
        title, name, year = book.values()
        print(f"{title} ({year}) - {name}")

    
# search for book in the file
def search_book():
    with open("./Library.csv", 'r') as cursor:
        the_books = cursor.readlines()

    headers = ["Title", "Name", "Year"]
    books = []
    for rows in the_books:
        book = rows.strip().split(",")
        bookks_final = dict(zip(headers, book))
        books.append(bookks_final)

    usr_input = input("Enter the title of book to search for: \n>").lower()
    for book in books:
        title, name, year = book.values()
        if usr_input in title.lower():
            print(f"{title} ({year}) - {name}")
        else:
            print(f"{usr_input} is not a book in the library")


# perform operation user selects
while option != 'q':
    if option == 'a':
        add_book()
    elif option == 'd':
        display_books()
    elif option == 's':
        search_book()
    else:
        print("Invalid selection!!!")
    
    print("\n\n")
    print("You are allowed to select the following actions:")
    print("Select (a) to add a book to reading list. \nSelect (d) to display all books in your collection \nSelect (s) to search \nSelect (q) to quit")
    option = input("\nEnter operation to perform: ").lower().strip()