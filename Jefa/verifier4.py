#function to check for unwanted characters (non-number char)in text
def check_unwanted(text,
                valid_chars=".-+0123456789",
                only_negative= False,
                empty_allowed= False,
                only_numbers=True,
                ):
    result = False
    # Prevents user from giving an empty string if empty values are invalid.
    if not text:
        if not empty_allowed:
            result = True  # result become True if empty values are invalid
        elif empty_allowed:
            result = False  # result become False if empty values are valid
        return result  # No need checking remaining characters
    
    # Result is equal true if the text passes any of the test.
    if only_numbers:
        if text == "-" or text == "+":
            result = True
        if text == ".":
            result = True
        if text.count(".") > 1: # test of number of decimal point
            result = True
        if "-" in text[1:] or "+" in text[1:]:
            result = True
        if only_negative: # if checking for a negative number
            if text[0] != "-": # first character is not a minus sign?
                result = True

    # Result equals true if an invalid character is found.
    for i in range(len(text)):
        if  not text[i] in valid_chars: 
            result = True
            break
    return result

def prompt(num,type):
    if num == "":
        message = f"\nYou gave an EMPTY value! Please I need {type}: "
    elif num != "":
        message = f"\n'{num}' are not {type} Please I need {type}: "
    num = input(message)
    return num

def verFloat(decimal):  #function checks for correct float or decimal numbers
    result=check_unwanted(decimal) #checks the text in the check_unwanted func
    while result == True:
        decimal = prompt(decimal,"DECIMALS")
        result=check_unwanted(decimal)
    return decimal #returns the correct(ed) text

def verInt(integer): #function verifies for correct integers only!
    valid_chars="-+0123456789"
    result=check_unwanted(integer,valid_chars) #checks the text in the check_unwanted func
    while result == True:
        integer = prompt(integer,"INTEGERS")
        result=check_unwanted(integer)
    return integer #returns the correct(ed) text

def verNegNum(NegNum):
    valid_chars="-.0123456789"
    result=check_unwanted(NegNum,valid_chars,only_negative=True) #checks the text as an integer and not a float
    while result == True:
        NegNum = prompt(NegNum,"NEGATIVE NUMBERS")
        result=check_unwanted(NegNum,valid_chars,only_negative=True) #checks the text as an integer and not a float
    return NegNum #returns the correct(ed) text

def verPosNum(PosNum):
    valid_chars="+.0123456789"
    result=check_unwanted(PosNum,valid_chars,) #checks the text as an integer and not a float
    while result == True:
        PosNum = prompt(PosNum,"POSITIVE NUMBERS")
        result=check_unwanted(PosNum,valid_chars,) #checks the text as an integer and not a float
    return PosNum #returns the correct(ed) text

def verNegInt(NegInt):
    valid_chars="-0123456789"
    result=check_unwanted(NegInt,valid_chars,only_negative=True) #checks the text as an integer and not a float
    while result == True:
        NegInt = prompt(NegInt,"NEGATIVE INTEGERS")
        result=check_unwanted(NegInt,valid_chars,only_negative=True) #checks the text as an integer and not a float
    return NegInt #returns the correct(ed) text

def verPosInt(PosInt):
    valid_chars="+0123456789"
    result=check_unwanted(PosInt, valid_chars) #checks the text as an integer and not a float
    while result == True:
        PosInt = prompt(PosInt,"POSITIVE INTEGERS")
        result=check_unwanted(PosInt, valid_chars) #checks the text as an integer and not a float
    return PosInt #returns the correct(ed) text

#Under construction will be fine in verifier5
import string 
def verEmpty(char, valid_chars= string.printable, message="All characters but not empty"):
    result= check_unwanted(char, valid_chars=valid_chars)
    while result == True:
        char = prompt(char, message)
        result = check_unwanted(char, valid_chars=valid_chars)
    return char

if __name__ == "__main__":
    while True:
    #     user = verFloat(input("Using VerFloat to check float numbers: ").strip())
    #     print(user,"is valid")
    #     user = verInt(input("Using VerInt to check Only integer numbers: ").strip())
    #     print(user," is valid")
    #     user = verNegNum(input("Using VerNegNum to check Only Negative Numbers: ").strip())
    #     print(user,"is valid")
    #     user = verPosNum(input("Using verPosNum to check Only Positive Numbers: "))
    #     print(user,"is valid")
    #     user = verNegInt(input("Using verNegInt to check Only Negative Integer: "))
    #     print(user,"is valid")
        # user = verPosInt(input("Using verPosInt to check Only Positive Integer: "))
        # print(user,"is valid")
        user = verEmpty(input("Using verEmpty to check for empty string: "))
        print(user,"is valid")