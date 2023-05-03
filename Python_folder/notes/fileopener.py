filename = "Things_I_to_do.txt"
with open(filename) as file_object:
    content = file_object.read()
    print(content)


with open(filename) as file_object:
    for lines in file_object.readlines():
        print(lines.rstrip())
        
with open(filename) as file_object:
    list_of_lines = file_object.readlines()

#for line in list_of_lines:
#    print(line.rstrip())

sum=""
for line in list_of_lines:
    sum+=line.strip()
print(sum,"\n")
print(sum[:10])
print(len(sum),"\n")
