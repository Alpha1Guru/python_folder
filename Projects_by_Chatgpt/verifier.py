#function to check for unwanted characters (non-number char)in text
def check_unwanted(decimal,float=True):
    if float == True:#by default treats the text as a float
        numbers = ".0123456789"
    elif float == False: # treats the text as an integer  
        numbers = "0123456789"
    unwanted = []
    points = 0
    
    #This code prevents the user from inputting nothing as an input
    if decimal=="":
        unwanted.append(True)
     
     # This code checks the number of decimal points  
    for i in range(len(decimal)):
        if decimal[i]==".":
            points +=1
     #This code is to prevent the occurrence of two decimal points       
    if points >1:
        unwanted.append(True)
                
    for i in range(len(decimal)):   
         if decimal[i] not in numbers : #prevents characters that are not numbers to be recognized
            unwanted.append(True)
         else:
            unwanted.append(False)#recognizes the rest
    return unwanted

def verifloat(decimal): #fuction verifies for correct float or decimal numbers
    result=check_unwanted(decimal) #checks the text in the check_unwanted func
    while True in result: #while the text failed the test
        if decimal == "":
            message = f"\nYou gave an EMPTY value!\tPlease I need a Decimal number: "
        elif decimal!= "":
            message = f"\n'{decimal}' is NOT A DECIMAL NUMBER!\tPlease enter a valid decimal number: "
        decimal=input(message) #it prompts user for a correct number
        result=check_unwanted(decimal) #checks the text again untill correct
    return decimal #returns the correct(ed) text

def verint(integer): #function verifies for correct integers only!
    result=check_unwanted(integer,float =False) #checks the text as an integer and not a float
    while True in result: #while the text failed the test
        if integer == "":
            message = f"\nYou gave an EMPTY value!\tPlease I need an Integer: "
        elif integer!= "":
            message = f"\n'{integer}' is NOT AN INTEGER!\tPlease I need an Integer: "
        integer=input(message) #it promts user for a correct integer
        result=check_unwanted(integer,float=False) #checks the text again untill correct
    return integer #returns the correctf(ed)text

# while True:
#    user = verifloat(input("Using Verifloat for float Give me a number: ").strip())
#    print(user)
#    user = verint(input("Using Verint for integer Give me a number: ").strip())
#    print(user)