def check_unwanted(text):
    numbers = ".0123456789"
    points = 0
    for i in range(len(text)):
        if text[i]==".":
            points+=1
    for i in range(len(text)):
        if text[i] in numbers and points <= 1:
           result = False
        else:
           result = True
        if result == True:
            break
    return result

def verify(text):
    result=check_unwanted(text)
    while result == True:
        print("not a number")
        text = input("Give me a number: ")
        result=check_unwanted(text)
    return text

#while True:
#    user = verify(input("Give me a number: "))
#    print(user)