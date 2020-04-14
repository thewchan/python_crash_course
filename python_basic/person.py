person_0 = {
    'first name': 'drew',
    'last name': 'gooden',
    'age': 23,
    'city': 'orlando',
    }

person_1 = {
    'first name': 'danny',
    'last name': 'gonzalez',
    'age': 24,
    'city': 'atlanta',
    }

person_2 = {
    'first name': 'cody',
    'last name': 'ko',
    'age': 28,
    'city': 'los angeles',
    }

people = [person_0, person_1, person_2]

for person in people:
    for key, value in person.items():
        print(f"{key}:\t{value}")
    print("\n")
        