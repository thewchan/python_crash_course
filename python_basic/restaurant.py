class Restaurant:
    """Simulate a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initiate restaurant instance with name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print restaurant information."""
        print(f"Welcome to {self.restaurant_name.title()}!")
        print(f"We serve {self.cuisine_type.title()} cuisine here.")
    
    def open_restaurant(self):
        """Print that this restaurant is opened"""
        print(f"The {self.restaurant_name.title()} is open!")
        
    def set_number_served(self, num):
        """Set the number_servevd attribute to input num"""
        self.number_served = num
        
    def increment_number_served(self, inc):
        """Increment number_served attribute by input inc"""
        self.number_served += inc

class IceCreamStand(Restaurant):
    """A child class of class Restaurant that represents an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize IceCreamStand with attributes of class Restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def show_flavors(self):
        """
        Print a list of the current flavors the ice cream stand is serving.
        """
        print("The current ice cream flavors are:")
        for flavor in self.flavors:
            print(f"- {flavor}")
                
pizza = Restaurant('my favoirte pizza place', 'italian')
print(pizza.restaurant_name)
print(pizza.cuisine_type)
pizza.describe_restaurant()
pizza.open_restaurant()

panda = Restaurant('panda express', 'chinese')
print('\n' + panda.restaurant_name)
print(panda.cuisine_type)
panda.describe_restaurant()
panda.open_restaurant()

taco = Restaurant('taco town', 'mexican')
print('\n' + taco.restaurant_name)
print(taco.cuisine_type)
taco.describe_restaurant()
taco.open_restaurant()

restaurant = Restaurant('new restaurant', 'new')
print(restaurant.number_served)
restaurant.set_number_served(4)
print(restaurant.number_served)
restaurant.increment_number_served(7)
print(restaurant.number_served)

current_flavors = ['vanilla', 'chocolate', 'straberry']
ice_cream = IceCreamStand(
        'my favorite ice cream stand', 'ice cream', current_flavors
        )
ice_cream.show_flavors()