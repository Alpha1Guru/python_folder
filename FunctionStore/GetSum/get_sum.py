def get_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(num for num in range(a, b+1))
print(get_sum(0, -1))

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) / 2
print(get_sum(0, -1))
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
print(get_sum(0, -1))
def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))
print(get_sum(0, -1))