# Function to convert list,float,string,integer to string
# The str() function cannot convert a list directly to a string this function does that
def stringer(data):  #Takes any data type
    string=""
    if type(data)==type(1) or type(data)==type(1.0) or type(data)==type("1.0") :
        string+=str(data)
        
    elif type(data) == type([1,2,3]) or type(data) == type((1,2,3)):
        for char in data:
            if type(char)==type(1) or type(char)==type(1.0) or type(char)==type("1.0"):
                string += str(char)
            elif type(char) == type([1,2,3]) or type(char) == type((1,2,3)) :
                string += stringer(char)
    return string 
#while True:
#    list=[1,3,6,"t",["car"],[1,[2,[3]]]]
#    list=stringer(list)
#    print ("Your list in string ",list)