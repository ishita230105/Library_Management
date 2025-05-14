from Scripts.db import connect

def register_user():
    name = input("Enter user name: ").strip()
    role = ""
    while role not in ("student", "teacher"):
        role = input("Enter role (student/teacher): ").strip().lower()
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, role) VALUES (?, ?)", (name, role))
    conn.commit()
    conn.close()
    print("User registered successfully.")

def list_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role FROM users")
    users = cursor.fetchall()
    conn.close()

    if not users:
        print("No users registered.")
        return

    print("\n--- Registered Users ---")
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]} | Role: {user[2]}")

def user_menu():
    while True:
        print("\n--- User Management ---")
        print("1. Register User")
        print("2. List Users")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

