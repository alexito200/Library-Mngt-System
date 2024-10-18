from mysql.connector import Error

def add_book(conn):
    cursor = conn.cursor()

    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    availability = True

    try:
        query = '''INSERT INTO books (title, genre, availability) VALUES (%s, %s, %s)'''
        cursor.execute(query, (title, genre, availability))
        conn.commit()
        print(f"Book '{title}' added successfully!")

    except Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        cursor.close()