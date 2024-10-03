class Book:

    def __init__(self, title, author, genre, publication_status, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_status = publication_status
        self.availability = availability


class User:
    def __init__(self, name, library_id, borrowed_books):
        self.__name = name
        self.__library_id = library_id
        self.borrowed_books = borrowed_books


    def name(self):
        return self.__name

    def name(self, user_name):
        if not user_name:
            raise ValueError("User name cannot be empty.")
        self.__name = user_name

    def library_id(self):
        return self.__library_id

    def library_id(self, id):
        if not id:
            raise ValueError("ID cannot be empty.")
        self.__library_id = id

class Author:
    def __init__(self, author_name, biography):
        self.author_name = author_name
        self.biography = biography