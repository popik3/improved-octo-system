import json

filename = 'a1.json'
with open(filename)as f:
    numbers = json.load(f)

print(numbers)