def display_books(conn):
    cursor = conn.cursor()     # Create a cursor object

    try:
        # SQL query to retrieve all books
        query = "SELECT title, genre, availability FROM books"
        cursor.execute(query)
        books = cursor.fetchall()  # Fetch all records

        print("\nList of Books:")
        for index, (title, genre, availability) in enumerate(books, start=1):
            print(f"\n{index}. Title: '{title}', Genre: {genre}, Status: {'Available' if availability else 'Not Available'}")

    except Exception as e:
        print(f"An error occurred while retrieving the books: {e}")
    finally:
        cursor.close()  # Close the cursor