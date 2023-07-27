def longest(a1, a2):
    longest_list = sorted(set(a1).union(set(a2)))
    longest_str = ""
    for char in longest_list:
    #     longest_str += str(char)
    # return longest_str
        yield str(char)


if __name__ == "__main__":
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    print(longest(a, b), longest(a, b) == "abcdefklmopqwxy")
    a = "abcdefghijklmnopqrstuvwxyz"
    print(longest(a, a), longest(a, a) == "abcdefghijklmnopqrstuvwxyz")
    
    