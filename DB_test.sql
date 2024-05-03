# create database db_test;
use db_test;

drop table if exists coordinates;
CREATE TABLE coordinates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6)
)comment ='The location of targets';

DROP TABLE IF EXISTS location;
CREATE TABLE location (
    IS_GPS BOOL PRIMARY KEY,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6)
)comment ='current aircraft location';