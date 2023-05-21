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
    data=string(input