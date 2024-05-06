# CREATE user "military"@"localhost" IDENTIFIED BY "1234";
# GRANT ALL PRIVILEGES ON military.* TO "military"@"localhost";

# CREATE DATABASE IF NOT EXISTS military;

use military;

drop table if exists coordinates;
CREATE TABLE coordinates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6)
)comment ='The location of targets';

DROP TABLE IF EXISTS location;
CREATE TABLE location (
    id INT AUTO_INCREMENT PRIMARY KEY,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6)
)comment ='current aircraft location';