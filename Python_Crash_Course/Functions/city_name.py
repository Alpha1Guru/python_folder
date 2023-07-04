def city_country(city_name,country_name= "Nigeria"):

    formatted = city_name.title() + "," + " " + country_name.title()

    print(formatted)

city_country("Lagos")

city_country("Chicago","United States")

city_country(city_name="Morocco",country_name="india")