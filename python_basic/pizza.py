#for loop exercises
pizzas = ['cheese', 'peperoni', 'sausage']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza} pizza.")
print("I really like pizzas!")

friends_pizzas = pizzas[ : ]
pizzas.append('anchovie')
friends_pizzas.append('hawaiian')
print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

