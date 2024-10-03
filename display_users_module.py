
def display_users(users):
    print("\nList of Users:")
    for index, (library_id, user_info) in enumerate(users.items(), start=1):
        borrowed_books = ', '.join(user_info['borrowed_books']) if user_info['borrowed_books'] else 'None'
        print(f"\n{index}. Library ID: {library_id}, Name: {user_info['name']}, Borrowed Books: {borrowed_books}")
