age = ""

while age != 'quit':
    age = input("What is your age?\n(Enter 'quit' to exit program) ")
    if age == 'quit':
        continue
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) < 12:
        print("Your ticket price is $10.")
    elif int(age) >= 12:
        print("Your ticket price is $15.")
 



