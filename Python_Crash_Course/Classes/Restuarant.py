class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.active = True
        self.open_time = ""
        self.close_time = ""

    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name}")
        Print(f"Cuisine_type: {self.cuisine_type}")

    # def is_active(self):
    #     return self.active    
    def isOpen(self):
        if self.active:
            print("This restaurant is open")
        else:
            print("This restaurant is close")

fav_restaurant = Restaurant("MariGolden","Soup")
fav_restaurant.isOpen()
fav_restaurant.active = False
fav_restaurant.isOpen()