CREATE TABLE IF NOT EXISTS multimedia_review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    comment TEXT NOT NULL,
    rating INT NOT NULL,
    created_at DATETIME NOT NULL,
    multimedia_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (multimedia_id) REFERENCES multimedia(id),
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);
