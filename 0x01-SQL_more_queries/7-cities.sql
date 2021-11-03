CREATE DATABASE if not EXISTS hbtn_0d_usa;
CREATE TABLE if not EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL  ,
    name VARCHAR(256) PRIMARY KEY(id),
    FOREIGN KEY(states_id) REFERENCES states(id) NOT NULL);
