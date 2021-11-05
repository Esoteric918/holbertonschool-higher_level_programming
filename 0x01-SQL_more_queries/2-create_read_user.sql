<<<<<<< HEAD
-- Create db hbtn_0d_2 & User user_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
=======
-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'hbtn_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
>>>>>>> 742f9aa05512735d2fb9bede974017b420373d0d
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
