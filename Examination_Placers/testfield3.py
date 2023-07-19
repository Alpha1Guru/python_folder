import numpy as np
import pandas as pd
from verifier4 import verPosInt as vi

p1 = "~"*3
p2 = "."*3
p3 = u"\u10FB"
class_file = "test_class.xlsx"

# Under construction
def correct_mistakes(mistake: str, func, *args, **kwargs):
    """Attempts to correct user inputs by rerunning a function

    Args:
        mistake (str):should be "y" or "n"
        func (function): _description_
    """
    if mistake.lower() == "y":
        func(*args, *kwargs)
    elif mistake.lower() == "n":
        print("Okay!")
    else:
        print("Didn't Catch that")
        correct_mistakes(mistake)
    pass
    
def get_class_names() -> list:
    """Get the names of classes
    """
    print(f"\n{p1}GIVE ME THE NAMES OF CLASSES IN ASCENDING ORDER{p1}"
          f"\n{p2}Type 0 when Done")
    class_names = []
    count = 1
    class_name = input(f"{p3} {count}. Class Name (Type 0 when Done): ").strip()
    while class_name != "0":
        class_names.append(class_name.upper())
        count += 1
        class_name = input(f"{p3} {count}. Class Name (Type 0 when Done): ").strip()
    print(f"{p2}Classes are:")
    for name_no, class_name in enumerate(class_names):
        print(f"\t{name_no+1}. {class_name}")
    #Validation may need a function for this
    while True:
        mistake = input("Made a mistake? [y/n]: ").strip()
        if mistake == "y":
            return get_class_names()
        elif mistake == "n":
            print("Done!\n")
            break
        else:
            print("Didn't catch that")

    return class_names

def get_students_by_class(class_names: list) -> dict:
    """maps the list of class_names to class members

    Args:
        class_names (list): A list of strings which represents names of classes

    Returns:
        dict: Dictionary containing the class names mapped to class members
    """
    def get_students(class_name: str, no_of_members: int) -> list:
        print(f"~~~GIVE ME THE MEMBERS OF {class_name.upper()}~~~")
        return [input(f"{p3} Member: ").strip() for i_member in range(no_of_members)]
    
    students_by_class = {}
    for class_name in class_names:
        no_of_members: int = int(vi(input(
            f"{p2} How many members are in {class_name}: ").strip()))
        students_by_class[class_name] = get_students(class_name, no_of_members)
    return students_by_class

def save_class_data_to_excel(class_file: str, students_by_class: dict) -> None:
    """Save class Details to an excel file

    Args:
        class_file (str): path to excel file
        students_by_class (dict): Dictionary of class names mapped 
                                to a list of members.
        
    """    
    with pd.ExcelWriter(class_file) as xfile:
        for class_name, class_members in students_by_class.items():
            data= {"Names":[name.title() for name in class_members]}
            sheet = pd.DataFrame(data,
                                index= (i+1 for i in range(len(class_members)))
                                )
            sheet.to_excel(xfile, sheet_name=class_name.upper() + " Class")

def get_actual_classes(students_by_class: dict) -> list:
    """Tries to get the classes that are to be assigned to
    halls i.e the actual classing to work on

    Args:
        students_by_class (dict): Dictionary of class names mapped 
                                to a list of members.

    Returns:
        list:  a list of the actual classes to work with
    """
    print(f"{p1}WHICH CLASSES ARE ACTUALLY WRITING THIS EXAM???{p1}"
          f"\nType y for yes or n for No for The Class")
    actual_working_class = []
    for class_name, class_members in students_by_class:
        response = input(f"{p1}{class_name} (type y or n): ").strip()
        
        #may need a function for this
        while True:
            if response == "y":
                actual_working_class.append(class_members)
                break
            if response == "n":
                break
            else:
                print("Didn't catch that")
    # checks if a mistake was made
    while True:
        mistake = input("Made a mistake? [y/n]: ").strip()
        if mistake == "y":
            return get_actual_classes()
        elif mistake == "n":
            print("Done!\n")
            break
        else:
            print("Didn't catch that")

    return actual_working_class
                
                                
