CREATE TABLE IF NOT EXISTS album_music (
	id INT PRIMARY KEY AUTO_INCREMENT,
	album_id INT REFERENCES album(id),
	music_id INT REFERENCES music(id)
)