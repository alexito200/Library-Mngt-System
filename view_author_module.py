
authors = {}

def view_author(authors):
    author_name = input("\nEnter the author's name you want to search for: ")
    if author_name in authors:
        author_info = authors[author_name]
        print(f"\nAuthor Details:\nName: {author_name}\nBiography: {author_info['biography']}")
    else:
        print(f'\nNo author found with the name: {author_name}')