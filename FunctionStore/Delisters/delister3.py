#Bug the keys choice are 
#not so useful because of recursion 
def delister(data, choice=None):
    un_listed= []
    if isinstance(data, (str, int, float)):
         print("Data:", data)
         un_listed.append(data)
         print("Unlisted:", un_listed)
         print ("\n")

    elif isinstance(data, (list, tuple)):
         print("Data:", data)
         for elem in data:
             un_listed += delister(elem)
             print("Unlisted:", un_listed)

    elif isinstance(data, dict):
        if not choice:
            choice = "s"
        elif choice not in ("s", "k", "v", "sp","u"):
            raise ValueError()
        
        for key, value in data.items():
            if choice == "u":
                un_listed.append(data)
                break 
            if choice == "s":
                un_listed += delister(key) + delister(value)
            elif choice == "k":
                un_listed += delister(key)
            elif choice == "v":
                un_listed += delister(value)
            elif choice == "sp":
                un_listed.append({key:value})
    else:
        raise ValueError("Unacceptable Data type"
        "must be a  list, tuple, Dictionary")
    return un_listed
    

a_list = tuple([1,3,["car","her",[1,{"name":345},]],6,"t",[1,[2,[3]]]])
a_dict = {"name":'chiboy',"list":[1,["1",2,{(1,2,3):[13,3,3,3,3,3],"church":"Dominic","angel":"micheal","dict":{"list":[2,3,{"dict":{"school": "johtech"}}]}}]]}

print(a_dict)
print("\n")

u_list = delister(a_dict)
print("\n\n")

print ("Universal list: ", u_list)
print("\n\n")

print(a_dict)
#Dictionary not ready