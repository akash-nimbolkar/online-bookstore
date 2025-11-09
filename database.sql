CREATE DATABASE bookstore;
USE bookstore;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    price DECIMAL(10,2)
);

INSERT INTO books (title, author, price) VALUES
("Clean Code", "Robert Martin", 500.00),
("JavaScript: The Good Parts", "Douglas Crockford", 400.00),
("The Pragmatic Programmer", "Andrew Hunt", 650.00);
