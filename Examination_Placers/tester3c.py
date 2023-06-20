#Creation of names for halls and class
hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M",]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B",]
#Storing the names of students by thier class
students_by_class = {
    "JSS1": ["jss1",],
    "JSS2": ["jss2","tom",'jerry',"akka","nduka","amaechi","olaf","elsa","anna","nkoli","ezinne","omma",'njiko',],
    "JSS3": ["jss3","geoferry","johnny","gemma","megan","godswill","florence","mina","gina","spike",],
    "SS1A": ["ss1a","horla","alamin","conda","samson","summ","melin","curry","ice",],
    "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace","magarita","toyin",],
    "SS2A": ["ss2a","emmma","latifa","baba","tola","bolo","achuu","raty","lot","amen","fomal","ifoma","khadi",],
    "SS2B": ["ss2b", "marvellous","chijo","saba","ike","nkoli","chike","onah","udo","udeh","amed","fire","gem",],
    "SS3A": ["ss3a","bolu","kante","tochi","kosi","holy","bad","musa","paul","jery","amos","isaac","grace"],
    "SS3B": ["ss3b","bade","xenox","kuma","kuga","osamu","kazamaza","torimaru","jin","chikasan","yotaru","hyuse","tachikawa",]
}
#Temporary list for data manipulation
classes = [students_by_class[key][:] for key in students_by_class.keys()]
# print("classes: ", classes)
#Creation of halls and their class divisions
halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}

total_students = [student for students_list in students_by_class.values() for student in students_list]
hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
hall_remainder = len(total_students) % len(hall_names)
print(hall_limits)
#To get class limits for each class
class_limits = [len(classe)//len(hall_names) for classe in classes]
print("class limits: ", class_limits)

#To get class limits for each class
class_remainders = [len(classe)%len(hall_names) for classe in classes]
print("class remainders", class_remainders)

def hallsize(hall_name):
    return sum(len(classe) for classe in halls[hall_name].values())

def totalhallsize():
    return sum(hallsize(hall_name) for hall_name in hall_names)

def remainder():
    return len(total_students) - totalhallsize()

print(len(total_students))
#Checks wether a user wants to specifcally input the hall limits of each hall

#Splits the students randomly in halls
import random
for iclas in range(len(class_names)):
    print(f"\n\n{class_names[iclas]}, {classes[iclas]}, length: {len(classes[iclas])}")
    print(f"class limit: {class_limits[iclas]}")
    for jhall in range(len(hall_names)):
        print(f"\n\t{hall_names[jhall]}")
        selected = random.choices(classes[iclas],k=class_limits[iclas])
        print(f"\n\tselected: {selected}")
        halls[hall_names[jhall]][class_names[iclas]].extend(selected)
        for ichosen in selected:
            classes[iclas].remove(ichosen)
    print(f"class after: {classes[iclas]},length: {len(classes[iclas])}")

#Takes care students left unassigned after the first process of assigning equally into each hall


# from tabulate import*

# # students_data = []
# # for hallname  in halls.keys():
# #     for classname,classemembers in halls[hallname].items():
# #         if len(classemembers) != 0:
# #             for member in classemembers:
# #                 students_data.append({"name":member,"class":classname,"hall":hallname})
# #         elif len(classemembers) == 0:
# #             continue

# students_data = [{"name":member,"class":classname,"hall":hallname} for hallname in halls.keys() for classname,classmembers in halls[hallname].items() if len(classmembers) != 0 for member in classmembers ]
# # print(students_data)        
# # print(len(students_data))

# students_by_hall_name_and_class = {}
# students_by_hall_name_only = {}

# def check_sorted_name_hall_index(studentsname,hallname):
#     students_by_hall_name_only[hallname].sort()
#     for i in range(len(students_by_hall_name_only[hallname])):
#         if studentsname == students_by_hall_name_only[hallname][i]:
#             index = i
#             break
#     return index


# askresponse = "c"
# for i in range(len(students_data)):
#     hall = students_data[i]["hall"]
#     if hall not in students_by_hall_name_and_class:
#         students_by_hall_name_and_class[hall] = []
#     if hall not in students_by_hall_name_only:
#         students_by_hall_name_only[hall] = [] 
#     students_by_hall_name_only[hall].append(students_data[i]["name"]) 
            
#     if askresponse.lower() == "s":  
#         alphabetical_order = check_sorted_name_hall_index(studentsname=students_data[i]["name"],hallname=hall)    
#         students_by_hall_name_and_class[hall].insert(alphabetical_order,[students_data[i]["name"],students_data[i]["class"]])
#     elif askresponse.lower() =="c":
#         students_by_hall_name_and_class[hall].append([students_data[i]["name"],students_data[i]["class"]])
# # print(students_by_hall_name_and_class)

# #prints table for each hall
# for hallname,studentnameclasses in students_by_hall_name_and_class.items():
#     print(f"\nHall table for {hallname.title()}:")
#     table =[[nameclass[0].title(),nameclass[1].upper()] for nameclass in studentnameclasses ]
#     # e.g:
#     # table                     = [['Gloria'      , 'SS1B'        ], ['Ss3A'        , 'SS3A'        ] ,['Kuma'        , 'SS3B'        ]]
#     # |~represents hall names~| = [[~nameclass[0]~, ~nameclass[1]~], [~nameclass[0]~, ~nameclass[1]~] ,[~nameclass[0]~, ~nameclass[1]~]]
#     #                             |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ studentnameclasses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
#     #print(table)
#     table_file=tabulate(table,headers = ["names".title(),"class".title()], tablefmt="grid", showindex= range(1,hallsize(hallname) + 1))
#     print(table_file)
#     table_filepath ="C:/Users/hp/Documents/Github/python_folder/Examination_Placers/tables/hall_"+str(hallname) + ".txt"
#     with open(table_filepath,"w") as tbf:
#         tbf.write(table_file )
