CREATE TABLE IF NOT EXISTS multimedia (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10,2) NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS book (
    multimedia_id INT NOT NULL,
    isbn13 CHAR(13) NULL,
    isbn10 CHAR(10) NULL,
    published_on DATE NULL,
    PRIMARY KEY (multimedia_id),
    CONSTRAINT fk_book_multimedia
        FOREIGN KEY (multimedia_id)
        REFERENCES multimedia (id)
);

CREATE TABLE IF NOT EXISTS album (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS music (
    multimedia_id INT NOT NULL PRIMARY KEY,
    duration INT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id)
);

CREATE TABLE IF NOT EXISTS album_music (
    id INT PRIMARY KEY AUTO_INCREMENT,
    album_id INT NOT NULL,
    music_id INT NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id),
    FOREIGN KEY (music_id) REFERENCES music(multimedia_id)
);

CREATE TABLE IF NOT EXISTS category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS multimedia_category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multimedia_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS multimedia_content (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multimedia_id INT NOT NULL,
    caption VARCHAR(128) NOT NULL,
    url VARCHAR(200) NOT NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id)
);

CREATE TABLE IF NOT EXISTS multimedia_review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    comment TEXT NOT NULL,
    rating INT NOT NULL,
    multimedia_id INT NOT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id)
);
