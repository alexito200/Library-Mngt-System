from mysql.connector import Error

def add_book(conn):
    cursor = conn.cursor()

    # Prompt user for book details
    title = input("Enter book title: ")
    # author_id = input("Enter author ID: ")
    genre = input("Enter book genre: ")
    availability = True  # By default, new books are available

    # SQL query to insert a new book
    try:
        query = '''INSERT INTO books (title, genre, availability) VALUES (%s, %s, %s)'''
        cursor.execute(query, (title, genre, availability))
        conn.commit()
        print(f"Book '{title}' added successfully!")

    except Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        cursor.close()