import re

num = float
def m_to_km(mile: num) -> num:
    return mile*1.609344

if __name__ == "__main__":
    while True:
        mile = input("Enter Distance miles: ")
        while not mile.isdecimal():
            print("Numbers only")
            mile = input("Enter Distance miles: ")
        print(m_to_km(int(mile)))