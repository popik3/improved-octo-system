import json

username = input("What is your name?")

filename = 'a1.json'
with open(filename, 'w')as f:
    json.dump(username, f)
    print(f"We'll remember you come back, {username}")