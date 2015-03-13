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

CREATE TABLE IF NOT EXIST category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    parent_category_id INT NOT NULL REFERENCES category(id)
);

CREATE TABLE IF NOT EXIST multimedia_category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multimedia_id INT NOT NULL REFERENCES multimedia(id),
    category_id INT NOT NULL REFERENCES category(id)
);

CREATE TABLE IF NOT EXIST content (
    id INT PRIMARY KEY AUTO_INCREMENT,
    caption VARCHAR(128) NOT NULL,
    url VARCHAR(200) NOT NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL
);

CREATE TABLE IF NOT EXIST multimedia_content (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multimedia_id INT NOT NULL REFERENCES multimedia(id),
    content_id INT NOT NULL REFERENCES content(id)
);

CREATE TABLE IF NOT EXIST multimedia_review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    comment TEXT NOT NULL,
    rating INT NOT NULL,
    multimedia_id INT NOT NULL REFERENCES multimedia(id)
);
