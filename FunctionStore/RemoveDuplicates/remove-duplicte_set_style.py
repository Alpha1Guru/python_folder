def remove_duplicate(data):
    if isinstance(data, list): 
        return list(set(data))
    elif isinstance(data, str):
        return "".join(set(data))
    elif isinstance(data, tuple):
        return tuple(set(data))
text = str("111134441111666666555")
print(remove_duplicate(text))
