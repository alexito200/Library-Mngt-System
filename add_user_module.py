def add_user(conn):
    user_name = input("\nEnter the user's name: ")
    library_id = input("\nEnter the user's library ID: ")

    cursor = conn.cursor()

    try:
        query = "INSERT INTO users (user_name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (user_name, library_id))
        conn.commit()
        print(f'\nUser "{user_name}" added successfully!')
    except Exception as e:
        print(f"\nAn error occurred while adding the user: {e}")
    finally:
        cursor.close()