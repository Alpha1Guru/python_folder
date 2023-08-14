def solution(text: str):
    splitted_string: list = []
    
    if len(text)%2 != 0:
        text = text + "_" 
        
    for i in range(0, len(text), 2):
        splitted_string.append(str(text[i] + text[i+1]))
    return splitted_string

def solution(s):
    """I think it uses the fact that when counting in two's if the number is
    an odd number the last number will be the last value (s[-1] or len(s) - 1)while if it is even 
    the number next to the last will be the last value e.g"""
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

if __name__ == "__main__":
    while True:
        user = input("Give some text: ")
        print(solution(user))