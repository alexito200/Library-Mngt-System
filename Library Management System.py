# Initialize dictionaries outside functions to ensure global access
books = {}
users = {}
authors = {}

class Book:
    def __init__(self, title, author, genre, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability

from add_book_module import add_book, books
from borrow_return_module import borrow_book, return_book
from search_book_module import search_book
from display_books_module import display_books

def book_operations():
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
                add_book(books) 

            elif choice == "2":
                borrowed_book_title = input('\nWhat book would you like to check out?: ')
                user_name = input('\nWhat is your name?: ')
                borrow_book(borrowed_book_title, user_name, books)

            elif choice == "3":
                returned_book_title = input("\nWhat book would you like to return?: ")
                return_book(returned_book_title, books)

            elif choice == "4":
                search_book(books)

            elif choice == "5":
                display_books(books)

            elif choice == "6":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nBook operations complete. You can choose another option.")

class User:
    def __init__(self, name, library_id, borrowed_books):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = borrowed_books

    def name(self):
        return self.__name

    def name(self, user_name):
        if not user_name:
            raise ValueError("\nUser name cannot be empty.")
        self.__name = user_name

    def library_id(self):
        return self.__library_id

    def library_id(self, id):
        if not id:
            raise ValueError("\nID cannot be empty.")
        self.__library_id = id

from add_user_module import add_user, users
from view_user_module import view_user
from display_users_module import display_users

def user_operations():
    while True:
        print("\nUser Operations Menu")
        print("\n1. Add a new user")
        print("\n2. View user details")
        print("\n3. Display all users")
        print("\n4. Back to main menu")
        
        choice = input("Select an option: ")

        try:
            if choice == "1":
                add_user()

            elif choice == "2":
                view_user()

            elif choice == "3":
                display_users(users)

            elif choice == "4":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nUser operations complete. You can choose another option.")

class Author:
    def __init__(self, author_name, biography):
        self.author_name = author_name
        self.biography = biography

from add_author_module import add_author, authors
from view_author_module import view_author
from display_authors_module import display_authors

def author_operations():
    while True:
        print("\nAuthor Operations Menu")
        print("\n1. Add a new author")
        print("\n2. View author")
        print("\n3. Display all authors")
        print("\n4. Back to main menu")
        
        choice = input("Select an option: ")

        try:
            if choice == "1":
                add_author()

            elif choice == "2":
                view_author(authors)

            elif choice == "3":
                display_authors(authors)

            elif choice == "4":
                break
            
            else:
                print("\nInvalid choice, please select again.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
        finally:
            print("\nAuthor operations complete. You can choose another option.")

while True:
    print('\nWelcome to the Library Management System!')
    print('\nMenu:')
    print('\n1. Book Operations')
    print('\n2. User Operations')
    print('\n3. Author Operations')
    print('\n4. Quit')

    choice = input("\nSelect an option: ")

    try:
        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice, please select again.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        print("\nMain menu operations complete.")
