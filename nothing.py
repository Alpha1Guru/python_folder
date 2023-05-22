filename = "C:/Users/hp/Documents/Github/python_folder/Python_folder/verifier.py"
for char in filename:
    if char in ("\\"):
        filename = filename.replace(char,"/")
with open(filename) as pyfile:
    file  = pyfile.read()
print(file)

# filename = "C:\Users\hp\Documents\Github\python_folder\Python_folder\\verifier.py"
# for char in filename:
#     if char in ("\\"):
#         filename = filename.replace(char,"/")
# print(filename)      
# # with open(filename) as pyfile:
# #     file  = pyfile.read()
# # print(file)
