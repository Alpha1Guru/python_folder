def delister(data):  #Takes any data type
    def del_list(data):
        un_listed=[]
        for elem in data:
            if isinstance(elem, (str, int, float)):
                un_listed.append(elem)
            elif (data, (list, tuple)):
                elem = list(elem)
                un_listed.extend(del_list(elem))
            # elif isinstance(elem, dict):
            #     un_listed.extend(del_dict)
        return un_listed     
    # def del_dict(data):
    #     un_listed =[]
    #     for key, value in data.items():
    #         if isinstance(data[key], (str, int, float)) :
    #             un_listed.append(data[key])
    #         elif isinstance(data[key], (list, tuple)):
    #             char = list(data[key])
    #             un_listed.extend(del_list(data[key]))
    #         # elif isinstance(data[key], dict):
    #         #     un_listed.extend(del_dict(data[key]))
    #     return un_listed

    if isinstance(data, (list, tuple)):
        return del_list(data)
    # elif isinstance(data, dict):
    #     return del_dict(data)
   
a_list = tuple([1,3,["car","her",[1,{"name":345},]],6,"t",[1,[2,[3]]]])
# a_dict = {"name":'chiboy',"list":[1,["1",2,{"list":[13,3,3,3,3,3],"church":"Dominic","angel":"micheal","dict":{"list":[2,3,{"dict":{"school": "johtech"}}]}}]]}
print(a_list)
u_list = delister(a_list)
print ("Universal list: ", u_list)
#Dictionary not ready