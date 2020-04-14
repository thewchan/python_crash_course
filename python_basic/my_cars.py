import car_class

my_beetle = car_class.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car_class.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())