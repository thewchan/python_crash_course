favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print('\n')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print('\n')

for name in favorite_languages.keys():
    print(name.title())
print('\n')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("\n")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print('\n')

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#set is a collection of unique values

polltakers = ['jen', 'sarah', 'edward', 'phil', 'drew', 'cody', 'danny']

for polltaker in polltakers:
    if polltaker in favorite_languages.keys():
        print(f"{polltaker.title()}, thank you for taking the poll.")
    else:
        print(f"{polltaker.title()}, please take the poll asap!")
print("\n")

#new group
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorte languages are:")
    for language in languages:
        print(f"\t{language.title()}")

