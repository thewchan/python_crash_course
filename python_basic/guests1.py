file_name = 'guest_list.txt'
print("We are building our party guest list! (Enter 'quit' to exit.)")
done_flag = False
while done_flag == False:
    guest = input("Enter guest name: ")
    if guest == 'quit':
        done_flag = True
        continue
    with open(file_name, 'a') as file_object:
        file_object.write(f"{guest}\n")
    print(f"Thanks for signing up, {guest.title()}!")
    
try:
    with open(file_name) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print("Sorry, no one signed up for the party!")
else:
    print("Here are those who signed up on the guest list:")
    for line in lines:
        print(line.strip())
        
