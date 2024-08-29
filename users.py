current_users = ['bond','zahidbond','admin','hank','james']
new_users = ['charlie','bond','hank','stu','tom']

for username in new_users:
    if username in current_users:
        print(username+" exists!, enter a new username")
    else:
        print(username+" available!")

    
