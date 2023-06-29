#function to check for unwanted characters (non-number char)in text
def check_unwanted(text,valid_chars=".-+0123456789", only_negative = False, only_positive = False):
    if text == "":#Prevents user from giving and empty string
        result = True # result becomes true if text is an empty string
        return result
    elif only_negative:
        for i in range(len(text)):# loops through the text 
            if text[i] in valid_chars and text.count(".") <= 1 and "+" not in text and text[0] == "-" and len(text) != 1 and "-" not in text[1:]: # if the character is in valid char, decimal point less than 2, absence of plus sign in text, minus sign MUST BE PRESENT - but at the firt position only (or not in any other position save the first)
                result = False # result is false for now
            else:
                result = True # result becomes True
                break #The loop breaks immediately when result becomes True
    elif only_positive:
        for i in range(len(text)): # loops through the text 
            if text[i] in valid_chars and text.count(".") <= 1 and "-" not in text and len(text) != 1 and "+" not in text[1:]: # if the character is in valid char, decimal point less than 2, absence of minus sign in text, plus sign MAYBE PRESENT - but only at the firt position (or not in any other position save the first)
                result = False # result is false for now
            else:
                result = True # result becomes True
                break #The loop breaks immediately when result becomes True
    else: # but if only_positive and only_negative are both false and the string is not empty then,
        for i in range(len(text)):# loops through the text 
            if text[i] in valid_chars and text.count(".") <= 1 and "+" not in text[1:] and "-" not in text[1:]: # if the character is in valid char, decimal point less than 2, minus and plus sign MAYBE PRESENT - but only at the firt position (or not in any other position save the first)
                result = False # result is false for now
            else: # if more than one decimal points or a non number character
                result = True # result becomes True
                break #The loop breaks immediately when result becomes True
        
    return result

def prompt(num,type):
    if num == "":
        message = f"\nYou gave an EMPTY value! Please I need a {type} number: "
    elif num != "":
        message = f"\n'{num}' is NOT A {type} number! Please I need a {type} number: "
    num = input(message)
    return num

def verFloat(decimal):  #fuction checks for correct float or decimal numbers
    result=check_unwanted(decimal) #checks the text in the check_unwanted func
    while result == True:
        decimal = prompt(decimal,"DECIMAL")
        result=check_unwanted(decimal)
    return decimal #returns the correct(ed) text

def verInt(integer): #function verifies for correct integers only!
    valid_chars="-+0123456789"
    result=check_unwanted(integer,valid_chars) #checks the text in the check_unwanted func
    while result == True:
        integer = prompt(integer,"INTEGER")
        result=check_unwanted(integer)
    return integer #returns the correct(ed) text

def verNegNum(NegNum):
    valid_chars="-.0123456789"
    result=check_unwanted(NegNum,valid_chars,only_negative=True) #checks the text as an integer and not a float
    while result == True:
        NegNum = prompt(NegNum,"NEGATIVE NUMBER")
        result=check_unwanted(NegNum,valid_chars,only_negative=True) #checks the text as an integer and not a float
    return NegNum #returns the correct(ed) text

def verPosNum(PosNum):
    valid_chars="+.0123456789"
    result=check_unwanted(PosNum,valid_chars,only_positive=True) #checks the text as an integer and not a float
    while result == True:
        PosNum = prompt(PosNum,"POSITIVE NUMBER")
        result=check_unwanted(PosNum,valid_chars,only_positive=True) #checks the text as an integer and not a float
    return PosNum #returns the correct(ed) text

def verNegInt(NegInt):
    valid_chars="-0123456789"
    result=check_unwanted(NegInt,valid_chars,only_negative=True) #checks the text as an integer and not a float
    while result == True:
        NegInt = prompt(NegInt,"NEGATIVE INTEGER")
        result=check_unwanted(NegInt,valid_chars,only_negative=True) #checks the text as an integer and not a float
    return NegInt #returns the correct(ed) text

def verPosInt(PosInt):
    valid_chars="+0123456789"
    result=check_unwanted(PosInt,valid_chars,only_positive=True) #checks the text as an integer and not a float
    while result == True:
        PosInt = prompt(PosInt,"POSITIVE INTEGER")
        result=check_unwanted(PosInt,valid_chars,only_positive=True) #checks the text as an integer and not a float
    return PosInt #returns the correct(ed) text

# while True:
#     user = verFloat(input("Using VerFloat to check float numbers: ").strip())
#     print(user,"is valid")
#     user = verInt(input("Using VerInt to check Onlyinteger numbers: ").strip())
#     print(user," is valid")
#     user = verNegNum(input("Using VerNegNum to check Only Negative Numbers: ").strip())
#     print(user,"is valid")
#     user = verPosNum(input("Using verPosNum to check Only Positive Numbers: "))
#     print(user,"is valid")
#     user = verNegInt(input("Using verNegInt to check Only Negative Integer: "))
#     print(user,"is valid")
#     user = verPosInt(input("Using verPosInt to check Only Positive Integer: "))
#     print(user,"is valid")