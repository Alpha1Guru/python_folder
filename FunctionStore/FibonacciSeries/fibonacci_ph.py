def fibonacci(num):
    """Accept a number(length) and generates Fibonacci numbers up to that length"""
    fibo =[0,1]
    i = 2 
    #while i <= num:
    while i < num:
        next_fibo = fibo[i-1] + fibo[i-2]
        fibo.append(next_fibo)
        i +=1
    return fibo
print(fibonacci(10))