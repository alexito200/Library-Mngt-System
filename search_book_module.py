def search_book(conn):
    book_title = input("\nEnter the title of the book you're looking for: ")
    cursor = conn.cursor()

    try:
        query = "SELECT title FROM books WHERE title = %s"
        cursor.execute(query, (book_title,))
        book_info = cursor.fetchone()

        if book_info:
            print(f'\nYes, "{book_title}" is available.')
        else:
            print(f'\nSorry, "{book_title}" is not available.')

    except Exception as e:
        print(f"An error occurred while searching for the book: {e}")
    finally:
        cursor.close()