# Library Management System

A command-line based Library Management System built with Python and SQLite. It allows for efficient management of books, users (students and teachers), and their borrow/return records.

## Features

- **Book Management**:
  - Add new books
  - View all books
  - Search by title or author
  - Delete books

- **User Management**:
  - Register users with roles (`student` or `teacher`)
  - List all registered users

- **Borrow & Return**:
  - Issue books to users (with availability check)
  - Return issued books
  - View transaction history (with status)

- **Persistence**: All data is stored in a local SQLite database (`library.db`).

## Project Structure

```
Library_Management/
├── Database
│   └── library.db 
├── Scripts/
│   └── book.py   
│   └── borrow.py
│   └── db.py                       
│   └── user.py         
│   └── utils.py
├── main.py
└── README.md   ← You’re reading it! 
```

## How to Run

1. **Clone the repository**:

2. **Run the application**:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.7+
- No external libraries required (uses `sqlite3` from the Python Standard Library)
 
---

## Authors
- **Ishita Modi** — [LinkedIn](https://www.linkedin.com/in/ishita-modi-155676341/) • [GitHub](https://github.com/ishita230105)
- **Mayank Singh** — [LinkedIn](https://www.linkedin.com/in/mayank-singh-367572246/) • [GitHub](https://github.com/thakurmayanksingh)
 
---


