* Updated: 2024-10-18 *
* Here are the updates to this program:
    - classes removed
    - mysql database (named test_db) integrated into the program to store books, authors, users, and borrowed books
    - all of the modules being imported into the main program have been changed to sql queries
    - there is now a new module named 'sql_connection' that connects the main program to the database

Library Management System by Alex Alarcon

TOC:
- Books
  - Add a new book
  - Borrowing a book
  - Returning a book
  - Searching for a book
  - Displaying all books
  - Back to main menu
- Users
  - Adding a new user
  - Viewing user details
  - Displaying all users
  - Back to main menu
- Authors
  - Adding a new author
  - Viewing author
  - Displaying all authors
  - Back to main menu
 

Books:

To add a new book, the user must enter '1' as the selection from the 'Books' menu. The program will then ask the user to enter the title, the author, and the genre of the book.
The program will print out a 'Book {book_title} added successfully.'

To borrow a book, the user must enter '2' as the selection from the 'Books' menu. The user will be asked to provide the title of the book being borrowed and their name. 
The program will search through the Books dictionary for a match, then print out '{user_name} has successfully borrowed "{book_title}".' The program will change the status of the book
from 'Available' to 'Borrowed'. If the book is already borrowed, the program will print out 'Sorry, "{book_title}" is already borrowed by {books[book_title]["borrowed_by"]}.' 


To return a book, the user must enter '3' as the selection from the 'Books' menu. The user will be prompted to enter the title of the book which the program will use to run a match
search. If the book's status is 'Borrowed', then the program will change it to 'Available'. A message reading, 'The book "{book_title}" has been successfully returned.', will print out.


To search for a book, the user must enter '4' as the selection from the 'Books' menu. The user will be prompted to enter in the book's title. If the title matches that of a book in the
Books dictionary, then a message reading, 'Yes, "{book_title}" is available.' will print out. If the title of the book is not found, the message will read
'Sorry, "{book_title}" is not available.'. 


To display all books, the user must enter '5' as the selection from the 'Books' menu. The program will print out an enumerated list of all the books in the Books dictionary. The list
will include the title, author, genre, and availability status.


To go back to the main menu, the user must enter '6' as the selection from the 'Books' menu.

Users:

To add a new user, the user must enter '1' as the selection from the 'Users' menu. The user will be prompted to enter the user's name along with a library ID formatted with a single
capital letter followed by any four numbers. An empty list of Borrowed Books is initiated for each user. The program will vet the library ID entered to find a duplicate. If no
duplicate is found, the program continues to printing out the message 'User "{user_name}" added successfully!'.


To view user details, the user must enter '2' as the selection from the 'Users' menu. The user will be asked to enter the library ID of the user they would like to search up. If the
program finds that the library ID belongs to an existing user, it will print out that user's details for the user to view. User details that will be printed out are the name and the
borrowed books, if any, of that specific user. If the program finds no user with that library ID, it will print out 'No user found with library ID: {library_id}'.

To display all users, the user must enter '3' as the selection from the 'Users' menu. The program will print out an enumerated list of all the users in the Users dictionary. The list
will include the user's library ID, name, and borrowed books.


To return to main menu, the user must enter '4' as the selection from the 'Users' menu.

Authors:

To add a new author, the user must enter '1' as the selection from the 'Author' menu. The user will be prompted to enter in the author's name and a short biography. The author will
be added to the authors' dictionary when the program prints out a message reading 'Author "{author_name}" added successfully!'.

To view an author, the user must enter '2' as the selection from the 'Author' menu. The user will be asked for the author that they are trying to search for. The program will search 
in the authors dictionary for a match. If a match is found, the program will print out the author's details that include name, and biography. If the program does not find an author 
with a matching name, it will print out 'No author found with the name: {author_name}'.


To display all authors, the user must enter '3' as the selection from the 'Author' menu. The program will print out an enumerated list of all the authors in the Authors dictionary.
The list will include the author's name, and biography.


To return to main menu, the user must enter '4' as the selection from the 'Authors' menu.
