CREATE TABLE IF NOT EXISTS cart (
	id INT PRIMARY KEY AUTO_INCREMENT,
	buyer_id INT NOT NULL,
	created_at DATETIME,
	modified_at DATETIME,
	FOREIGN KEY (buyer_id) REFERENCES auth_user(id)
);

CREATE TABLE IF NOT EXISTS cart_item (
	id INT PRIMARY KEY AUTO_INCREMENT,
	cart_id INT NOT NULL,
	multimedia_id INT NOT NULL,
	object_type VARCHAR(45) NOT NULL,
	quantity INT NOT NULL,
	FOREIGN KEY (cart_id) REFERENCES cart(id),
	FOREIGN KEY (multimedia_id) REFERENCES multimedia(id)
);

CREATE TABLE IF NOT EXISTS transaction (
	id INT PRIMARY KEY,
	cart_id INT NOT NULL,
	created_at DATETIME NOT NULL,
	modified_at DATETIME NOT NULL,
	FOREIGN KEY (cart_id) REFERENCES cart(id)
);