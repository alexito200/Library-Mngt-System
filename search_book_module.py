def search_book(books):
    book_title = input("\nEnter the title of the book you're looking for: ")
    book_info = books.get(book_title, None)

    if book_info:
        print(f'\nYes, "{book_title}" is available.')
    else:
        print(f'\nSorry, "{book_title}" is not available.')


