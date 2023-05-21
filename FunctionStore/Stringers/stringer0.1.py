# Function to convert list,float,string,integer to string
def string(datatype):  #Takes any data type
    string=""
    try:
        if datatype/1==datatype:
                string+=str(datatype)
    except TypeError:
            for char in datatype:
                string+=str(char)
    return string
    
while True:
    data=string(input("give me a data :. "))
    print("Your data ",data)
    
    list=[1,3,6,"t",["car"]]
    list=string(list)
    print ("Your list in string ",list)