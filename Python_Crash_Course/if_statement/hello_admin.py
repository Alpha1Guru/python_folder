current_users = ["rapheal","odinaka","micheal","udoh","Admin","favour","mujeeb",]
# current_users.clear()
if current_users:
    for user in current_users:
        if user.lower()== "admin":
            print("Hello Admin would you like to see status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to get some users!")
    
new_users = ["Mujeeb","job","avast","emily","okoye"]
def CheckNewUser(newuser):
    if newuser.lower() not in [Cuser.lower() for Cuser in current_users]:
        print(f"The user name {newuser.title()} is available")
    else:
        print(f"The user name {newuser.title()} is already in use.")
        newuser = input("You will need to enter another username.\n\t User name: ")
        CheckNewUser(newuser)

for user in new_users:
    CheckNewUser(user)