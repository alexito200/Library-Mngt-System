def add_author(conn):
    author_name = input("\nEnter the author's name: ")
    biography = input(f"\nEnter a short biography for {author_name}: ")

    cursor = conn.cursor()

    try:
        query = "INSERT INTO authors (author_name, biography) VALUES (%s, %s)"
        cursor.execute(query, (author_name, biography))
        conn.commit()
        print(f'\nAuthor "{author_name}" added successfully!')
    except Exception as e:
        print(f"\nAn error occurred while adding the author: {e}")
    finally:
        cursor.close()
