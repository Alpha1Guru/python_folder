import string
from verifier3d import check_unwanted
def getNames(names: str):
    names: str = names.strip()
    is_titled = names.istitle()
    if not is_titled:
        return None
    valid_chars: str = string.ascii_letters + string.whitespace + string.digits
    check = check_unwanted(names, valid_chars=valid_chars,)
    if  check:
        return None
    name_fragments: list = names.split()
    print(name_fragments)
    dict_name: dict = {}
    if len(name_fragments) >= 1:
        first_name = name_fragments[0]
        dict_name["first"] = first_name
    if len(name_fragments) >= 2:
        last_name = name_fragments[1]
        dict_name["last"] = last_name
    if len(name_fragments) > 2:
        other_names = set(name for name in name_fragments[2:])
        dict_name["others"] = other_names
    return dict_name
if __name__ == "__main__":
    while True:
        print(getNames(input("Give me a name: "))) 