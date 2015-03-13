CREATE TABLE music (
	id INT PRIMARY KEY AUTO_INCREMENT,
	multimedia_id INT REFERENCES multimedia(id),
	duration INT
)