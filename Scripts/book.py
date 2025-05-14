from Scripts.db import connect

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    total = int(input("Enter number of copies: "))
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)",
                   (title, author, total, total))
    conn.commit()
    conn.close()
    print("Book added successfully.")

def view_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, total_copies, available_copies FROM books")
    books = cursor.fetchall()
    conn.close()

    if not books:
        print("No books found.")
        return

    print("\n--- Book List ---")
    for book in books:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Total: {book[3]} | Available: {book[4]}")

def search_books():
    keyword = input("Enter title or author to search: ").strip()
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, total_copies, available_copies FROM books WHERE title LIKE ? OR author LIKE ?",
                   (f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    conn.close()

    if not results:
        print("No matching books found.")
        return

    print("\n--- Search Results ---")
    for book in results:
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Total: {book[3]} | Available: {book[4]}")

def delete_book():
    book_id = input("Enter book ID to delete: ").strip()
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("Book deleted if it existed.")

def book_menu():
    while True:
        print("\n--- Book Management ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Delete Book")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")
