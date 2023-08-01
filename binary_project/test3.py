
def check_unwanted(decimal):
    numbers = "0123456789"
    unwanted = []
    sum=0
    
    #This code prevents the user from inputting nothing as an input
    if decimal=="":
        unwanted.append(True)
     
     # This code checks the number of decimal points  
    for i in range(len(decimal)):
        if decimal[i]==".":
            sum+=1
     #This code is to prevent the occurrence of two decimal points       
    if sum>1:
        unwanted.append(True)
                
    for i in range(len(decimal)):
        
        #prevents the occurrence of decimal points in the beginning and end
        
        # if (i != 0 or i != len(decimal) -1) and decimal[i] =="." :
        ##   The code stated above does not really prevent the occurrence of decimal point in a number but still works   
        ## The code above does not really make a difference as it still works like -- if decimal[i] =="." :  
        ## This is because if i ==0 ( that is in the beginning but not in the end) the condition still will be fullfilled because i is not equal to the last number
        ## So also if i==len(decimal-1) the condition will still be fullfilled because i is not equal to 0 that is the first number
        ##All this happen because of the or operator. The fulfillment of one condition (Truth value of true) inspite of the  unfulfilled condition (Truth value of false) will still lead to the execution of  the code
        ##However
        #  if (i != 0 and i != len(decimal) -1) and decimal[i] =="." :  if (i != 0 and i != len(decimal) -1) and decimal[i] =="." :
        ##The code stated below actually prevents the occurrence of decimal point in the beginning or end of a number
        ##This is because both conditions must be fullfilled before the code can execute
        #The and operator mkes sure that i is not equal to 0 (that i is the beginning)   and i is not equal to len(decimal)-1 before executing the next line
         # that is the decimal point can be recognized if it does not appear at the beginning or end of a number
       
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
 
    
while  True :
    decimal =str(float(verify(input("Give me a float  " ))))
    
    #code to split  the number into integer and fraction
    decimal_point_index = decimal.index(".")
    integer = decimal[:decimal_point_index]
    fraction ="0" + decimal[decimal_point_index:]
    
    
    print(decimal)
    print(integer)
    print(fraction)

    