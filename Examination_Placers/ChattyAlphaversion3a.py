#Creation of names for halls and class
hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M",]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B",]
#Storing the names of students by their class
students_by_class = {
    "JSS1": ["jss1", "john", "fatima","mujeeb","helen","absalom",],
    "JSS2": ["jss2"],
    "JSS3": ["jss3","geoffrey","taiwo",],
    "SS1A": ["ss1a","horla","olaf", "rati","jarimat",],
    "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace","magarita","toyin",],
    "SS2A": ["ss2a","emmma","latifa","baba","tola",],
    "SS2B": ["ss2b", "marvellous"],
    "SS3A": ["ss3a","bolu","kante","tochi","kosi",],
    "SS3B": ["ss3b","bade","xenox","kuma",]
}
#Temporary list for data manipulation
classes = [students_by_class[key][:] for key in students_by_class.keys()]
# print("classes: ", classes)
#Creation of halls and their class divisions
halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}

total_students = [student for students_list in students_by_class.values() for student in students_list]
hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
hall_remainder = len(total_students) % len(hall_names)

def hallsize(hall_name):
    return sum(len(classe) for classe in halls[hall_name].values())

def totalhallsize():
    return sum(hallsize(hall_name) for hall_name in hall_names)

def remainder():
    return len(total_students) - totalhallsize()

#Checks wether a user wants to specifically input the hall limits of each hall
from verifier import verint as vi
while True:
    response = input("Do you want to define the hall limits yourself? [Y/N]: ")
    if response == "Y":
        hall_limits = []
        while sum(hall_limits) != len(total_students):
            hall_limits = []
            num_not_assigned = len(total_students)
            print("Total number of Students: {}".format(num_not_assigned))
            for i in range(len(hall_names)):
                hall_limit = int(vi(input(f"Tell me the hall limit of {hall_names[i]}: ").strip()))
                hall_limits.append(hall_limit)
                num_not_assigned-= hall_limit; 
                if num_not_assigned > 0: print("Number of students left: {}\n".format(num_not_assigned))
                elif num_not_assigned < 1: print("Number of students left: 0\n")
            if sum(hall_limits) != len(total_students):
                print(f'''Your input does not match the total number of the students.
                Here are what you inputted:
                    Total = {sum(hall_limits)}
                    Total no of students = {len(total_students)}''')
                if sum(hall_limits) < len(total_students): print("Your hall limits were {} less than the Total number of students! \n".format(abs(num_not_assigned)))
                elif sum(hall_limits) > len(total_students): print("Your hall limits were {} more than the Total number of students! \n".format(abs(num_not_assigned)))
                for i in range(len(halls)):
                    print(hall_names[i]," = ", hall_limits[i])
                print("TRY AGAIN!!\n")
        break
    elif response == "N":
        break
    else:
        print("Invalid input!. Type [Y/N]")

#Splits the students randomly in halls
import random
for i in range(len(hall_names)):
    while hallsize(hall_names[i]) < hall_limits[i]:
        for j in range(len(class_names)):
            if len(classes[j]) > 0 and hallsize(hall_names[i]) < hall_limits[i]:
                selected = random.choice(classes[j])
                # print(classes[j])
                classes[j].remove(selected)
                # print(classes[j])
                halls[hall_names[i]][class_names[j]].append(selected)
                halls[hall_names[i]][class_names[j]].sort()
#     print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
# print("remainder",remainder(),"\t")

#Takes care students left unassigned after the first process of assigning equally into each hall
for i in range(len(hall_names)):
    if remainder() == 0:
        break
    else:
        random_class = random.choice(classes)
        j = classes.index(random_class)
        while len(random_class) == 0:
            random_class = random.choice(classes)
            j = classes.index(random_class)
        selected = random.choice(random_class)
        # print(random_class)
        halls[hall_names[i]][class_names[j]].append(selected)
        halls[hall_names[i]][class_names[j]].sort()
        random_class.remove(selected)
        # print(random_class)
    # print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
# print("remainder",remainder())
# print(halls)

from tabulate import*

# students_data = []
# for hallname  in halls.keys():
#     for classname,classemembers in halls[hallname].items():
#         if len(classemembers) != 0:
#             for member in classemembers:
#                 students_data.append({"name":member,"class":classname,"hall":hallname})
#         elif len(classemembers) == 0:
#             continue

students_data = [{"name":member,"class":classname,"hall":hallname} for hallname in halls.keys() for classname,classmembers in halls[hallname].items() if len(classmembers) != 0 for member in classmembers ]
# print(students_data)        
# print(len(students_data))

students_by_hall_name_and_class = {}
students_by_hall_name_only = {}

def check_sorted_name_hall_index(studentsname,hallname):
    students_by_hall_name_only[hallname].sort()
    for i in range(len(students_by_hall_name_only[hallname])):
        if studentsname == students_by_hall_name_only[hallname][i]:
            index = i
            break
    return index

while True:
    askresponse = input("""How do you want your table to look? 
                        Strictly alphabetical (type: s) or by class (type: c): """)
    if askresponse.lower() in ("s","c"):
        break      
    elif askresponse.lower() not in ("s","c"):
        print("Invalid response! (type s or c)")
for i in range(len(students_data)):
    hall = students_data[i]["hall"]
    if hall not in students_by_hall_name_and_class:
        students_by_hall_name_and_class[hall] = []
    if hall not in students_by_hall_name_only:
        students_by_hall_name_only[hall] = [] 
    students_by_hall_name_only[hall].append(students_data[i]["name"]) 
            
    if askresponse.lower() == "s":  
        alphabetical_order = check_sorted_name_hall_index(studentsname=students_data[i]["name"],hallname=hall)    
        students_by_hall_name_and_class[hall].insert(alphabetical_order,[students_data[i]["name"],students_data[i]["class"]])
    elif askresponse.lower() =="c":
        students_by_hall_name_and_class[hall].append([students_data[i]["name"],students_data[i]["class"]])
# print(students_by_hall_name_and_class)

#prints table for each hall
for hallname,studentnameclasses in students_by_hall_name_and_class.items():
    print(f"\nHall table for {hallname.title()}:")
    table =[[nameclass[0].title(),nameclass[1].upper()] for nameclass in studentnameclasses ]
    # e.g:
    # table                     = [['Gloria'      , 'SS1B'        ], ['Ss3A'        , 'SS3A'        ] ,['Kuma'        , 'SS3B'        ]]
    # |~represents hall names~| = [[~nameclass[0]~, ~nameclass[1]~], [~nameclass[0]~, ~nameclass[1]~] ,[~nameclass[0]~, ~nameclass[1]~]]
    #                             |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ studentnameclasses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    #print(table)
    table_file=tabulate(table,headers = ["names".title(),"class".title()], tablefmt="grid", showindex= range(1,hallsize(hallname) + 1))
    print(table_file)
    table_filepath ="C:/Users/hp/Documents/Github/python_folder/Examination_Placers/tables/hall_"+str(hallname) + ".txt"
    with open(table_filepath,"w") as tbf:
        tbf.write(table_file )
