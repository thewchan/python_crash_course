#practice with lists
guests = ['Jesus', 'Mozart', 'Obama', 'David Dobrik', 'Mary Berry', 'Claire Saffitz', 'Chris Morroco']
print(guests)
print(f'Dear {guests[0]}, please come to my party!')
print(f'Dear {guests[1]}, please come to my party!')
print(f'Dear {guests[2]}, please come to my party!')
print(f'Dear {guests[3]}, please come to my party!')
print(f'Dear {guests[4]}, please come to my party!')
print(f'Dear {guests[5]}, please come to my party!')
print(f'Dear {guests[6]}, please come to my party!')

print(f"Uh oh {guests[3]} can't make it!")

guests[3] = 'Liza Koshy'
print(f'Dear {guests[3]}, please come to my party!')
print(f'Current guests: {guests}')
print('We now have a bigger table!')
guests.insert(0, 'Buddha')
guests.insert(3, 'Drew Gooden')
guests.append('Danny Gonzalez')
print(f'Current guests: {guests}')

print('Just kidding we only have room for 2 ha ha!')
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
disinvite = guests.pop()
print(f"Sorry {disinvite}, you can't come anymore!")
print(f'Current guests: {guests}')
del guests[1]
del guests[0]
print(f'Current guests: {guests}')