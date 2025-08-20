CREATE DATABASE if NOT EXISTS django_db;
USE django_db;

CREATE TABLE IF NOT EXISTS student (
    id char(32) NOT NULL, 
    name varchar(50) NOT NULL, 
    email varchar(254) NOT NULL, 
    phone varchar(10) NOT NULL, 
    city varchar(20) NOT NULL, 
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4;
