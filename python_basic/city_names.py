def city_country(city, country):
    if country.lower() == "usa":
        formatted_city = f"{city.title()}, {country.upper()}"
    else:
        formatted_city = f"{city.title()}, {country.title()}"
    return formatted_city

print("This program format your city names. Enter 'q' anytime to quit.")
while True:
    city = input("Input city name: ")
    if city == 'q': break
    country = input("Input country name: ")
    if country == 'q': break
    formatted_city = city_country(city, country)
    print(formatted_city)