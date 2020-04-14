bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) #printing the whole list will also print the brackets 

print(bicycles[0].title()) #printing individual items from a list will NOT print brackets

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #calling -1 always return last item in a list. -2 return 2nd to the last, etc.

message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)
