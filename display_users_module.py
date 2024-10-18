def display_users(conn):
    cursor = conn.cursor()     # Create a cursor object

    try:
        # SQL query to select all users
        query = "SELECT id, user_name, library_id FROM users"
        cursor.execute(query)
        users = cursor.fetchall()  # Fetch all results

        print("\nList of Users:")
        for index, (id, user_name, library_id) in enumerate(users, start=1):
            library_id_display = library_id if library_id else 'None'
            print(f"\n{index}. ID: {id}, Name: {user_name}, Library ID: {library_id}")
    except Exception as e:
        print(f"\nAn error occurred while displaying users: {e}")
    finally:
        cursor.close()  # Close the cursor