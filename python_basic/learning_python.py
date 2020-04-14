file_name = 'python_notes.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.strip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())