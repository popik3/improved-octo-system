import json

def get_stored_username():
    filename = 'a1.json'
    try:
        with open(filename)as f:
            username = json.load(f)
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename = 'a1.json'
    with open(filename, 'w')as f:
        json.dump(username, f)
    return username
def greet_user():
        username = get_stored_username()
        if username:
            print(f"Welcome back, {username}")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")

greet_user()

