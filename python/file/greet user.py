import json

filename = 'a1.json'
with open(filename)as f:
    username = json.load(f)
    print(f"Welcome back, {username}")