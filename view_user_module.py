from sql_connection import connect_database

def view_user(conn):
    user_name = input("\nEnter the name of the user you want to search for: ")

    cursor = conn.cursor()  # Create a cursor object

    try:
        # SQL query to select user details by name
        query = "SELECT id, user_name, library_id FROM users WHERE user_name = %s"
        cursor.execute(query, (user_name,))
        user_info = cursor.fetchone()

        if user_info:
            user_id, user_name, library_id = user_info  # Unpack the result
            print(f"\nUser Details:\nID: {user_id}\nName: {user_name}\nLibrary ID: {library_id}")
        else:
            print(f'\nNo user found with name: {user_name}')
    except Exception as e:
        print(f"\nAn error occurred while retrieving user details: {e}")
    finally:
        cursor.close()  # Close the cursor