def get_hall_names()-> list:
    """Get the names of Halls to be used by students
    """
    print(f"\n{p1}GIVE ME THE NAMES OF HALLS{p1}"
          f"\n{p2}Type 0 when Done")
    hall_names = []
    hall_name = input(f"{p3} Hall Name (Type 0 when Done): ").strip()
    while hall_name != "0":
        hall_names.append(hall_name.upper())
        hall_name = input(f"{p3} Hall Name (Type 0 when Done): ").strip()
    print(f"{p2}Halls are:")
    for name_no, hall_name in enumerate(hall_names):
        print(f"\t{name_no+1}. {hall_name}")
    
    #Validation may need a function, checks whether the user made a mistake
    while True:
        mistake = input("Made a mistake? [y/n]: ").strip()
        if mistake == "y":
            return get_hall_names()
        elif mistake == "n":
            print("Done!\n")
            break
        else:
            print("Didn't catch that")
    return hall_names

def hall_size(hall_name: str, halls: dict) -> int:  
    return sum(len(class_) for class_ in halls[hall_name].values())
    pass

def total_hall_size(hall_names: list) -> int:
    return sum(hall_size(hall_name, halls) for hall_name in hall_names)
    pass

def remainder(total_students: list, hall_names: list) -> int:
    return len(total_students) - total_hall_size()
    pass

def assign_to_hall():
   
    pass
def save_hall_data_to_excel():
    pass

def store_db(class_file: str):
    class_names = get_class_names()
    print(class_names)
    
    #Storing the names of students by their class
    students_by_class = get_students_by_class(class_names)
    print(students_by_class)
    
    save_class_data_to_excel(class_file, students_by_class)
    
    classes = get_actual_classes(students_by_class)  #Actual classes to work with
    print(classes)
    
    hall_names = get_hall_names()
    halls = {hall_name: {class_: [] for class_ in class_names} for hall_name in hall_names}
    total_students = [student for students_list in students_by_class.values() for student in students_list]
    hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
    hall_remainder = len(total_students) % len(hall_names)

    
# hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M",]
# class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B",]

# #Storing the names of students by their class
# students_by_class = {
#     "JSS1": ["jss1", "john", "fatima","mujeeb","helen","absalom",],
#     "JSS2": ["jss2"],
#     "JSS3": ["jss3","geoffrey","taiwo",],
#     "SS1A": ["ss1a","horla","olaf", "rati","jarimat",],
#     "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace",
#              "magarita","toyin",],
#     "SS2A": ["ss2a","emmma","latifa","baba","tola",],
#     "SS2B": ["ss2b", "marvellous"],
#     "SS3A": ["ss3a","bolu","kante","tochi","kosi",],
#     "SS3B": ["ss3b","bade","xenox","kuma",]
# }


# #Temporary list for data manipulation
# classes = [students_by_class[key][:] for key in students_by_class.keys()]

# #Creation of halls and their class divisions
# halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}

# total_students = [student for students_list in students_by_class.values() for student in students_list]
# hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
# hall_remainder = len(total_students) % len(hall_names)

# def hallsize(hall_name):
    
#     return sum(len(classe) for classe in halls[hall_name].values())

# def totalhallsize():
#     return sum(hallsize(hall_name) for hall_name in hall_names)

# def remainder():
#     return len(total_students) - totalhallsize()

# #Checks wether a user wants to specifically input the hall limits of each hall
# while True:
#     response = input("Do you want to define the hall limits yourself? [Y/N]: ").strip()
#     if response == "Y":
#         hall_limits = []
#         while sum(hall_limits) != len(total_students):
#             hall_limits = []
#             num_not_assigned = len(total_students)
#             print("Total number of Students: {}".format(num_not_assigned))
#             for ihall in range(len(hall_names)):
#                 hall_limit = int(vi(input(f"Tell me the hall limit of {hall_names[ihall]}: ").strip()))
#                 hall_limits.append(hall_limit)
#                 num_not_assigned-= hall_limit; 
#                 if num_not_assigned > 0: print("Number of students left: {}\n".format(num_not_assigned))
#                 elif num_not_assigned < 1: print("Number of students left: 0\n")
#             if sum(hall_limits) != len(total_students):
#                 print(f'''Your input does not match the total number of the students.
#                 Here are what you inputted:
#                     Total = {sum(hall_limits)}
#                     Total no of students = {len(total_students)}''')
#                 if sum(hall_limits) < len(total_students): 
#                     print("Your hall limits were {} less than the Total number of students! \n".format(abs(num_not_assigned)))
#                 elif sum(hall_limits) > len(total_students): 
#                     print("Your hall limits were {} more than the Total number of students! \n".format(abs(num_not_assigned)))
#                 for ihall in range(len(halls)):
#                     print(hall_names[ihall]," = ", hall_limits[ihall])
#                 print("TRY AGAIN!!\n")
#         break
#     elif response == "N":
#         break
#     else:
#         print("Invalid input!. Type [Y/N]")

