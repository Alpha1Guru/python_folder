def delister(data):  #Takes any data type
    unilist=[]
    if type(data) == type([1,2,3]) or type(data) == type((1,2,3)):
        for char in data:
            if type(char)==type(1) or type(char)==type(1.0) or type(char)==type("1.0"):
                unilist.append(char)
            elif type(char) == type([1,2,3]) or type(char) == type((1,2,3)):
                char = list(char)
                unilist.extend(delister(char))
    return unilist 

alist=tuple([1,3,["car","her",[1,{"name":345},]],6,"t",[1,[2,[3]]]])
ulist=delister(alist)
print ("Universal list: ", ulist)