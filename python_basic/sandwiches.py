sandwich_orders = [
    'reuben', 'blt', 'hamburger', 'french dip', 'blt', 'philly cheesesteak',
    'pastrami', 'blt', 'reuben', 'pastrami', 'blt',
    ]
finished_sandwiches = []
print(sandwich_orders)

print("We are out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print(finished_sandwiches)