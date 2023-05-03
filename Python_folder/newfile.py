source_file="/data/user/0/ru.iiec.pydroid3/app_HOME/Function_Maker/string_function/string_1.py"
target_file="/storage/emulated/0/Python_folder/Function_Maker/string_function/string_1.py"
#To read from source file and copy contents to a variable
with open(source_file) as file_object:
    source_content=file_object.read()
    
# creates a new file called the target file as writes the content of the source file to the target file
with open(target_file,'w') as file_object:
    file_object.write(source_content)
 
       
#To verify that change

#read the contents of the target file
with open(target_file) as file_object:
    target_content= file_object.read()
    
## The display both files
print("Source file: %s\n\n%s\n\n"%(source_file , source_content) )
print("Target file: %s\n\n%s\n\n"%(target_file , target_content) )