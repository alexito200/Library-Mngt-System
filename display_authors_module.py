authors = {}

def display_authors(authors):
    print("\nList of Authors:")
    for index, (author_name, author_info) in enumerate(authors.items(), start=1):
        print(f"\n{index}. Author Name: {author_name}, Biography: {author_info['biography']}")
