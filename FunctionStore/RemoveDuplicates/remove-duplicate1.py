def remove_duplicate(data): 
    def rm_dp_list(list):    
        unique=[]
        for x in list:
            if x not in unique:
                unique.append(x)
        return unique   
    def rm_dp_str(str):
        def count_char(cha,string):
            count = 0
            for x in string:
                if cha == x:
                    count+=1     
            return count       
        unique=str[::-1]
        character = []
        for char in unique:
            if char not in character:
                character.append(char)
                if count_char(char,unique)>1:
                    unique = unique.replace(char,"",count_char(char,unique)-1)
        return unique[::-1]
    if type(data)== type([1,2,3]): 
        return rm_dp_list(data)
    elif type(data)==type("str"):
        return rm_dp_str(data)
    elif type(data)==type((1,2,3)):
        new_data = list(data)   
        return tuple(rm_dp_list(new_data))
text = tuple("111134441111666666555")
print(remove_duplicate(text))