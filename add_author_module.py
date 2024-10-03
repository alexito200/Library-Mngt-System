# Module 5: 
# Adding a new author with author details.
    # prompt for user input
    # ask for author's name and biography
    # add into a 'author' dictionary
# Viewing author details.
    # prompt for user input
    # ask what author they are searching for
    # print out the author's details
# Displaying a list of all authors.
    # user enters the number for this selection
    # program prints out all authors in enumerated format

authors = {}

def add_author():
    author_name = input("\nEnter the author's name: ")
    biography = input(f"\nEnter a short biography for {author_name}: ")

    authors[author_name] = {
        'biography': biography
    }
    print(f'\nAuthor "{author_name}" added successfully!')



