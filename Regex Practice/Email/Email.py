#! python3.

import re

# urls = """
# http://python-engineer.com
# http://www.pyeng.net
# """
# pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.\w+)")
# matches = pattern.finditer(urls)
# for match in matches: print(match)

test_string = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.com
https://www.pyeng.net"""

pattern = re.compile(r"(https?):/{2}(www.)?([a-zA-z-]+)(\.[a-zA-z]+)")

print("Finditer:")
matches = pattern.finditer(test_string)   
for match in matches:
    print(match.groups())
subbed_urls = pattern.sub(r"\3\4",test_string)
print(subbed_urls)
print("\nFindall:")
list_of_matches = pattern.findall(test_string)
print(list_of_matches)
for match in list_of_matches:
    print(match)

# print("\nMatch:")
# mat = pattern.match(test_string)
# print(mat)

# print("\nSearch:")
# ser = pattern.search(test_string)
# print(ser)
# print(ser.groups())