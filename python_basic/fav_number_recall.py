import json

filename = 'fav_number.json'
try:
    with open(filename) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    print("I don't know what your favorite number is...")
else:
    print(f"I know your favorite number! It's {fav_number}!")