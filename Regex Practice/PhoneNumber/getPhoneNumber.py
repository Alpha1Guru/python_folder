from isPhoneNumber import isPhoneNumber as iPN

def getPhoneNumber(text: str) -> list:
    """Returns a list of phone numbers found in string"""
    return [text[i:i+12] for i in range(len(text)) if iPN(text[i:i+12])]
    
if __name__ == "__main__":
    def getPhoneNumber(text: str) -> list:
        for i in range(len(text)):
            chunk = text[i:i+12]
            if iPN(chunk):
                print(f"Phone number found: {chunk}")
        print("Done")
    text = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    getPhoneNumber(text)