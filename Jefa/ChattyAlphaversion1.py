hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M",]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B",]

students_by_class = {
    "JSS1": ["jss1", "john", "fatia","mujeeb","helen","absolom",],
    "JSS2": ["jss2"],
    "JSS3": ["jss3","geoferry","taiwo",],
    "SS1A": ["ss1a","horla","olaf", "rati","jarimat",],
    "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace","magarita","toyin",],
    "SS2A": ["ss2a","emmma","latifa","baba","tola",],
    "SS2B": ["ss2b", "marvellous"],
    "SS3A": ["ss3a","bolu","kante","tochi","kosi",],
    "SS3B": ["ss3b","bade","xenox","kuma",]
}
#Temporal list for data manipulation
JSS1 = students_by_class["JSS1"][:]
JSS2 = students_by_class["JSS2"][:]
JSS3 = students_by_class["JSS3"][:]
SS1A = students_by_class["SS1A"][:]
SS1B = students_by_class["SS1B"][:]
SS2A = students_by_class["SS2A"][:]
SS2B = students_by_class["SS2B"][:]
SS3A = students_by_class["SS3A"][:]
SS3B = students_by_class["SS3B"][:]

classes = [JSS1, JSS2, JSS3, SS1A, SS1B, SS2A, SS2B, SS3A, SS3B]
# print("classes: ", classes)

halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}

total_students = [student for students_list in students_by_class.values() for student in students_list]
hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
hall_remainder = len(total_students) % len(hall_names)
class_limits = [len(students_by_class[classe]) // len(hall_names) for classe in class_names]
class_remainders = [len(students_by_class[classe]) % len(hall_names) for classe in class_names]

def hallsize(hall_name):
    return sum(len(classe) for classe in halls[hall_name].values())

def totalhallsize():
    return sum(hallsize(hall_name) for hall_name in hall_names)

def remainder():
    return len(total_students) - totalhallsize()
#user inputs
from verifier4 import verPosInt as vi
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
        print("Not allowed. Type [Y/N]")
#to spit the student in halls
import random
for i in range(len(hall_names)):
    while hallsize(hall_names[i]) < hall_limits[i]:
        for j in range(len(class_names)):
            if len(classes[j]) != 0 and hallsize(hall_names[i]) < hall_limits[i]:
                selected = random.choice(classes[j])
                # print(classes[j])
                classes[j].remove(selected)
                # print(classes[j])
                halls[hall_names[i]][class_names[j]].append(selected)
#     print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
# print("remainder",remainder(),"\t")

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
        random_class.remove(selected)
#         print(random_class)
#     print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
# print("remainder",remainder())
# print("\n",halls)

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
# print("\n",students_data)        
# print(len(students_data))

students_by_hall = {}
for i in range(len(students_data)):
    hall = students_data[i]["hall"]
    if hall not in students_by_hall:
        students_by_hall[hall] = []
    students_by_hall[hall].append([students_data[i]["name"],students_data[i]["class"]])
#print("\n",students_by_hall)

for hallname,studentnameclasses in students_by_hall.items():
    print(f"Hall table for {hallname.title()}:")
    table =[[nameclass[0].title(),nameclass[1].upper()] for nameclass in studentnameclasses ]
    # e.g:
    # table                     = [['Gloria'      , 'SS1B'        ], ['Ss3A'        , 'SS3A'        ] ,['Kuma'        , 'SS3B'        ]]
    # |~represents hall names~| = [[~nameclass[0]~, ~nameclass[1]~], [~nameclass[0]~, ~nameclass[1]~] ,[~nameclass[0]~, ~nameclass[1]~]]
    #                             |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ studentnameclasses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    #print(table)
    print(tabulate(table,headers = ["names".title(),"class".title()], tablefmt="rounded_grid", showindex= range(1,hallsize(hallname) + 1)))
