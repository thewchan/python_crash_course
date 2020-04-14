catfile = 'cats.txt'
dogfile = 'dogs.txt'

try:
    with open(catfile) as dog_f:    
        doglines = dog_f.readlines()
except FileNotFoundError:
    #print("There are no dogs...")
    pass
else:
    print("Here are the dogs!")
    for dog in doglines:
        print(f"- {dog.strip()}")

try:
    with open(dogfile) as cat_f:
        catlines = cat_f.readlines()
except FileNotFoundError:
    #print("There are no cats...")
    pass
else:
    print("Here are the cats!")
    for cat in catlines:
        print(f"- {cat.strip()}")
