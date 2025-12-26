CREATE DATABASE IF NOT EXISTS project;
USE project;

CREATE TABLE IF NOT EXISTS library (
    Member VARCHAR(20),
    BookID VARCHAR(20),
    BookName VARCHAR(100),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    RollNo VARCHAR(20),
    Mobile VARCHAR(15),
    DateBorrowed VARCHAR(50),
    DateDue VARCHAR(50),
    DaysonBook VARCHAR(20),
    LateReturnFine VARCHAR(20),
    DateOverDue VARCHAR(20),
    FinalPrice VARCHAR(20)
);
