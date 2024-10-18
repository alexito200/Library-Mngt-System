def display_authors(conn):
    cursor = conn.cursor()     # Create a cursor object

    try:
        # SQL query to retrieve all authors
        query = "SELECT id, author_name, biography FROM authors"
        cursor.execute(query)
        authors = cursor.fetchall()  # Fetch all records

        print("\nList of Authors:")
        for index, (id, author_name, biography) in enumerate(authors, start=1):
            print(f"\n{index}. ID: {id}, Author Name: {author_name}, Biography: {biography}")

    except Exception as e:
        print(f"An error occurred while retrieving the authors: {e}")
    finally:
        cursor.close()  # Close the cursor
