#start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print("Verifying user: "+current_users.title())
    confirmed_users.append(current_users)
#display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())
