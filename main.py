import hashlib
import json
import getpass

filename = "./data/passwords.json"
password_manager = {
    "username": "username",
    "password": "password",
}
account = 0

def sign_up():
    password_data = {}
    with open(filename, "r") as f:
        temp = json.load(f)
    password_data["username"] = input("Sign up with your username")
    password = getpass.getpass("Enter your password")
    salt = "5gz"
    dataBase_password = password+salt
    hashed = hashlib.md5(dataBase_password.encode())
    print(hashed.hexdigest())
    password_data["password"] = hashed.hexdigest()
    temp.append(password_data)
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)

def login():
    print("Will be redirected to home if invalid credentials")
    username = input("Enter your username")
    password = getpass.getpass("Enter your password")
    salt = "5gz"
    dataBase_password = password+salt
    hashed = hashlib.md5(dataBase_password.encode())
    with open(filename, "r") as f:
        temp = json.load(f)
        for entry in temp:
            if username in entry["username"] and hashed.hexdigest() in entry["password"]:
               print('You are logged in')
            else:
                print("")


def exit_app(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

while True:
    choice = int(input("Enter 1 to sign up 2 to login 3 to exit"))
    if choice == 1:
        sign_up()
        account += 1
    if choice == 2:
        login()
    if choice == 3:
        exit_app(filename)
        break
    if choice < 1 or choice > 3:
        print('Invalid number')