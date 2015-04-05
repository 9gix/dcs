CREATE TABLE IF NOT EXISTS cart (
	id INT PRIMARY KEY AUTO_INCREMENT,
	buyer_id INT NOT NULL,
	created_at DATETIME,
	modified_at DATETIME,
	FOREIGN KEY (buyer_id) REFERENCES auth_user(id)
);

CREATE TABLE IF NOT EXISTS transaction (
	id INT PRIMARY KEY,
	cart_id INT NOT NULL,
	created_at DATETIME NOT NULL,
	modified_at DATETIME NOT NULL,
	FOREIGN KEY (cart_id) REFERENCES cart(id)
);
