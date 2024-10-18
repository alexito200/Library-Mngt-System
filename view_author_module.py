def view_author(conn):
    author_name = input("\nEnter the author's name you want to search for: ")

    cursor = conn.cursor()

    try:
        query = "SELECT biography FROM authors WHERE author_name = %s"
        cursor.execute(query, (author_name,))
        author_info = cursor.fetchone()

        if author_info:
            print(f"\nAuthor Details:\nName: {author_name}\nBiography: {author_info[0]}")
        else:
            print(f'\nNo author found with the name: {author_name}')
    except Exception as e:
        print(f"\nAn error occurred while viewing the author: {e}")
    finally:
        conn.close()