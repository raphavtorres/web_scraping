CREATE DATABASE web_scraping;

USE web_scraping;

CREATE TABLE products (
    id INT AUTO_INCREMENT,
    productName VARCHAR(255) NOT NULL,
    productPrice BOOLEAN,
    PRIMARY KEY (id)
);

INSERT INTO products (productName, productPrice) VALUES ("");