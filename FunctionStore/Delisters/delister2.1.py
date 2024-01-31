#Bug fixed: Dictionary still being 
#delisted in the del_list function 
def delister(data): 
    def del_list(data):
        un_listed=[]
        for elem in data:
            print("Element:", elem, type(elem))
            if isinstance(elem, (str, int, float)):
                un_listed.append(elem)
                print("Unlisted:", un_listed)
                print ("\n")
            elif isinstance(elem, (list, tuple)):
                un_listed += del_list(list(elem))
                print("Unlisted:", un_listed)
                print("\n")
            elif isinstance(elem, dict):
                continue 
        return un_listed

    if isinstance(data, (list, tuple)):
        return del_list(data)
    else:
        raise ValueError("This is not a list")
   
a_list = tuple([1,3,["car","her",[1,{"name":345},]],6,"t",[1,[2,[3]]]])
a_dict = {"name":'chiboy',"list":[1,["1",2,{"list":[13,3,3,3,3,3],"church":"Dominic","angel":"micheal","dict":{"list":[2,3,{"dict":{"school": "johtech"}}]}}]]}
print(a_dict)
print("\n")
u_list = delister(a_dict)
print ("Universal list: ", u_list)
#Dictionary not ready