# main_program.py
from sql_connection import connect_database
from add_book_module import add_book
from borrow_return_module import borrow_book, return_book
from search_book_module import search_book
from display_books_module import display_books
from add_user_module import add_user
from view_user_module import view_user
from display_users_module import display_users
from add_author_module import add_author
from view_author_module import view_author
from display_authors_module import display_authors

# Function Definitions
def book_operations(conn):
    while True:
        print("\nBook Operations")
        print("\n1. Add a new book")
        print("\n2. Borrow a book")
        print("\n3. Return a book")
        print("\n4. Search for a book")
        print("\n5. Display all books")
        print("\n6. Back to main menu")
        
        choice = input("\nSelect an option: ")

        try:
            if choice == "1":
                add_book(conn)  # Pass the connection to add_book

            elif choice == "2":
                book_title = input('\nWhat book would you like to check out?: ')
                user_name = input('\nWhat is your name?: ')
                borrow_date = input('\nEnter the borrow date (YYYY-MM-DD): ')
                borrow_book(conn, book_title, user_name, borrow_date)  # Pass the connection to borrow_book

            elif choice == "3":
                returned_book_title = input("\nWhat book would you like to return?: ")
                return_book(conn, returned_book_title)  # Pass the connection to return_book

            elif choice == "4":
                search_book(conn)  # Pass the connection to search_book

            elif choice == "5":
                display_books(conn)  # Pass the connection to display_books

            elif choice == "6":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nBook operations complete.")

def user_operations(conn):
    while True:
        print("\nUser Operations Menu")
        print("\n1. Add a new user")
        print("\n2. View user details")
        print("\n3. Display all users")
        print("\n4. Back to main menu")
        
        choice = input("\nSelect an option: ")

        try:
            if choice == "1":
                add_user(conn)  # Pass the connection to add_user

            elif choice == "2":
                view_user(conn)  # Pass the connection to view_user

            elif choice == "3":
                display_users(conn)  # Pass the connection to display_users

            elif choice == "4":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nUser operations complete.")

def author_operations(conn):
    while True:
        print("\nAuthor Operations Menu")
        print("\n1. Add a new author")
        print("\n2. View author")
        print("\n3. Display all authors")
        print("\n4. Back to main menu")
        
        choice = input("\nSelect an option: ")

        try:
            if choice == "1":
                add_author(conn)  # Pass the connection to add_author

            elif choice == "2":
                view_author(conn)  # Pass the connection to view_author

            elif choice == "3":
                display_authors(conn)  # Pass the connection to display_authors

            elif choice == "4":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nAuthor operations complete.")


def main():
    conn = connect_database()
    if conn is None:
        print("Failed to connect to the database. Exiting program.")
        return  # Exit if connection failed

    print('\nWelcome to the Library Management System!')
    
    while True:
        print('\nMenu:')
        print('\n1. Book Operations')
        print('\n2. User Operations')
        print('\n3. Author Operations')
        print('\n4. Quit')

        choice = input("\nSelect an option: ")

        try:
            if choice == "1":
                book_operations(conn)  # Pass the connection to book_operations
            elif choice == "2":
                user_operations(conn)  # Pass the connection to user_operations
            elif choice == "3":
                author_operations(conn)  # Pass the connection to author_operations
            elif choice == "4":
                print("\nExiting the program.")
                break
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nMain menu operations complete.")

    if conn.is_connected():
        conn.close()

    # Close the connection when done
    # conn.close()
    # print("Database connection closed.")

if __name__ == "__main__":
    main()
