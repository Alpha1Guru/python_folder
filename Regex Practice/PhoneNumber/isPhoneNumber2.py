import re
phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
print(phone_regex)
mo = phone_regex.search('My number is 415-555-4242.')