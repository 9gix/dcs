# Review app


        
## SQL DDL

    -- Insert Book, You need the Multimedia ID
    
    INSERT INTO multimedia (
        name, 
        description,
        price,
        created_at,
        modified_at,
        organisation_id)
    VALUES (
        '',
        '',
        NULL,
        '2015-04-08 10:36:08.448069',
        '2015-04-08 10:36:08.448069',
        2);
        
    -- After Insert SQL query, it return the primary ke which then become multimedia id
    INSERT INTO book (
        multimedia_id,
        isbn13,
        isbn10,
        published_on)
    VALUES (
        25,
        '9876543210123',
        '9876543210',
        '2013-01-20');
        
        
## SQL DDL

    CREATE TABLE IF NOT EXISTS multimedia_review (
        id INT PRIMARY KEY AUTO_INCREMENT,
        comment TEXT NOT NULL,
        rating INT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        multimedia_id INT NOT NULL,
        user_id INT NOT NULL,
        FOREIGN KEY (multimedia_id) REFERENCES multimedia(id),
        FOREIGN KEY (user_id) REFERENCES auth_user(id)
    );

    DROP TABLE IF EXISTS multimedia_review;

## SQL SELECT

### Select all review for a certain multimedia

    SELECT
        username,
        rating,
        comment,
        created_at AS datetime
    FROM multimedia_review mr, auth_user u
    WHERE u.id = mr.user_id
        AND multimedia_id = %s;


## SQL DML

### Insert a review from a user

    INSERT INTO multimedia_review
        (multimedia_id, user_id, comment, rating)
    VALUES (%s, %s, %s, %s);



# Multimedia category

## SQL DDL

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

    DROP TABLE IF EXISTS multimedia_category;
    DROP TABLE IF EXISTS category;



# Music

## SQL DDL

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

    DROP TABLE IF EXISTS album_music;
    DROP TABLE IF EXISTS album;
    DROP TABLE IF EXISTS music;

## SQL SELECT

### Select all music with its album and organisation for listing

    SELECT
        mul.id AS id,
        mul.name AS name,
        a.name AS album,
        price,
        o.name AS organisation
    FROM multimedia mul, music mus, album_music am, album a, organisation o
    WHERE mul.id = mus.multimedia_id
        AND am.music_id = mus.multimedia_id
        AND am.album_id = a.id
        AND mul.organisation_id = o.id;

### Select detailed information of a music

    SELECT
        mul.id AS id,
        mul.name AS name,
        a.name AS album,
        description,
        duration,
        price,
        o.name AS organisation
    FROM multimedia mul, music mus, album_music am, album a, organisation o
    WHERE mul.id = mus.multimedia_id
        AND am.music_id = mus.multimedia_id
        AND am.album_id = a.id
        AND mul.organisation_id = o.id
        AND mul.id = %s;



# Book

## SQL DDL

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

    DROP TABLE IF EXISTS book;


## SQL SELECT

### Select all books for listing

    SELECT m.id, m.name, description, isbn13, isbn10, price, o.name AS publisher
    FROM book, multimedia m, organisation o
    WHERE book.multimedia_id = m.id
        AND m.organisation_id = o.id;

### Select detailed information of a book

    SELECT m.id, m.name, description, isbn13, isbn10, price, o.name AS publisher
    FROM book, multimedia m, organisation o
    WHERE book.multimedia_id = m.id
        AND m.organisation_id = o.id
        AND book.isbn13 = %s


# Transaction

    -- DDL Statement --

    CREATE TABLE IF NOT EXISTS cart (
        id INT PRIMARY KEY AUTO_INCREMENT,
        buyer_id INT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        modified_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        is_completed BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (buyer_id) REFERENCES auth_user(id)
    );

    DROP TABLE IF EXISTS cart;

    -- Query Statement --

    --> Gets list of cart items in a specific cart
    SELECT ci.id, ci.object_id, m.name, m.price
    FROM cart_item ci, multimedia m 
    WHERE ci.object_id = m.id AND
          ci.cart_id = %s

    --> Gets total price of the list of cart items obtained above
    SELECT ci.id, sum(m.price) as total
    FROM cart_item ci, multimedia m 
    WHERE ci.object_id = m.id AND
          ci.cart_id = %s

    --> Gets the most recently created cart for this user
    SELECT c1.id 
    FROM cart c1
    WHERE c1.buyer_id = %s AND
         c1.is_completed = false AND
         c1.created_at >= ALL (SELECT c2.created_at FROM cart c2);

    --> Deletes an item in the cart_item
    DELETE FROM cart_item 
    WHERE cart_id = %s AND 
          object_id = %s

# Search

    -- Search for books and applications that contain 'translate' in either name, description, or the name of the people who are working on it
    SELECT
        m.id AS id,
        m.name AS name,
        m.description AS description,
        m.price AS price,
        'books' AS url_prefix,
        b.isbn13 AS url_suffix
    FROM multimedia m, book b
    WHERE
        m.id = b.multimedia_id AND
        (
            m.name LIKE '%translate%' OR
            m.description LIKE '%translate%' OR
            m.id IN (
                SELECT c.multimedia_id FROM crew c, person p
                WHERE c.person_id = p.id AND p.name LIKE '%translate%'))
    UNION
    SELECT
        m.id AS id,
        m.name AS name,
        m.description AS description,
        m.price AS price,
        'books' AS url_prefix,
        m.id AS url_suffix
    FROM multimedia m, application a
    WHERE
        m.id = a.multimedia_id AND
        (
            m.name LIKE '%translate%' OR
            m.description LIKE '%translate%' OR
            m.id IN (
                SELECT c.multimedia_id FROM crew c, person p
                WHERE
                    c.person_id = p.id AND
                    p.name LIKE '%translate%'
            )
        )
