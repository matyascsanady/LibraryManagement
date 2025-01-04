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

    user = login()

    options = get_main_menu_options(user[3])
    menu(options, user)


def display_welcome():
    """Greets the user."""

    print("\nWelcome to the LibraryManagement software!")
    print("To use the software you have to login first. Please do so below.\n\n")


def display_goodbye():
    """Says goodbye to the user."""

    print("\nThank you for using LibraryManagement software!")
    print("Hope you found all the books you wanted. Hope to see you soon.")


def menu(options, record):
    """Main menu of the software. Options are based on user roles."""

    active_user_id = record[0]
    role = record[3]

    while True:
        print()
        for option in options:
            print(option)

        user_input = input("\nEnter your choice: ")

        if user_input == "0":
            statistics(active_user_id, role)
        elif user_input == "1":
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
            display_goodbye()
            exit()
        else:
            print("Invalid input! Try again")


def get_main_menu_options(role):
    """Defines the options based on the user role."""

    options = [
        "0 - Statistics",
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


# Statistics
def statistics(user_id, role):
     """Statistics option."""

     options = get_statistics_options(role)

     while True:
         print()
         for option in options:
             print(option)

         user_input = input("\nEnter your choice: ")

         if user_input == "1":
             current_user_rented_books(user_id)
         elif user_input == "2":
             current_user_read_books(user_id)
         elif user_input == "3" and role != "Reader":
             number_of_books()
         elif user_input == "4" and role != "Reader":
             average_page_num()
         elif user_input == "5" and role != "Reader":
             max_page_num()
         elif user_input == "6" and role != "Reader":
             min_page_num()
         elif user_input == "7" and role != "Reader":
             most_active_reader()
         elif user_input == "8" and role != "Reader":
             most_books()
         elif user_input == "9" and role != "Reader":
             avg_book_num_per_user()
         elif user_input == "10" and role != "Reader":
             avg_book_qual()
         elif user_input == "11" and role != "Reader":
             list_user_rented_books()
         elif user_input == "12" and role != "Reader":
             books_released_in_year()
         elif user_input == "13" and role != "Reader":
             books_written_in_language()
         elif user_input == "99":
             return
         else:
             print("Invalid input! Try again")


def get_statistics_options(role):
    """Defines the options for the statistics menu based on the user role."""

    options = [
        "1 - My currently rented books",
        "2 - My read books"
    ]

    if role == "Librarian" or role == "Admin":
        for opt in ["3 - Number of books in library",
                    "4 - Average page number",
                    "5 - Max page number",
                    "6 - Min page number",
                    "7 - Most active reader",
                    "8 - Highest amount of the same books",
                    "9 - Average number of books currently rented per user",
                    "10 - Average book quality",
                    "11 - List every current rent by a user",
                    "12 - Books released in (given year)...",
                    "13 - Books written in (given language)..."]:
            options.append(opt)

    options.append("99 - Return")

    return options


def current_user_rented_books(user_id):
    """Shows the user the books they currently rent."""

    books = get_user_books(user_id)
    if not books:
        print("You don't rent any books!")
        return

    print("\nYour currently rented books:\n")
    for book in books:
        print(f"{book[0]} - {book[1]}")

    input("\nPress Enter to continue...")


def current_user_read_books(user_id):
    """Shows the user the books they have read (rented) before."""

    books = set(get_user_read_books(user_id))
    if not books:
        print("You have not read any books! Try renting some!")
        return

    print("\nYour read books:\n")
    for book in books:
        print(f"{book[0]} - {book[1]}")

    input("\nPress Enter to continue...")


def number_of_books():
    """Shows the user the number of books in the library."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")
        return

    num = len(books)

    print(f"\nThere are {num} books in the library.")
    input("\nPress Enter to continue...")


def average_page_num():
    """Shows the user the average page number of books in the library."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")
        return

    pages = 0
    for book in books:
        if book[3]:
            pages += int(book[3])

    print(f"\nThe average page number is {round(pages / len(books))}")
    input("\nPress Enter to continue...")


def max_page_num():
    """Shows the user the max page number of the books in the library."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")
        return

    pages = [int(book[3]) for book in books if book[3]]

    print(f"\nThe max page number is {max(pages)}")
    input("\nPress Enter to continue...")


def min_page_num():
    """Shows the user the min page number of the books in the library."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")
        return

    pages = [int(book[3]) for book in books if book[3]]

    print(f"\nThe max page number is {min(pages)}")
    input("\nPress Enter to continue...")


