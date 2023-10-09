def fibo(num):
    fibo = []
    a,b = 0, 1
    while a < num:
        fibo.append(a)
        a, b = b , a+b
    return fibo
if __name__ == "__main__":
    print(fibo(10))