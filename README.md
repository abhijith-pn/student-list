# student-list
A student search rest api

## database setup
To create database "studentlist" and user "ubuntu" and password "ubuntu"
```
CREATE DATABASE studentlist WITH ENCODING 'UTF8';
CREATE USER ubuntu WITH ENCRYPTED PASSWORD 'ubuntu';
ALTER ROLE ubuntu set client_encoding TO 'utf8';
ALTER ROLE ubuntu SET default_transaction_isolation TO 'read committed';
ALTER ROLE ubuntu SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE studentlist to ubuntu;
```