def fibonacci(num):
    fibo_list = []
    a , b =  0, 1
    while a < num:
        fibo_list.append(a)
        a, b = b, b+a
    return fibo_list

if __name__ == "__main__":
    while True:
       print(fibonacci(int(input("Give me a number: "))))