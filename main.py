from login_handler import login
from modify_db import create_new_user


def main():

    while True:
        result, role = login()
        if result:
            break

    options = get_main_menu_options(role)
    menu(options, role)


def menu(options, role):

    while True:
        print()
        for option in options:
            print(option)

        user_input = input("\nEnter your choice: ")

        if user_input == "1":
            print("Rent a book")
        elif user_input == "2":
            print("Return a book")
        elif user_input == "3" and role != "Reader":
            print("Add a book")
        elif user_input == "4" and role != "Reader":
            print("Remove a book")
        elif user_input == "5" and role == "Admin":
            add_user()
        elif user_input == "6" and role == "Admin":
            print("Remove a user")
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


# Admin options
def add_user():
    user_name = input("\nUsername: ")
    password = input("Password: ")
    role = input("Role: ")

    if not user_name or not password or not role or role not in ["Admin", "Reader", "Librarian"]:
        print("Invalid input(s)! Every field must be filled!")

    create_new_user(user_name, password, role)
    print("New user created successfully!")


if __name__ == "__main__":
    main()
