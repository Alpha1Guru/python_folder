num = float
def cel_to_fah(degrees_in_celsius: num) -> num :
    """Converts degree Celsius to Fahrenheit"""
    num = (degrees_in_celsius*9)/5
    return num

if __name__ == "__main__":
    while True:
        degree_celsius = input("Temperature in degree celsius:\n")
        while not degree_celsius.isdecimal():
            print("Numbers only")
            degree_celsius = input("Temperature in degree celsius:\n")

        print(cel_to_fah(int(degree_celsius)))