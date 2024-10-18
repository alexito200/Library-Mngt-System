def display_books(conn):
    cursor = conn.cursor()

    try:
        query = "SELECT title, genre, availability FROM books"
        cursor.execute(query)
        books = cursor.fetchall()

        print("\nList of Books:")
        for index, (title, genre, availability) in enumerate(books, start=1):
            print(f"\n{index}. Title: '{title}', Genre: {genre}, Status: {'Available' if availability else 'Not Available'}")

    except Exception as e:
        print(f"An error occurred while retrieving the books: {e}")
    finally:
        cursor.close()