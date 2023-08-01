source_file="/data/user/0/ru.iiec.pydroid3/app_HOME/saverfile.py"
target_file="/storage/emulated/0/Python_folder/saverfile.py"
#To read from source file and copy contents to a variable
with open(source_file) as file_object:
    source_content=file_object.read()

#To read from the target file before any change was made
with open(target_file) as file_object:
    first_form_of_target_file = file_object.read()
# Overwrites the content of the source file to the target file
with open(target_file,'w') as file_object:
    file_object.write(source_content)
 
       
#To verify that change

#read the contents of the target file
with open(target_file) as file_object:
    target_content= file_object.read()
    
## The display both files
print("Source file: %s\n\n%s\n\n"%(source_file , source_content) )
print("Target file before change: %s\n\n%s\n\n"%(target_file , first_form_of_target_file))
print("Target file after change: %s\n\n%s\n\n"%(target_file , target_content) )