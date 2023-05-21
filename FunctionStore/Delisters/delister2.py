def delister(data):  #Takes any data type
    def del_list(data):
        unilist=[]
        for char in data:
            if type(char)==type(1) or type(char)==type(1.0) or type(char)==type("1.0"):
                unilist.append(char)
            elif type(char) == type([1,2,3]) or type(char) == type((1,2,3)):
                char = list(char)
                unilist.extend(del_list(char))
            elif type(char) == type({"name":"python"}):
                for values in char.values():
                    unilist.extend(del_dict(values))
        return unilist     
    def del_dict(data):
        unilist =[]
        for char in data.values():
            if type(char)==type(1) or type(char)==type(1.0) or type(char)==type("1.0"):
                unilist.append(char)
            elif type(char) == type([1,2,3]) or type(char) == type((1,2,3)):
                char = list(char)
                unilist.extend(del_list(char))
            elif type(char) == type({"name":"python"}):
                for value in char.values():
                    unilist.extend(del_dict(value))

    if type(data) == type([1,2,3]) or type(data) == type((1,2,3)):
        return del_list(data)
    elif type(data) == type({"name":"python"}):
        return del_dict(data)
   
# alist=tuple([1,3,["car","her",[1,{"name":345},]],6,"t",[1,[2,[3]]]])
alist = {"name":'chiboy',"list":[1,["1",2,{"list":[13,3,3,3,3,3],"church":"Dominic","angel":"micheal","dict":{"list":[2,3,{"dict":{"school": "johtech"}}]}}]]}
for v in alist.values():
    print(v)
ulist=delister(alist)
print ("Universal list: ", ulist)