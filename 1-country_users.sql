-- This SQL script creates a table users that has
-- these attributes: id, email, name, country

CREATE TYPE countryEnum AS ENUM ('US', 'CO', 'TN');

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    countryEnum NOT NULL DEFAULT 'US'
);
