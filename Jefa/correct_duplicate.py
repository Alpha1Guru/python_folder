
def correct_duplicate(data, list_: list, message: str):
    """Asks again for a data if already in the list provided

    Args:
        data (Any): _description_
        list_ (list): list of something
        message (str, optional): Displayed if the data given already exist. Defaults to None.

    Returns:
        Any: returns a data that is not in the list provided
    """    
    if  data in list_:
        data = input(f"{message}: " or "you have typed that before: ")
        correct_duplicate(data, list_, message)
    return  data

if __name__ == "__main__":
    basket = []
    while True:
        new_food = correct_duplicate(input("Add a food you love in the basket: ").lower(), basket, message="Sorry!!, thats already in the basket")
        basket.append(new_food)
        print(basket)