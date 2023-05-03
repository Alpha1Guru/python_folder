countries = ["canada","usa","rome","china","japan","korea","france","dubai"]
print("Before change: ",countries)
print("Sorted: ",sorted(countries))
print("After sorted: ",countries)

# print("Reversing using the reversed function")
# reversed = reversed(countries)
# print(reversed)
# print("After reversed function: ", countries)

print("Reversing using the reverse method")
countries.reverse()
print("After reversed method: ",countries)

print("Reversing using the reverse method again")
countries.reverse()
print("After reversed method again: ",countries)

print("Using the sorted method: ")
countries.sort()
print("After sorted method: ", countries)