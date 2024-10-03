users = {}

def add_user():
    user_name = input("\nEnter the user's name: ")
    library_id = input("\nEnter the library ID for the user (e.g., 'A1234'): ")

    borrowed_books = []

    users[library_id] = {
        'name': user_name,
        'borrowed_books': borrowed_books
    }
    print(f'\nUser "{user_name}" added successfully!')
