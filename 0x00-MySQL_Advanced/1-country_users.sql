-- This SQL script creates a table users that has
-- these attributes: id, email, name, country

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
     country ENUM('US', 'CO', 'TN') DEFAULT 'US',
);
