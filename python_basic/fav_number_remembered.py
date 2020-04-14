import json

def fav_number_recall():
    """recall favorite number if already stored in .json."""
    filename = 'fav_number.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number

def get_fav_number():
    """Ask user for fav number"""
    filename = 'fav_number.json'
    fav_number = input("What is your favorite number?")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
    return fav_number

def fav_number_remembered():
    """Tell user what their fav number is if known. Otherwise ask for one."""
    fav_number = fav_number_recall()
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}!")
    else:
        fav_number = get_fav_number()
        print(f"{fav_number}. "
            "Okay I'll remember what your favorite number is next time!")
        
fav_number_remembered()