# #Splits the students randomly in halls
# import random
# jclas = 0
# for ihall in range(len(hall_names)):
#     while hallsize(hall_names[ihall]) < hall_limits[ihall]:
#         if len(classes[jclas]) > 0 and hallsize(hall_names[ihall]) < hall_limits[ihall]:
#             selected = random.choice(classes[jclas])
#             # print(class_names[jclas])
#             # print(classes[jclas])
#             classes[jclas].remove(selected)
#             # print(classes[jclas])
#             halls[hall_names[ihall]][class_names[jclas]].append(selected)
#             halls[hall_names[ihall]][class_names[jclas]].sort()
#         jclas=jclas+1
#         if jclas == len(class_names): jclas = 0

# # Deals with the remainder
# for ihall in range(len(hall_names)):
#     if remainder() == 0:
#         break
#     else:
#         random_class = random.choice(classes)
#         jclas = classes.index(random_class)
#         while len(random_class) == 0:
#             random_class = random.choice(classes)
#             jclas = classes.index(random_class)
#         selected = random.choice(random_class)
#         halls[hall_names[ihall]][class_names[jclas]].append(selected)
#         halls[hall_names[ihall]][class_names[jclas]].sort()
#         random_class.remove(selected)

# from tabulate import*
# # Saving to file
# students_data = [{"name":member,"class":classname,"hall":hallname} 
#                  for hallname in halls.keys() 
#                  for classname,classmembers in halls[hallname].items() 
#                  if len(classmembers) != 0 for member in classmembers ]
# students_by_hall_name_and_class = {}
# students_by_hall_name_only = {}

# def check_sorted_name_hall_index(studentsname,hallname):
#     students_by_hall_name_only[hallname].sort()
#     for imember in range(len(students_by_hall_name_only[hallname])):
#         if studentsname == students_by_hall_name_only[hallname][imember]:
#             index = imember
#             break
#     return index

# while True:
#     askresponse = input("""How do you want your table to be? 
#                         Strictly alphabetical (type: s) or by class (type: c): """).strip()
#     if askresponse.lower() in ("s","c"):
#         break      
#     elif askresponse.lower() not in ("s","c"):
#         print("Invalid response! (type s or c)")
# for istddata in range(len(students_data)):
#     hall = students_data[istddata]["hall"]
#     if hall not in students_by_hall_name_and_class:
#         students_by_hall_name_and_class[hall] = []
#     if hall not in students_by_hall_name_only:
#         students_by_hall_name_only[hall] = [] 
#     students_by_hall_name_only[hall].append(students_data[istddata]["name"]) 
            
#     if askresponse.lower() == "s":  
#         alphabetical_order = check_sorted_name_hall_index(studentsname=students_data[istddata]["name"],hallname=hall)    
#         students_by_hall_name_and_class[hall].insert(alphabetical_order,[students_data[istddata]["name"],students_data[istddata]["class"]])
#     elif askresponse.lower() =="c":
#         students_by_hall_name_and_class[hall].append([students_data[istddata]["name"],students_data[istddata]["class"]])
# # print(students_by_hall_name_and_class)

# hall_file = "hall_placement.xlsx"
# with pd.ExcelWriter(hall_file) as xfile:
#     for hallname,studentnameclasses in students_by_hall_name_and_class.items():
#         d = {"Name": [nameclass[0].title() for nameclass in studentnameclasses ], "Class": [nameclass[1] for nameclass in studentnameclasses]}
#         # print(d)
#         sheet = pd.DataFrame(d, index=(i+1 for i in range(len(studentnameclasses))) )
#         # print(sheet)
#         sheet.to_excel(xfile, sheet_name=hallname + " Hall")
if __name__ == "__main__":
    store_db(class_file)