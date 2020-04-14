#list exercises
numbers = range(1, 21)
#for number in numbers:
#    print(number)

numbers = range(1, 1_000_001)
#for number in numbers:
#    print(number)

million_list = list(range(1, 1_000_001))
print(min(million_list))
print(max(million_list))
print(sum(million_list))

odd_numbers = range(1, 21, 2)
for number in odd_numbers:
    print(number)
    
threes = range(3, 31, 3)
for three in threes:
    print(three)

numbers = range(1,11)
for number in numbers:
    print(number ** 3)
    
cubes = [number ** 3 for number in range(1,11)]
print(cubes)