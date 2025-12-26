<p align="center">
  <h1 align="center">Library Management System</h1>
  <p align="center">Python Tkinter Desktop Application with MySQL</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green">
  <img src="https://img.shields.io/badge/Database-MySQL-orange">
  <img src="https://img.shields.io/badge/Type-Academic-lightgrey">
</p>

---

## 📌 Overview

This is a **GUI-based Library Management System** developed using **Python Tkinter** and **MySQL**.  
The project demonstrates **desktop GUI development**, **database connectivity**, and **CRUD operations**.

It is created as an **academic learning project**.

---

## ✨ Features

- Desktop GUI using Tkinter
- Member type selection (Student / Teacher)
- Book selection from predefined list
- Automatic filling of:
  - Book ID
  - Borrow Date
  - Due Date (15 days)
  - Days on Book
  - Late Return Fine (static)
  - Final Price
- MySQL database integration
- CRUD operations:
  - Add record
  - View records
  - Update record
  - Delete record
- Record display using TreeView
- Exit confirmation dialog

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Core language |
| Tkinter | GUI |
| MySQL | Database |
| mysql-connector-python | Database connectivity |

---

## Library-Management-System/

│

├── main.py        # The main Python script (Tkinter GUI) 

├── database.sql   # Database schema and table setup

└── README.md      # Project documentation

---

## Database Overview

**Database Name:** project  
**Table Name:** library

| Column | Description |
|------|------------|
| Member | Member type |
| BookID | Book identifier |
| BookName | Book name |
| FirstName | Member first name |
| LastName | Member last name |
| RollNo | Roll number |
| Mobile | Mobile number |
| DateBorrowed | Borrow date |
| DateDue | Due date |
| DaysonBook | Days on book |
| LateReturnFine | Fine amount |
| DateOverDue | Overdue status |
| FinalPrice | Book price |

---

## Installation

```bash
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System
pip install mysql-connector-python
python main.py




