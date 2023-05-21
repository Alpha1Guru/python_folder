filename="fileopener_what_i_learnt.py"

with open(filename) as file_object:
    content=file_object.read()
    print(content+"\n")
 
#with open(filename) as file_object:   
#    for line in file_object.readlines():
#        print(line)
#    list_of_lines = file_object.readlines()

#sum=""
#for line in list_of_lines:
#    sum+=line.strip()
#    print(sum)
