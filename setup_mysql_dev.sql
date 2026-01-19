-- MYSQL setup for the shopnest database for the project
-- Shows the reperentaion of the databases meant for the project

-- Creating the development database
CREATE DATABASE IF NOT EXISTS shopnest_dev_db;

-- Creating testing database
CREATE DATABASE IF NOT EXISTS shopnest_test_db;

-- Create the users on this database (and adjust password as needed)
CREATE USER IF NOT EXISTS 'shopnest_dev'@'localhost' IDENTIFIED BY 'Siriusa1.615';

-- Grant privileges to user on development databases
GRANT ALL PRIVILEGES ON shopnest_dev_db.* TO 'shopnest_dev'@'localhost';

-- Gramt privileges to user on test databases
GRANT ALL PRIVILEGES ON shopnest_test_db.* TO 'shopnest_dev'@'localhost';

-- Flush all privileges
FLUSH PRIVILEGES;
