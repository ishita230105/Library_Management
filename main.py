from Scripts.db import create_tables
from Scripts.book import book_menu
from Scripts.user import user_menu
from Scripts.borrow import borrow_menu

def main_menu():
    while True:
        print("\n--- Library Management ---")
        print("1. Book Management")
        print("2. User Management")
        print("3. Borrow/Return")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            borrow_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    create_tables()
    main_menu()
