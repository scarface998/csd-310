""" 
    Title: dawson-whatabook_delivery.py
    Author: Jake Dawson
    Date: March 6 2022
    Description: This is the application that allows customers of WhatABook 
    to browse in-store book listings, add books to their wishlist, register for 
    accounts, and view store hours and locations. 
"""

# imports for the program
import sys
import mysql.connector
from mysql.connector import errorcode

# connection information for the database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
# shows the user menu when called
def show_menu():
    print("\n-- Main Menu --")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4) Exit Program")

    # this try block catches user input errors
    try:
        choice = int(input("Type in a number to choose a menu option: "))
        return choice

    except ValueError:
        print("\n An invalid entry occurred, closing program...")
        sys.exit(0)

# this function is called when the user wants to see the list of books
def show_books(_cursor):

    # book information from the user
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # sets the results above equal to the books information
    books = cursor.fetchall()

    print("\n-- DISPLAYING BOOK LISTING --")

    # iterates through all the received data in the books variable
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))

# this function is called when the user wants to show store information.
def show_locations(_cursor):

    # pulls store_id and the location from the store table for all stores
    _cursor.execute("SELECT store_id, locale from store")

    # sets the locations variable equal to the data from the above query
    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    # iterates through the locations data to display all the store entries
    for location in locations:
        print("Locale: {}\n".format(location[1]))

# this function is called get the user's user_id and validate it to confirm if it is valid or not, and then returns the user_id if it is valid. 
# An error message is displayed and the program is ended if the user_id is not valid.
def validate_user():

    # checks to see if the entered value is correct
    try:
        user_id = int(input("\nPlease enter your user ID: "))

        if user_id < 0 or user_id > 3:
            print("\nInvalid user ID, program terminated...\n")
            sys.exit(0)

        return user_id
    # if the entry is not valid this ends the program
    except ValueError:
        print("\nInvalid entry, program terminated...\n")
        sys.exit(0)

# this function shows the menu for a user with a correct user_id
def show_account_menu():
    
    # checks to see if the menu option chosen is correct or not 
    try:
        print("\n--Customer Menu --")
        print("\n1. Wishlist\n2. Add Book\n3. Main Menu")

        account_menu_option_chosen = int(input("Type in a number to choose a menu option: "))

        return account_menu_option_chosen

    # if the menu option chosen wasn't correct, this will run
    except ValueError:
        print("\nInvalid menu option, program terminated...\n")
        sys.exit(0)

# this function can be called to view all the books in a user's wishlist.
def show_wishlist(_cursor, _user_id):

    #this cursor collects information from across multiple tables then uses two inner joins to display the matching information collected.
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    # this sets the variable wishlist equal to the information collected from the cursor.
    wishlist = _cursor.fetchall()

    print("\n --DISPLAYING WISHLIST ITEMS --")

    # this iterates through all the books in the wishlist to display their information.
    for book in wishlist:
        print("\nBook Name: {}\nAuthor: {}\n".format(book[4], book[5]))

# this function when called displays all the books that the whatabook company has that aren't already in the user's wishlist.
def show_books_to_add(_cursor,_user_id):

    # this query selects information from the book table that is not already in the wishlist table.
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    # this sets the cursor to hold the values from the query variable.
    _cursor.execute(query)

    # this sets the books_to_add variable equal to all the information being currently held by the cursor.
    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    # this iterates through all the books that were being held in the books_to_add variable, presenting the available books that can be added to the user's wishlist.
    for book in books_to_add:
        print("\nBook ID: {}\nBook Name: {}\n".format(book[0], book[1]))

# this function can be called when the user wishes to add new books to their wishlist.
def add_book_to_wishlist(_cursor,_user_id,_book_id):

    # this function inserts the book information into the wishlist table based on the user's selection(s)
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# tries to connect to the database using the config information above.
try:
    db = mysql.connector.connect(**config)

    cursor = db.curson()

    print("\nWelcome to the WhatABook Application!")

    # this calls the show_menu() method and sets the user_selection equal to the result returned from this.
    user_selection = show_menu()

    # this while statement allows the user to keep choosing different menu options as long as the option is not 4 (to exit the program).
    while user_selection != 4:

        # this if statement allows the user to view all the books that the WhatABook company sells.
        if user_selection == 1:
            show_books(cursor)
        
        # this if statement allows the user to view the different locations for the WhatABook company.
        if user_selection == 2:
            show_locations(cursor)
        
        # this if statement allows the user to verify their user_id then view the account_menu as long as the user_id was valid.
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # this while statement allows the user to stay inside the customer menu as long as the user doesn't enter option 3 to return to main menu.
            while account_option != 3:

                # this if statement is what allows the user to view their wishlist by calling the show_wishlist() method.
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                
                # this if statement is what allows the user to add books to their wishlist by calling the show_books_to_add() and add_book_to_wishlist() methods.
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("\nEnter the book ID of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # this commits the changes above to the database.
                    db.commit()

                    print("\nBook ID: {} was added to your wishlist!".format(book_id))

                # this ensures that if the customer is entering negative values or values over 3 that it will keep prompting them to enter the correct value until they do.
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                account_option = show_account_menu()

        # this ensures that if the user enters negative values or values over 4 that it will keep prompting them to enter the correct value until they do.
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please try again...")

        # this calls the show_menu() method after the customer menu has been left.
        user_selection = show_menu()
    print("\n\nProgram terminated...")

# if the ER_ACCESS_DENIED_ERROR or ER_BAD_DB_ERROR errors are presented
# this prints the appropriate error message based on the error. 
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
# this ensures the connection to the database closes correctly 
# and does not cause any issues from not being closed securely.
finally:
    db.close()