from city_country import city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("Enter a city name: ")
    if city == 'q':
        break
    country = input("Enter the city's country: ")
    if country == 'q':
        break
    formatted_name = city_country(city, country)
    print(f"\tNeatly formatted name: {formatted_name}.")