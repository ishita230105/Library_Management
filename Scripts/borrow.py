from Scripts.db import connect
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def issue_book():
    try:
        user_id = int(input("Enter user ID: ").strip())
        book_id = int(input("Enter book ID: ").strip())
        issue_date = datetime.now().strftime(DATE_FORMAT)

        conn = connect()
        cursor = conn.cursor()

        # Check book availability
        cursor.execute("SELECT available_copies FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        if not book:
            print("❌ Book not found.")
            return
        if book[0] <= 0:
            print("❌ No copies available.")
            return

        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            print("❌ User not found.")
            return

        # Record transaction and update copies
        cursor.execute("""
            INSERT INTO transactions (user_id, book_id, issue_date, return_date)
            VALUES (?, ?, ?, NULL)
        """, (user_id, book_id, issue_date))
        cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        print("✅ Book issued successfully.")
    except ValueError:
        print("❌ Invalid input.")

def return_book():
    try:
        transaction_id = int(input("Enter transaction ID to return book: ").strip())
        return_date = datetime.now().strftime(DATE_FORMAT)

        conn = connect()
        cursor = conn.cursor()

        # Check transaction exists and is not already returned
        cursor.execute("""
            SELECT book_id, return_date FROM transactions WHERE id = ?
        """, (transaction_id,))
        tx = cursor.fetchone()
        if not tx:
            print("❌ Transaction not found.")
            return
        if tx[1] is not None:
            print("❌ Book already returned.")
            return

        book_id = tx[0]

        # Mark as returned and update available copies
        cursor.execute("UPDATE transactions SET return_date = ? WHERE id = ?", (return_date, transaction_id))
        cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        print("✅ Book returned successfully.")
    except ValueError:
        print("❌ Invalid input.")

def view_transactions():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, u.name, b.title, t.issue_date, t.return_date
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        JOIN books b ON t.book_id = b.id
        ORDER BY t.id DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No transactions yet.")
        return

    print("\n--- Transaction History ---")
    for row in rows:
        status = "Returned" if row[4] else "Issued"
        print(f"ID: {row[0]} | User: {row[1]} | Book: {row[2]} | Issued: {row[3]} | Returned: {row[4] or '---'} | Status: {status}")

def borrow_menu():
    while True:
        print("\n--- Borrow/Return Menu ---")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Transactions")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            issue_book()
        elif choice == '2':
            return_book()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            break
        else:
            print("Invalid option. Try again.")
