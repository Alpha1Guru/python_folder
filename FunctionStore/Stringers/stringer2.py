# Function to convert list,float,string,integer to string
def stringer(data):
    string = ""   
    if isinstance(data, (str, int)):
        string = str(data)
    elif isinstance(data, (tuple, list)):
        for char in data:
            string += stringer(char)
    return string 

list_=[1,3,6,"t",["car"],[1,[2,[3]]]]
list_=stringer(list_)
print("Your list in string form:", list_, )

