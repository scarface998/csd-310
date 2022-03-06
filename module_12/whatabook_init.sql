/*
    Title: whatabook.init.sql
    Author: Jake Dawson
    Date: March 6 2022
    Description: WhatABook database initialization script.
*/


-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('127 Bing Bong Road, Bing Idaho, 1234');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Fire', 'Lord of Fire', 'Book about fire');

INSERT INTO book(book_name, author, details)
    VALUES('Water', 'Lord of Water', 'Book about water');

INSERT INTO book(book_name, author, details)
    VALUES('Wind', 'Lord of Wind', "Book about Wind");

INSERT INTO book(book_name, author, details)
    VALUES('Ice', 'Lord of Ice', 'Book about Ice');

INSERT INTO book(book_name, author, details)
    VALUES('Beasts', 'Lord of Beasts', 'Book about beasts');

INSERT INTO book(book_name, author, details)
    VALUES("Rocks", 'Lord of Rocks', 'Book about rocks');

INSERT INTO book(book_name, author, details)
    VALUES('Air', 'Lord of Air', 'Book about air');

INSERT INTO book(book_name, author, details)
    VALUES('Elements', 'Lord of Elements', 'Book about elements');

INSERT INTO book(book_name, author, details)
    VALUES('Trash', 'Lord of Trash', 'Book about Trash');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Robert', 'Dodson');

INSERT INTO user(first_name, last_name)
    VALUES('George', 'Dawn');

INSERT INTO user(first_name, last_name)
    VALUES('Bill', 'Bugs');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Robert'), 
        (SELECT book_id FROM book WHERE book_name = 'Wind')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'George'),
        (SELECT book_id FROM book WHERE book_name = 'Rocks')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bill'),
        (SELECT book_id FROM book WHERE book_name = 'Elements')
    );
