-- script to create and prepare mysql server
CREATE DATABASE IF NOT EXISTS study_room_db;

CREATE USER IF NOT EXISTS 'study_room_dev'@'localhost' IDENTIFIED BY 'study_room_pwd';
GRANT ALL ON study_room_db.* TO 'study_room_dev'@'localhost';
