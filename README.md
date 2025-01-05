# LibraryManagement

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction
This project is the final assignment of a programming course.  
It is a console application with an SQLite database in the background, designed to handle tasks related to library management.  
Written in pure Python with no third-party dependencies.

## Features
- Login system
- Role-based access:
  - **Admin**: Add and remove users, reset the database to its initial state
  - **Librarian**: Add and remove books
  - **Reader**: Rent and return books
- Predefined statistics queries on the database

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/matyascsanady/LibraryManagement.git
   ```
2. Ensure that python 3.12.x is installed

## Usage
1. Run the main.py (this will create the DB with its initial values)
2. Login with your account. If you do not have one have one yet, you can use one of the followings (Username - Password - Role).
   - Admin - 123 - Admin
   - Librarian - 123 - Librarian
   - Reader - 123 - Reader
3. After login a menu will be displayed. Each option has a number from this point on you have to navigate with option numbers.á

## Configuration
No configuration is needed. The DB gets created by program with its initial values.

## Contributing
This project is opten to contributions, however not expected as it is the final product of a course.
### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License.
Feel free to use, modify, or distribute under the terms of the license.
