"""Simulates a simple fake lottery"""
from random import choice

numbers_letters = [
        34, 12, 89, 38, 57, 12, 4, 90, 85, 45, 
        'F', 'R', 'L', 'V', 'O',
        ]

lottery = (
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}"
    )
print(f"The winning lottery is: {lottery}")

my_ticket = (
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}"
    )
ticket_count = 1
print(my_ticket)

while my_ticket != lottery:
    my_ticket = (
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}-{choice(numbers_letters)}-"
    f"{choice(numbers_letters)}"
    )
    print(my_ticket)
    ticket_count += 1

print(f"The winning lottery is: {lottery}")
print(ticket_count)
