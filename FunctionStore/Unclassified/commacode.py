"""Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument
and returns a string with all the items separated by a 
comma and a space, with and inserted before the last
item. For example, passing the previous spam list to the 
function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to 
work with any list value passed to it."""

#No 2
# def commacode(list_of_words):
#     return "" if len(list_of_words) == 0 else (", ".join(list_of_words[:-1]) + " and " + list_of_words[-1] if len(list_of_words) > 1 else list_of_words[0])

#No 3
def commacode(list_of_words):
    return ", ".join(list_of_words[:-1]) + f" and {list_of_words[-1]}" if len(list_of_words)> 1 else "".join(list_of_words)

#NO 1
# def commacode(list_of_words: list):
#     if len(list_of_words) > 1:
#         comma_spaced = ", ".join(list_of_words[:-1]) + " and " +list_of_words[-1]
#     elif len(list_of_words) == 1:
#         comma_spaced = list_of_words[0]
#     else: #It is empty
#         comma_spaced = ""
#     return comma_spaced
print(commacode(["fruits","vegtables","nothing",]))

print((lambda list_of_words: "" if len(list_of_words) == 0 else (", ".join(list_of_words[:-1]) + " and " + list_of_words[-1] if len(list_of_words) > 1 else list_of_words[0]))(["fruits","vegetables","nothing","something","don't", "car"]))
