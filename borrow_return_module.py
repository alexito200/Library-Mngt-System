books = {}

def borrow_book(book_title, user_name, books):
    if book_title in books:
        if books[book_title]['status'] == 'available':
            books[book_title]['status'] = 'borrowed'
            books[book_title]['borrowed_by'] = user_name
            print(f'\n{user_name} has successfully borrowed "{book_title}".')
        else:
            print(f'\nSorry, "{book_title}" is already borrowed by {books[book_title]["borrowed_by"]}.')
    else:
        print(f'\nSorry, "{book_title}" is not available in the library.')




def return_book(book_title, books):
    if book_title in books:
        if books[book_title]['status'] == 'borrowed':
            books[book_title]['status'] = 'available'
            books[book_title]['borrowed_by'] = None
            print(f'The book "{book_title}" has been successfully returned.')
        else:
            print(f'The book "{book_title}" is not currently borrowed.')
    else:
        print(f'Sorry, "{book_title}" is not in the library catalog.')

