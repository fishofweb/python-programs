print("Welcome to the Database Admin Program.\n")

db = {
    "admin":"12345678",
    "shanza": "shanza1000",
    "sadaf": "sadaf1000",
    "ammara": "ammara1000",
    "mahnoor": "mano1000",
    "saniya": "saniya1000",
    "maryam": "maryam1000",
    "sonia": "sonia1000",
}

username = input("Enter your username: ").lower().strip()
password = input("Enter your password: ").lower().strip()

if username not in db.keys():
    print("incorrect username")
    quit()

if password not in db.values():
    print("incorrect password")
    quit()

if username == 'admin' and password == '12345678':
    print("welcome", username, "here is you database\n\n")
    for k , v in db.items():
        print(k)
        print("user:",k,"\tpassword:",v)


for user,passwd in db.items():
    if user == username and password == passwd and username != 'admin' and password != '12345678':
        print("Hello",username,"You are logged in!")
        print("\n")
        change_pwd = input("Would you like to change your password(y/n): ").lower().strip()
        if change_pwd == 'y':
            new = input("Type your new password: ")
            if len(new)<8:
                print("Password is too short , type atleast 8 characters.")
                break
            new_confirm = input("Type your new password again: ")
            if new == new_confirm:
                db[username] = new_confirm
                print("your password is changed to", new_confirm)
            else:
                print("password mismatched")
                break
        else:
            print("ok your password is still", passwd)
            break

print("\tUsername:",username,"\t\tpassword:",password)