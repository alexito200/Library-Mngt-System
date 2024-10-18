def add_user(conn):
    user_name = input("\nEnter the user's name: ")
    library_id = input("\nEnter the user's library ID: ")

    cursor = conn.cursor()     # Create a cursor object

    try:
        # SQL query to insert a new user
        query = "INSERT INTO users (user_name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (user_name, library_id))
        conn.commit()  # Commit the transaction
        print(f'\nUser "{user_name}" added successfully!')
    except Exception as e:
        print(f"\nAn error occurred while adding the user: {e}")
    finally:
        cursor.close()  # Close the cursor