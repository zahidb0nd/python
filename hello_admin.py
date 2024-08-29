# hello_admin.py

# List of users (currently empty or populated with usernames)
users = []

# Check if the list of users is empty
if not users:
    print("We need to find some users!")
else:
    for user in users:
        print(f"Hello, {user}!")

