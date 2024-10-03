
def display_books(books):
    print("\nList of Books:")
    for index, (title, details) in enumerate(books.items(), start=1):
        print(f"\n{index}. Title: '{title}', Author: {details['author']}, Genre: {details['genre']}, Status: {details['status']}")
