def longest(a1: str, a2: str) -> str:
    """Take 2 strings s1 and s2 
    including only letters from a to z. 
    Return a new sorted string, the longest possible, 
    containing distinct letters - each taken only once - coming from s1 or s2.

    Args:
        a1 (str): any string
        a2 (str): any string

    Returns:
        str: a new sorted string of distinct letters from adding a1 and a2
    """    
    longest_list = sorted(set(a1).union(set(a2)))
    longest_str = ""
    for char in longest_list:
        longest_str += str(char)
    return longest_str

def longest_by_someone(a1, a2):
    return "".join(sorted(set(a1 + a2)))

if __name__ == "__main__":
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a, b), longest(a, b) == "abcdefklmopqwxy")
    a = "abcdefghijklmnopqrstuvwxyz"
    print(longest(a, a), longest(a, a) == "abcdefghijklmnopqrstuvwxyz")