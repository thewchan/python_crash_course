print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    try:
        first_number = int(first_number)
    except ValueError:
        print("Please enter a number!")
        continue
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        second_number = int(second_number)
    except ValueError:
        print("Please enter a number!")
        continue
    answer = first_number + second_number
    print(answer)