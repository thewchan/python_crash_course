number = input("Choose a number, and I'll tell you if it is a multiple of ten: ")
if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")