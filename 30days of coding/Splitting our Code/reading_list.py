# create a menu to display the different options available to a user
print("You are allowed to select the following actions:")
print("Select (a) to add a book to reading list. \nSelect (d) to display all books in your collection \nSelect (q) to quit")

book_list = []
option = input("\nEnter operation to perform: ").lower().strip()

# create functions for each operation

# add book to list
def add_book():
    book = {}
    book_title = input("Enter the title of the book: \n>")
    auth_name = input("Enter the name of the authur of the book: \n>")
    year_published = input("Enter the year the book was published \n>")
    
    book["Title"] = book_title
    book["Authors Name"] = auth_name
    book["Published Year"] = year_published

    book_list.append(book)
    print("Successfully Added to Library!!!")


# Display all the books in the list
def display_books(library):
    for books in library:
        # title, author, year = books.values()
        # print(f"{title}, by {author} ({year})")
        print(f"{books['Title']} ({books['Published Year']}) by {books['Authors Name']}")


# perform operation user selects
while option != 'q':
    if option == 'a':
        add_book()
    elif option == 'd':
        display_books(book_list)
    else:
        print("Invalid selection!!!")
    
    print("\n\n")
    print("You are allowed to select the following actions:")
    print("Select (a) to add a book to reading list. \nSelect (d) to display all books in your collection \nSelect (q) to quit")
    option = input("\nEnter operation to perform: ").lower().strip()