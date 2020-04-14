usernames = ['admin', 'jaden', 'will', 'willow', 'jade']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status "+ 
                  "report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!\n")

current_users = usernames[:]
new_users = ['jaden', 'john', 'hank', 'Will', 'cody']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user}, you will need a differnt username.")
    else:
        print(f"{new_user}, this username is available.")