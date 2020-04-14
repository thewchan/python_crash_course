filename = 'don_quixote.txt'

with open(filename) as f:
    lines = f.readlines()

the_count = 0
for line in lines:
    the_count += line.lower().count('the ')

print(f"There are {the_count} instances of the word 'the' in this book.")