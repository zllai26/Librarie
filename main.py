'''
Code is made by zllai26
Licensed with GNU GPL 3.0
This is Librarie
Run the shell scripts first before using this
'''

import json

def add():
    book = input("What book do you want to add? ")
    book_id = input("Give ID: ")
    
    try:
        with open("books.json", "r") as f:
            book_list = json.load(f)
    except FileNotFoundError:
        book_list = []

    new_book = {"name": book, "id": book_id, "borrow": False}
    book_list.append(new_book)

    with open("books.json", "w") as f:
        json.dump(book_list, f, indent=4)
    print(f"Successfully added '{book}'!")

def borrow(): 
    borrow_id = input("Enter the ID to borrow: ")
    try:
        with open("books.json", "r") as f:
            book_list = json.load(f)
    except FileNotFoundError:
        print("No books stored in your Library Database yet. Use function 1 to add a book.")
        return

    book_found = False

    for book in book_list:
        if book.get("id") == borrow_id:
            book_found = True
            if book.get("borrow") == True:
                print("Book has already been borrowed.")
            else:
                book["borrow"] = True
                print("Borrowing book success!")
            break

    if not book_found:
        print("Your book ID doesn't match our database.")
        return

    with open("books.json", "w") as f:
        json.dump(book_list, f, indent=4)

def list_books():
    try:
        with open("books.json", "r") as f:
            book_list = json.load(f)
    except FileNotFoundError:
        print("No books stored in your Library Database yet. Use function 1 to add a book.")
        return

    if not book_list:
        print("Your database is empty.")
        return

    for book in book_list:
        print(f"Name: {book.get('name')}, ID: {book.get('id')}, Borrowed: {book.get('borrow')}")

while True:
    print("\nWelcome to Librarie")
    print("You can (1) add a book, (2) borrow a book, (3) list down books, (4) exit")
    try:
        user = int(input("Give me your choice from 1 to 4: "))
        match user:
            case 1:
                add()
            case 2:
                borrow()
            case 3:
                list_books()
            case 4:
                print("Exiting... Goodbye!")
                break
            case _:
                print("This user input doesn't exist. Try again.")

    except ValueError:
        print("This user input doesn't exist. Try again.")
