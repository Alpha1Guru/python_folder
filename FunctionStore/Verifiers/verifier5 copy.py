"""Docstring by Chatgpt"""
import string
from typing import Tuple

class verify:
    """
    checks an string of text for unwanted characters
    """
    def __init__(
            self,
            text,
            numbers=True,
            decimal=True,
            only_positive=False,
            only_negative=False,
            empty_allowed=False,
            letters=False,          
            punctuation = False,
            whitespace=False,
            invalid_message: Tuple[str,str]=None,
            ignore: Tuple[str, ...] = None,
            remove: Tuple[str, ...] = None,
            len: set = None,):
        pass
      
    def check_unwanted(text,
                valid_chars=".-+0123456789",
                only_negative= False,
                empty_allowed= False,
                only_numbers=True,
                ) -> bool:
        
    
        # Prevents user from giving an empty string if empty values are invalid.
        if not text:
            if not empty_allowed:
                return True  # returns True if empty values are invalid
            elif empty_allowed:
                return False  # returns False if empty values are valid
        # No need checking remaining characters
        
        # Returns True if the text passes any of the test.
        if only_numbers:
            if text == "-" or text == "+":
                return True
            if text == ".":
                return True
            if text.count(".") > 1: # test of number of decimal point
                return True
            if "-" in text[1:] or "+" in text[1:]:
                return True
            if only_negative: # if checking for a negative number
                if text[0] != "-": # first character is not a minus sign?
                    return True

        # Returns true if an invalid character is found.
        for i in range(len(text)):
            if  not text[i] in valid_chars: 
                return True
                break
        return False

    def prompt(text: str, type_text: str,
            invalid_message: Tuple[str,str] = None, 
            empty_allowed=False) -> str:
        if not text and not empty_allowed:
            if invalid_message:
                message = f"\n{invalid_message[0]}: "
            elif not invalid_message:    
                message = (f"\nYou gave an EMPTY value!"
                        f"\nPlease I need a {type_text.upper()}: ")
        elif text:
            if invalid_message:
                message = f"\n{invalid_message[1]}: "
            elif not invalid_message:
                message = (f"\n'{text}' is NOT A {type_text.upper()}!"
                        f"\nPlease I need a {type_text.upper()}: ")
        text = input(message)
        return text

    def verify(text,
            numbers=True,
            decimal=True,
            only_positive=False,
            only_negative=False,
            empty_allowed=False,
            letters=False,          
            punctuation = False,
            whitespace=False,
            invalid_message: Tuple[str,str]=None,
            ignore: Tuple[str, ...] = None,
            remove: Tuple[str, ...] = None,
            len: set = None,
            ):

        if not letters and not numbers and not punctuation: 
            numbers = True  # should have raised an error instead, coming soon ...
            pass
        
        # if min_len is not None or max_len:
        #     if max_len < 1:
        #         pass # Will have to raise error
        #     if min_len < 1:
        #         pass # Will have to raise error

        if letters or punctuation or whitespace:
            only_numbers = False
        else:
            only_numbers = True
        
        def get_valid_char_and_type(ignore):
            type_text = ""
            valid_char = ""
            if ignore:
                for char in ignore:
                    valid_char += str(char)

            if numbers:
                valid_char += string.digits
                if only_positive:
                    valid_char += "+"
                    type_text = "positive"
                elif only_negative:
                    valid_char += "-"
                    type_text = "negative"
                elif not only_negative and not only_positive:
                    valid_char += "-+"
                    type_text = ""
                if decimal:
                    valid_char += "."
                    type_text += " decimal"
                elif not decimal:
                    type_text += " integer"
                type_text += " number"

            if letters:
                valid_char += string.ascii_letters
                type_text = "letter (s)"

            if punctuation:
                valid_char += string.punctuation 

            if numbers and letters or punctuation :
                type_text = "valid character(s)"
                          
            if remove is not None:
                for char in valid_char:
                    if char in remove:
                        valid_char = valid_char.replace(char,"")
            
            return (valid_char, type_text)
        
        valid_char_type_text = get_valid_char_and_type(ignore)
        print(valid_char_type_text)
        result=check_unwanted(text,valid_char_type_text[0],
                            only_negative=only_negative,
                            empty_allowed=empty_allowed,
                            only_numbers=only_numbers,)
        while result == True:
            text = prompt(text, 
                        valid_char_type_text[1], 
                        empty_allowed=empty_allowed,
                        invalid_message=invalid_message)
            result=check_unwanted(text,valid_char_type_text[0],
                            only_negative=only_negative,
                            empty_allowed=empty_allowed,
                            only_numbers=only_numbers)
        return text

verInt = verify
verFloat = verify
verNegNum = verify
verPosNum = verify
verNegInt = verify
verPosInt = verify
verAlpha = verify
verPunc = verify
verAlphaNum = verify
verChar = verify

if __name__ == "__main__":
    while True:
        # user = verFloat(
        #     input("Using VerInt to check Only Float numbers: ").strip(),
        #     decimal=True)
        # print(("empty" if not user else user) ,"is valid")

        # user = verInt(
        #     input("Using VerInt to check Only integer numbers: ").strip(),
        #     decimal=False)
        # print(("empty" if not user else user) ,"is valid")

        # user = verNegNum(
        #     input("Using VerNegNum to check Only Negative Numbers: ").strip(),
        #     decimal=True, only_negative=True)
        # print(("empty" if not user else user) ,"is valid")

        # user = verPosNum(
        #     input("Using verPosNum to check Only Positive Numbers: ").strip(),
        #     decimal=True, only_positive=True)
        # print(("empty" if not user else user) ,"is valid")

        # user = verNegInt(
        #     input("Using verNegInt to check Only Negative Integer: "),
        #     only_negative=True, decimal=False, 
        #     invalid_message= ("Come on, You didn't give a value!",
        #                       "Come on, a Negative Integer!"))
        # print(("empty" if not user else user) ,"is valid")

        # user = verAlpha(
        #         input("Using verAlpha to check Only letters: "),
        #         letters=True, empty_allowed=False, 
        #         numbers=False,
        #         invalid_message=(
            #         "No Not an empty value!",
        #             "Your input contain invalid characters that are not letters"
        #               ),
        #         ignore=(".",",","!"," ")
        #         )
        # print(("empty" if not user else user) ,"is valid")

        # user = verPunc(
        #     input("Using verPosInt to check Only Punctuations: "),
        #     decimal=False, empty_allowed=True,
        #     punctuation=True, numbers=False, ignore=" "
        #     )
        # print(("empty" if not user else user) ,"is valid")
        
        # user = verChar(
        #     input("Using verChar to check All characters (Nothing really!!): "),
        #     invalid_message=("No empty value please", "How can you be wrong?!"),
        #     remove=("a"))
        # print(("empty" if not user else user) ,"is valid") 
        

        
    # PROBLEMS:
    # ---------
    # # Zero problem is -0 negative? or +0 positive?

    ## No Error was raise when both letters and numbers are equal to false.
    ## It defaulted to numbers instead 
    # user = verAlpha( 
    #             input("Using verAlpha to check Only letters: "),
    #         ->  letters=False, empty_allowed=False, 
    #         ->  numbers=False,
    #             invalid_message=("No Not an empty value!",
    #                     "Your input contain invalid characters that are not letters"
    #                     )
    #             )
    # print(("empty" if not user else user) ,"is valid")