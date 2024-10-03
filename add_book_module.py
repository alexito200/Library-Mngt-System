
books = {}

def add_book(books):
    """Function to add a book to the library."""
    book_title = input('\nTell me the title of the book: ')
    book_author = input(f'\nWho is the author of {book_title}?: ')
    book_genre = input(f'\nWhat is the genre of {book_title}?: ')

    # Add the book to the provided dictionary
    books[book_title] = {
        "author": book_author,
        "genre": book_genre,
        "status": 'available'
    }
    print(f'\nBook "{book_title}" added successfully!')

