import bcrypt

users = {}

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ").encode('utf-8')

    
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    
    users[username] = hashed_password

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ").encode('utf-8')

    
    hashed_password = users.get(username)

    if hashed_password and bcrypt.checkpw(password, hashed_password):
        print("Login successful!")
        # Implementing  secured page
        print("Welcome to the secured page!")
    else:
        print("Login failed. Invalid credentials.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
