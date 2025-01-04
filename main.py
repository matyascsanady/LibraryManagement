import os
import create_db
from login_handler import login
from modify_db import create_new_user, delete_user, crete_new_rent
from read_db import get_available_books


def main():

    if not os.path.exists("db/library.db"):
        print("Database not found. Creating the database...")
        create_db.main()
        print("Database created successfully!")

    while True:
        result, record = login()
        if result:
            break

    options = get_main_menu_options(record[3])
    menu(options, record)


def menu(options, record):

    role = record[3]

    while True:
        print()
        for option in options:
            print(option)

        user_input = input("\nEnter your choice: ")

        if user_input == "1":
            rent_book(record[0])
        elif user_input == "2":
            print("Return a book")
        elif user_input == "3" and role != "Reader":
            print("Add a book")
        elif user_input == "4" and role != "Reader":
            print("Remove a book")
        elif user_input == "5" and role == "Admin":
            add_user()
        elif user_input == "6" and role == "Admin":
            remove_user()
        elif user_input == "9":
            exit()
        else:
            print("Invalid input! Try again")


def get_main_menu_options(role):
    options = [
        "1 - Rent a book",
        "2 - Return a book"
    ]

    if role == "Librarian" or role == "Admin":
        for opt in ["3 - Add a book", "4 - Remove a book"]:
            options.append(opt)

    if role == "Admin":
        for opt in ["5 - Add a user", "6 - Remove a user"]:
            options.append(opt)

    options.append("9 - Exit")

    return options


# Reader options
def rent_book(user_id):

    books = get_available_books()
    book_ids = []

    while True:
        print()

        for book in books:
            book_ids.append(book[0])
            print(f"{book[0]} - {book[1]}")

        try:
            book_input = int(input("\nEnter the number of the book: "))
            if book_input in book_ids:
                crete_new_rent(user_id, book_input)
                break
            else:
                print("Invalid input! Try again")
        except ValueError:
            print("Invalid input! Try again")


# Admin options
def add_user():
    user_name = input("\nUsername: ")
    password = input("Password: ")
    role = input("Role: ")

    if not user_name or not password or not role or role not in ["Admin", "Reader", "Librarian"]:
        print("Invalid input(s)! Every field must be filled!")

    create_new_user(user_name, password, role)
    print(f"New user ({user_name}) created successfully!")


def remove_user():
    user_name = input("\nUsername: ")

    delete_user(user_name)

    print(f"User ({user_name}) deleted successfully!")


if __name__ == "__main__":
    main()
