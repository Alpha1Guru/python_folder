
#code to covert float number decimal to binary
def check_unwanted(decimal):
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
         if (i != 0 and i != len(decimal) -1) and decimal[i] =="." :
            unwanted.append(False)
         elif decimal[i] not in numbers : #prevents characters that are not numbers to be recognized
            unwanted.append(True)
         else:
            unwanted.append(False)#recognizes the rest
    return unwanted

def verify(decimal):
    result=check_unwanted(decimal)
    while True in result:
        print("not a number")
        decimal=input("give me a decimal: ")
        result=check_unwanted(decimal)
    return decimal

#while True:
#    user = verify(input("Give me a number: "))
#    print(user)