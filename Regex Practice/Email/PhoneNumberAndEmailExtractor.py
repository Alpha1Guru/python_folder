#! python3
"""A program to extract phone number and email from clipboard"""

import re
test_string = """
800-420-7240
415-863-9900
415 893 9950
893-9950
415-893-9950x34"""
phone_regex = re.compile(r"""                    
    (?P<areacode>\d{3}|\(\d{3}\))?     # Area code (optional)
    (?P<separator>\s{0,1}|-)?           # separator (optional)
    (?P<firstdigits>\d{3})                 # first 3 digits
    (?P=separator)                   # separator
    (?P<lastdigits>\d{4})                 # last 4 digits
    (?P<extension>\s*(?:ext|x|ext.)\s*(?:\d{2,5}))?
    """, re.X)
phone_matches = phone_regex.finditer(test_string)

for match in phone_matches:
    print(match.group(), match.groups(), sep=" ", end="\n\n")

# email_regex = re.compile(r"""(?x: abay)""")
# print(email_regex.search("abay").group())
