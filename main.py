import create_db
from login_handler import login
from modify_db import *
from read_db import *


def main():
    """Main entry point to the LibraryManagement software"""

    if not os.path.exists("db/library.db"):
        print("Database not found. Creating the database...")
        create_db.main()
        print("Database created successfully!")

    display_welcome()

    while True:
        result, record = login()
        if result:
            break

    options = get_main_menu_options(record[3])
    menu(options, record)


def display_welcome():
    """Greets the user."""

    print("\nWelcome to the LibraryManagement software!")
    print("To use the software you have to login first. Please do so below.\n\n")


def menu(options, record):
    """Main menu of the software. Options are based on user roles."""

    active_user_id = record[0]
    role = record[3]

    while True:
        print()
        for option in options:
            print(option)

        user_input = input("\nEnter your choice: ")

        if user_input == "1":
            rent_book(active_user_id)
        elif user_input == "2":
            return_book(active_user_id)
        elif user_input == "3" and role != "Reader":
            add_book()
        elif user_input == "4" and role != "Reader":
            remove_book()
        elif user_input == "5" and role == "Admin":
            add_user()
        elif user_input == "6" and role == "Admin":
            remove_user(active_user_id)
        elif user_input == "7" and role == "Admin":
            reset_db()
        elif user_input == "9":
            exit()
        else:
            print("Invalid input! Try again")


def get_main_menu_options(role):
    """Defines the options based on the user role."""

    options = [
        "1 - Rent a book",
        "2 - Return a book"
    ]

    if role == "Librarian" or role == "Admin":
        for opt in ["3 - Add a book", "4 - Remove a book"]:
            options.append(opt)

    if role == "Admin":
        for opt in ["5 - Add a user", "6 - Remove a user", "7 - Reset Database"]:
            options.append(opt)

    options.append("9 - Exit")

    return options


# Reader options
def rent_book(user_id):
    """ Lists all the books availabe to rent.
    Creates a record in the RENTS table based on the User_ID and Book_ID.
    Validates user inputs."""

    books = get_available_books()
    if not books:
        print("No books available to rent!")
        return

    book_ids = [ book[0] for book in books ]

    while True:
        print("\nBooks available to rent:\n")

        for book in books:
            print(f"{book[0]} - {book[1]}")

        try:
            book_input = int(input("\nEnter the ID of the book: "))
            if book_input in book_ids:
                crete_new_rent(user_id, book_input)
                break
            else:
                print("Invalid input! Try again")
        except ValueError:
            print("Invalid input! Try again")


def return_book(user_id):
    """Lists all the books available to return.
    Sets the return date of the specific rent record in the RENTS table to the current date.
    Validates user input."""

    user_books = get_user_books(user_id)
    if not user_books:
        print("No books available to return!")
        return

    book_ids = []

    while True:
        print("\nYour rented books:\n")

        for book in user_books:
            book_ids.append(book[0])
            print(f"{book[0]} - {book[1]}")

        try:
            book_input = int(input("\nEnter the number of the book: "))
            if book_input in book_ids:
                finish_rent(user_id, book_input)
                break
            else:
                print("Invalid input! Try again")
        except ValueError:
            print("Invalid input! Try again")


# Librarian options
def add_book():
    """Creates a record in the BOOKS table based on the user input. Validates the input."""

    while True:
        name = input("Name: ")
        author = input("Author: ")
        pages = input("Pages: ")
        release_year = input("Release Year: ")
        language = input("Language: ")

        if not name or not author:
            print("Invalid input (name and author are required)! Try again")
            continue

        if language and language not in ["magyar", "angol"]:
            print("Invalid language (either use \"magyar\" or \"angol\")! Try again")
            continue

        if pages:
            try:
                pages = int(pages)
            except ValueError:
                print("Invalid input (pages has to be a number)! Try again")
                continue

        if release_year:
            try:
                release_year = int(release_year)
            except ValueError:
                print("Invalid input (release year has to be a number)! Try again")
                continue

        break

    create_book(name, author, pages, release_year, language)


def remove_book():
    """Lists all the books in the library.
    Removes the record that matches the ID given by the user.
    Validates input."""

    books = get_all_books()
    book_ids = [book[0] for book in books]

    while True:
        for book in books:
            print(f"{book[0]} - {book[1]}")

        selected_id = input("\nID of book to remove: ")
        try:
            selected_id = int(selected_id)
            if selected_id in book_ids:
                delete_book_by_id(selected_id)
                break
            else:
                print("Invalid input! Try again")
        except ValueError:
            print("Invalid input! Try again")


# Admin options
def add_user():
    """Creates a new record in the USERS table based on the user input.
    Validates the inputs."""

    user_name = input("\nUsername: ")
    password = input("Password: ")
    role = input("Role: ")

    if not user_name or not password or not role or role not in ["Admin", "Reader", "Librarian"]:
        print("Invalid input(s)! Every field must be filled!")

    create_new_user(user_name, password, role)
    print(f"New user ({user_name}) created successfully!")


def remove_user(active_user_id):
    """Deletes a record in the USERS table that matches the given user id. Validates input."""

    users = get_users()
    user_ids = [user[0] for user in users]

    while True:
        for user in users:
            print(f"{user[0]} - {user[1]}")

        user_id = input("\nID of user to delete: ")

        try:
            user_id = int(user_id)
            if user_id not in user_ids:
                print("Invalid input! Try again")
                continue

            if user_id == active_user_id:
                print("Unable to delete the current user! You may use another admin account to delete this one.")
                continue

            delete_user(user_id)
            break

        except ValueError:
            print("Invalid input! Try again")


def reset_db():
    """Resets the database with the initial values."""

    print("This options resets the whole database to its initial state.")
    print("All of the changes would be lost, with no way to recover them!")
    decision = input("Would you like to proceed? (y/n): ")

    if decision == "y":
        create_db.main()
        print("Database reset successfully!")
    else:
        print("Aborting!")
        return


if __name__ == "__main__":
    main()
