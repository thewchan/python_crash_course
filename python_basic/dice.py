"""Simulate a die roll with either a 6-, 10-, or 20-sided die."""
from random import randint

class Die:
    """Simulates a die with a default number of sides of 6."""
    
    def __init__(self, sides=6):
        """Initiates the die with attribute 'sides'"""
        self.sides = sides
    
    def roll_die(self):
        """Simulates a die roll."""
        roll = randint(1, self.sides)
        print(f"Roll: {roll}")

d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

for x in range(10):
    d6.roll_die()

print('\n')

for x in range(10):
    d10.roll_die()

print('\n')

for x in range(10):
    d20.roll_die()

print('\n')