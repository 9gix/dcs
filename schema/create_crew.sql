CREATE TABLE IF NOT EXISTS organisation (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE IF NOT EXISTS crew (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multimedia_id INT NOT NULL,
    person_id INT NOT NULL,
    role_id INT NOT NULL,
    organisation_id INT NOT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id),
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (organisation_id) REFERENCES organisation(id)
);
