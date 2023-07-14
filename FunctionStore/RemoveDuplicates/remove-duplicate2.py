def remove_duplicate(data):
    def rm_dp_list(list_):
        unique = []
        for x in list_:
            if x not in unique:
                unique.append(x)
        return unique
    def rm_dp_str(str_):
        unique = str_[::-1]
        for char in unique:
            if unique.count(char) > 1:
                unique = unique.replace(char, "", unique.count(char)-1)
        return unique[::-1]

    if isinstance(data, list): 
        return rm_dp_list(data)
    elif isinstance(data, str):
        return rm_dp_str(data)
    elif isinstance(data, tuple):
        new_data = list(data)
        return tuple(rm_dp_list(new_data))
text = str("111134441111666666555")
print(remove_duplicate(text))