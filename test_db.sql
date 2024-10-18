CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each borrowing transaction
    user_id INT,                             -- Foreign key referencing the user who borrowed the book
    book_id INT,                             -- Foreign key referencing the borrowed book
    borrow_date DATE NOT NULL,               -- Date when the book was borrowed
    return_date DATE DEFAULT NULL,           -- Date when the book was returned (NULL if not returned yet)
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,   -- References users table
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE    -- References books table
);


CREATE TABLE authors (
	id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(255),
    biography TEXT
);

CREATE TABLE books (
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(400) NOT NULL,
    author_id INT,
    genre VARCHAR(100),
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

SELECT * FROM books;
SELECT * FROM borrowed_books;
SELECT * FROM users; 
SELECT * FROM authors;

ALTER TABLE users CHANGE name user_name VARCHAR(255) NOT NULL;

SHOW CREATE TABLE users;
