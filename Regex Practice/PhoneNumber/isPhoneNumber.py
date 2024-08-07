def isPhoneNumber(number: str, delimiter = "-") -> bool:
    str(number)
    if len(number) != 12:
        return False
    if not number[:3].isdecimal():
        return False
    if not number[3] == delimiter:
        return False
    if not number[4:7].isdecimal():
        return False
    if not number[7] == delimiter:
        return False
    if not number[8:].isdecimal():
        return False
    return True
if __name__ == "__main__":
    print('Is 415-555-4242 a phone number?')
    print(isPhoneNumber('415-555-4242'))
    print('Is Moshi moshi a phone number?')
    print(isPhoneNumber('Moshi moshi'))
