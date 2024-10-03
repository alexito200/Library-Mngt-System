users = {}

def view_user():
    library_id = input("\nEnter the library ID of the user you want to search for: ")
    if library_id in users:
        user_info = users[library_id]
        print(f"\nUser Details:\nName: {user_info['name']}\nBorrowed Books: {', '.join(user_info['borrowed_books'])}")
    else:
        print(f'\nNo user found with library ID: {library_id}')
