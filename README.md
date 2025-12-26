📚 Library Management System (Python + Tkinter + MySQL)

A GUI-based Library Management System developed using Python Tkinter and MySQL.
This project demonstrates GUI design, database connectivity, and CRUD operations in Python.

It is built as an academic / learning project to understand how desktop applications interact with databases.

🚀 Features

🖥️ Desktop GUI using Tkinter

👤 Member type selection (Student / Teacher)

📚 Book selection from predefined list

🗓️ Automatic filling of:

Book ID

Borrow Date

Due Date (15 days)

Days on Book

Late Return Fine (static)

Final Price

🗄️ MySQL database integration

🔄 CRUD operations:

Add new record

View records

Update records

Delete records

📊 Display all records using TreeView

🧾 View selected record details in text area

❌ Exit confirmation dialog

🛠️ Tech Stack

Language: Python

GUI: Tkinter, ttk

Database: MySQL

Database Connector: mysql-connector-python

📂 Project Structure
Library-Management-System/
│
├── main.py        # Main application file
├── README.md      # Project documentation
└── database.sql   # MySQL table structure

🗄️ Database Structure
CREATE DATABASE project;
USE project;

CREATE TABLE library (
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

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System

2️⃣ Install Dependency
pip install mysql-connector-python

3️⃣ Update MySQL Credentials

Update inside main.py:

host="localhost"
username="root"
password="1234"
database="project"

4️⃣ Run Application
python main.py

🧠 How the Application Works

Books are selected from a predefined list

Selecting a book auto-fills related details

Records are stored in a MySQL database

TreeView displays all records

Clicking a row loads data back into input fields

CRUD operations are executed through buttons

⚠️ Current Limitations

Late return fine is static

Overdue detection is not dynamic

Date values are stored as strings

No authentication system

Designed for academic use

📌 Future Enhancements

🔐 Login authentication

📅 Dynamic overdue & fine calculation

📄 Export records (Excel / PDF)

🗃️ Improved database schema

🌐 Web version using Django or Flask

👨‍💻 Author

Suraj Chavan
🎓 MCA Graduate
🐍 Python | Django | MySQL
📍 Mumbai, India

⭐ Conclusion

This project focuses on Python GUI development and database operations and serves as a strong foundation for building more advanced library or management systems.****
