CREATE TABLE IF NOT EXISTS cart (
    id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (buyer_id) REFERENCES auth_user(id)
);

CREATE TABLE IF NOT EXISTS transaction (
    id INT PRIMARY KEY,
    cart_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES cart(id)
);
