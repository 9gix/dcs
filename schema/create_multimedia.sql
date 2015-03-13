CREATE TABLE multimedia (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE book (
    id INT NOT NULL,
    multimedia_id INT NOT NULL,
    isbn13 CHAR(13) NULL,
    isbn10 CHAR(10) NULL,
    published_on DATE NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_book_multimedia
        FOREIGN KEY (multimedia_id)
        REFERENCES multimedia (id)
);

CREATE TABLE category (
);

CREATE TABLE multimedia_category (
);

CREATE TABLE content (
);

CREATE TABLE multimedia_content (
);

CREATE TABLE multimedia_review (
);
