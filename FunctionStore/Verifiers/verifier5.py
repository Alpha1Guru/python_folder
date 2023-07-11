"""Docstring by Chatgpt"""
import string
class verify:
    pass
def check_unwanted(text,
                   valid_chars=".-+0123456789",
                   only_negative= False,
                   only_positive= False,
                   empty_allowed= False,
                   only_numbers=True):
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
        elif text.count(".") > 1: # test of number of decimal point
            result = True
        elif only_negative: # if checking for a negative number
            if text[0] != "-": # first character is not a minus sign?
                result = True
        elif "-" in text[1:] or "+" in text[1:]:
            result = True
        return result
    else:
        # Result equals true if an invalid character is found.
        for i in range(len(text)):
            if  not text[i] in valid_chars: 
                result = True
                break
    return result

def prompt(text, type, empty_allowed=False):
    if not text and not empty_allowed:
        message = (f"\nYou gave an EMPTY value! "
                   f"Please I need a {type}: ")
    else :
        message = (f"\n'{text}' is NOT A {type}!"
                   f" Please I need a {type}: ")
    text = input(message)
    return num

def verify(text,
           numbers=True,
           decimal=True,
           only_positive=False,
           only_negative=False,
           empty_allowed=False,
           letters=False,          
           punctuation = False,
           ignore=None):
    if not ignore:
        ignore = ()

    if not letters and not numbers and not punctuation: 
        numbers = True  # should have raised error coming up
    if letters or punctuation:
        only_numbers = False
    def get_valid_char_and_type(ignore,):
        pass
    type = ""
    valid_char = set(ignore)
    if numbers:
        valid_char.add(set(string.digits))
        if only_positive:
            valid_char.add("+")
            type = "positive"
        elif only_negative:
            valid_char.add("-")
            type = "negative"
        elif not only_negative and not only_positive:
            valid_char.add(set("-+"))
            type = ""
        if decimal:
            valid_char.add(".")
            type += " decimal"
        elif not decimal:
            type += " integer"
        type += " number"

    if letters:
        valid_char.add(set(string.ascii_letters))
        type = "letters"

    if punctuation:
        valid_char.add(set(string.punctuation))
        type = "punctuation"

    if numbers and letters:
        type = "characters"
    result=check_unwanted(text,valid_chars,
                          only_negative=only_negative,
                          empty_allowed=empty_allowed,
                          only_numbers=only_numbers)
    while result == True:
        text = prompt(text, type, empty_allowed=empty_allowed)
        result=check_unwanted(text)
    return text #returns the correct(ed) text
# verInt = def verify() 

# while True:
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
    # print(("empty" if not user else user) ,"is valid")