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
