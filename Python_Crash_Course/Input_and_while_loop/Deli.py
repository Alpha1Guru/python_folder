print("Sorry we are out Turkey\n")
food_orders = ["fufu","egosi soup","potato","turkey","turkey","catfish","pepper soup","turkey","insala soup","fried rice","turkey","turkey",]
finished_orders = []
while "turkey" in food_orders:
    food_orders.remove("turkey")
while food_orders:
    current_food = food_orders.pop()
    print("Making you  your " + current_food + " ...")
    finished_orders.append(current_food)
print("\nYour orders are ready!\n")
for order in finished_orders:
    print("Enjoy your " + order + ".")