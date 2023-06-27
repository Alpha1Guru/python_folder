#function to check for unwanted characters (non-number char)in text
def check_unwanted(text,valid_chars=".-+0123456789", negative = True,positive = True):
    if text == "":#Prevents user from giving and empty string
        result = True # result becomes true if text is an empty string
        return result
    
    elif text != "":# but if text is not an empty string
        if (positive and text.count("+") <= 1 and "+" not in text[1:]) or (negative and text.count("-") <= 1 and "-" not in text[1:]):
            for i in range(len(text)):# loops through the text 
                if text[i] in valid_chars and text.count(".") <= 1:# if the character is a number and decimal points are no more than one
                    result = False # result is false for now
                else: # if more than one decimal points or a non number character
                    result = True # result becomes True
                    break #The loop breaks immediately when result becomes True
        else:
            result = True
        return result

def verFloat(decimal):  #fuction verifies for correct float or decimal numbers
    result=check_unwanted(decimal) #checks the text in the check_unwanted func
    while result == True: # while the text failed the test
        if decimal == "":
            message = f"\nYou gave an EMPTY value!\tPlease I need a Decimal number: "
        elif decimal!= "":
            message = f"\n'{decimal}' is NOT A DECIMAL number!\tPlease I need a Decimal number: "
        decimal=input(message) #it prompts user for a correct number
        result=check_unwanted(decimal) #checks the text again untill correct
    return decimal #returns the correct(ed) text

def verInt(integer): #function verifies for correct integers only!
    valid_chars="-+0123456789"
    result=check_unwanted(integer,valid_chars) #checks the text as an integer and not a float
    while result == True: # while the text failed the test
        if integer == "":
            message = f"\nYou gave an EMPTY value!\tPlease I need an Integer: "
        elif integer!= "":
            message = f"\n'{integer}' is NOT AN INTEGER!\tPlease I need an Integer: "
        integer=input(message) #it promts user for a correct integer
        result=check_unwanted(integer,valid_chars) #checks the text again untill correct
    return integer #returns the correct(ed) text

def verNegNum():
    pass
while True:
   user = verFloat(input("Using Verifloat for float Give me a number: ").strip())
   print(user)
   user = verInt(input("Using Verint for integer Give me a number: ").strip())
   print(user)