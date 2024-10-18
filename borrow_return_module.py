import random

def borrow_book(user_name, book_title, borrow_date, conn):
    cursor = conn.cursor()

    try:
        # Step 1: Check if the user exists
        cursor.execute("SELECT id FROM users WHERE name = %s", (user_name,))
        user_result = cursor.fetchone()

        if user_result:
            # User exists, retrieve the user_id
            user_id = user_result[0]
        else:
            # User does not exist, insert the new user with a random 4-digit library_id
            library_id = str(random.randint(1000, 9999))
            
            query_insert_user = """
                INSERT INTO users (name, library_id)
                VALUES (%s, %s)
            """
            cursor.execute(query_insert_user, (user_name, library_id))
            conn.commit()

            # Retrieve the newly generated user_id
            user_id = cursor.lastrowid

            print(f"New user '{user_name}' has been added with library ID {library_id}.")

        # Step 2: Check if the book exists and is available
        cursor.execute("SELECT id FROM books WHERE title = %s", (book_title,))
        book_result = cursor.fetchone()

        if book_result:
            book_id = book_result[0]
        else:
            print(f"No book found with title '{book_title}'.")
            return

        # Step 3: Check if the book is already borrowed
        query_check_borrow = "SELECT COUNT(*) FROM borrowed_books WHERE book_id = %s AND return_date IS NULL"
        cursor.execute(query_check_borrow, (book_id,))
        book_borrowed = cursor.fetchone()[0]

        if book_borrowed == 0:
            # Step 4: Insert new record in borrowed_books table
            query_insert_borrow = """
                INSERT INTO borrowed_books (user_id, book_id, borrow_date) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query_insert_borrow, (user_id, book_id, borrow_date))
            conn.commit()

            print(f"{user_name} has successfully borrowed '{book_title}'.")
        else:
            print(f"'{book_title}' is already borrowed by someone else.")
    
    except Exception as e:
        print(f"An error occurred while borrowing the book: {e}")
    finally:
        cursor.close()

def return_book(book_title, conn):
    cursor = conn.cursor()     # Create a cursor object

    try:
        # SQL query to check if the book exists and is borrowed
        query_check = "SELECT status FROM books WHERE title = %s"
        cursor.execute(query_check, (book_title,))
        book_info = cursor.fetchone()

        if book_info:
            status = book_info[0]

            if status == 'borrowed':
                # SQL query to update the book status to 'available'
                query_update = "UPDATE books SET status = %s, borrowed_by = %s WHERE title = %s"
                cursor.execute(query_update, ('available', None, book_title))
                conn.commit()  # Commit the transaction
                print(f'The book "{book_title}" has been successfully returned.')
            else:
                print(f'The book "{book_title}" is not currently borrowed.')
        else:
            print(f'Sorry, "{book_title}" is not in the library catalog.')
    except Exception as e:
        print(f"\nAn error occurred while returning the book: {e}")
    finally:
        cursor.close()  # Close the cursor
