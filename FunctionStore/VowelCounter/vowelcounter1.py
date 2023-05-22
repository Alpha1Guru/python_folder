print("""Hello User!
      Welcome to the vowel detector""")
text = input("Give me a text: ")
vowels = ("a","e","i","o","u")
count = 0
for char in text :
    if char.lower() in vowels:
        count += 1
print(f"The number of vowels detected are: {count}")