def most_active_reader():
    """Shows the user(s) with the highest number of books read."""

    result = {}

    users = get_users()
    user_ids = [user[0] for user in users]

    max_books_read = 0
    most_active_users = []

    for user_id in user_ids:
        num = len(get_user_read_books(user_id))
        result[user_id] = num

        if num > max_books_read:
            max_books_read = num
            most_active_users = [user_id]
        elif num == max_books_read:
            most_active_users.append(user_id)

    print("\nThe most active users are:")
    for user_id in most_active_users:
        print(f"{get_user_by_id(user_id)[1]}(ID: {user_id}) read {result[user_id]} books")

    input("\nPress Enter to continue...")


def most_books():
    """Shows the user the highest amount of book(s) in the library."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")
        return

    results = {}
    for book in books:
        if book[1] not in results.keys():
            results[book[1]] = 1
        else:
            results[book[1]] += 1

    max_copies = max(results.values())
    highest_amount_books = [book for book, count in results.items() if count == max_copies]

    print("\nHighest amount of a single book(s):")
    for book in highest_amount_books:
        print(f"\"{book}\" has {max_copies} copies in the library")

    input("\nPress Enter to continue...")


def avg_book_num_per_user():
    """Shows the user the average number of books rented per user in the library."""

    users = get_users()
    user_ids = [user[0] for user in users]

    books_read_by_users = 0
    for user_id in user_ids:
        books_read_by_users += len(get_user_books(user_id))


    print(f"\nThe average number of books rented per user is {round(books_read_by_users / len(user_ids), 2)}")
    input("\nPress Enter to continue...")


def avg_book_qual():
    """Show the user that average book quality in the library."""

    books = get_all_books()

    sum_quality = 0
    valid_book_num = 0
    for book in books:
        if book[6]:
            sum_quality += book[6]
            valid_book_num += 1

    print(f"\nThe average quality of the books in the library is {round(sum_quality / valid_book_num, 2)}")
    input("\nPress Enter to continue...")


def list_user_rented_books():
    """Shows the currently rented books of the given user."""

    users = get_users()
    user_ids = [user[0] for user in users]

    print()
    for user in users:
        print(f"{user[0]} - {user[1]}")

    while True:
        selected_id = input("\nPlease select a user ID: ")
        try:
            selected_id = int(selected_id)

            if selected_id not in user_ids:
                print("Invalid selection. Try again!")
                continue

            user_rents = get_user_books(selected_id)

            print(f"\nBooks rented by \"{get_user_by_id(selected_id)[1]}\" are:")
            for book in user_rents:
                print(f"{book[0]} - {book[1]}")

            input("\nPress Enter to continue...")
            break

        except ValueError:
            print("Invalid input! Try again!")


def books_released_in_year():
    """Lists the books released in the given year."""

    books = get_all_books()
    if not books:
        print("There are no books in the library.")

    while True:
        try:
            year = int(input("\nPlease select a year: "))
            break
        except ValueError:
            print("Invalid input! Try again!")

    valid_books = [book for book in books if book[4] == year]
    if valid_books:
        print(f"\nBooks released in the year {year}:")
        for book in valid_books:
            print(f"{book[0]} - {book[1]}")
    else:
        print(f"\nThere are no books in the library. That were released in {year}")

    input("\nPress Enter to continue...")


def books_written_in_language():
    """Lists the books that were written in the given language."""

    books = get_all_books()

    results = {
        "magyar": [],
        "angol": []
    }

    for book in books:
        if book[5]:
            results[book[5]].append(book)

    while True:
        selected_lang = input("\nPlease select a language (magyar/angol): ")

        if not selected_lang in ["magyar", "angol"]:
            print("Invalid selection. Try again!")
            continue

        else:
            result = results[selected_lang]
            if result:
                print(f"\nBooks written in the language \"{selected_lang}\":")
                for book in result:
                    print(f"{book[0]} - {book[1]}")

            else:
                print(f"\nThere are no books in the library. That were written in the language \"{selected_lang}\"")

            break

    input("\nPress Enter to continue...")


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
        quality = input("Quality: ")

        if not name or not author or not quality:
            print("Invalid input (name, author and quality are required)! Try again")
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

        if language and language not in ["magyar", "angol"]:
            print("Invalid language (either use \"magyar\" or \"angol\")! Try again")
            continue

        if quality not in ["1", "2", "3", "4", "5"]:
            print("Invalid input (quality has to an integer between 1 and 5! Try again)")
            continue

        break

    create_book(name, author, pages, release_year, language, quality)


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
