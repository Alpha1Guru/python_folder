print("""Hello User!
Welcome to the vowel detector""")
def vowel_counter(text):
    vowels = ("a","e","i","o","u")
    count = 0
    for char in text :
        if char.lower() in vowels:
            count += 1
    return count
user_text = input("Give me a text: ")

print(f"The number of vowels detected are: {vowel_counter(user_text)}")