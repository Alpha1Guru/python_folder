import numpy as np
import pandas as pd
from verifier4 import verPosInt as vi

p1 = "~"*3
p2 = "."*3
p3 = u"\u10FB"
class_file = "class.xlsx"

def get_class_names():
    """Get the names of classes
    """
    print(f"\n{p1}GIVE ME THE NAMES OF CLASSES IN ASCENDING ORDER{p1}"
          f"\n{p2}Type 0 to quit")
    class_names = []
    while class_name := input(f"{p3} Class Name: ") != "0":
        class_names.append(class_name.upper())
    print(f"{p2}Classes are:")
    for name_no, class_name in enumerate(class_names):
        print(f"\t{name_no}. {class_name}")
    mistake = input("Made a mistake? [y/n]: ")
    if mistake == "y":
        get_class_names()
    print("Done!\n")
    return class_names

def get_students_by_class(class_names: list) -> dict:
    """maps the list of class_names to class members

    Args:
        class_names (list): A list of strings which represents names of classes

    Returns:
        dict: Dictionary containing the class names mapped to class members
    """
    def get_students(class_name: str, no_of_members: int):
        print(f"~~~GIVE ME THE MEMBERS OF {class_name.upper()}~~~")
        return [input(f"{p3} Member: ") for i_member in range(no_of_members)]
    
    students_by_class = {}
    for class_name in class_names:
        no_of_members: int = int(vi(input(
            f"{p2} Number of Members of {class_name}: ")))
        students_by_class[class_name] = get_students(class_name, no_of_members)
    return students_by_class

def save_class_data_to_excel(class_file: str, students_by_class: dict):
    """Save class Details to an excel file

    Args:
        class_file (str): path to excel file
        students_by_class (dict): Dictionary containing class names a
    """    
    with pd.ExcelWriter(class_file) as xfile:
        for class_name, class_members in students_by_class.items():
            data= {class_name.upper():[name.title() for name in class_members]}
            sheet = pd.DataFrame(data, index= (i+1 for i in range(len(class_members))), columns=["S/N","Names"])
            sheet.to_excel(xfile, sheet_name=class_name.upper() + " Class")

def get_hall_names():
    pass
def assign_to_hall():
    pass
def save_hall_data_to_excel():
    pass

hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M",]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B",]

#Storing the names of students by their class
students_by_class = {
    "JSS1": ["jss1", "john", "fatima","mujeeb","helen","absalom",],
    "JSS2": ["jss2"],
    "JSS3": ["jss3","geoffrey","taiwo",],
    "SS1A": ["ss1a","horla","olaf", "rati","jarimat",],
    "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace",
             "magarita","toyin",],
    "SS2A": ["ss2a","emmma","latifa","baba","tola",],
    "SS2B": ["ss2b", "marvellous"],
    "SS3A": ["ss3a","bolu","kante","tochi","kosi",],
    "SS3B": ["ss3b","bade","xenox","kuma",]
}
class_file = "class.xlsx"
with pd.ExcelWriter(class_file) as xfile:
    for class_name, class_members in students_by_class.items():
        data= {"Names":[name.title() for name in class_members]}
        sheet = pd.DataFrame(data,
                             index= (i+1 for i in range(len(class_members)))
                             )
        sheet.to_excel(xfile, sheet_name=class_name.upper() + " Class")
"""SOME VARIABLES AND FUNCTIONS USED
---=================================---
Variables:
            classes= this variable is a list of lists. The elements of the list
            are lists/(class) that contains names of class members its use is 
            to manipulate the students_by_class dictionary without affecting 
            the dictionary itself.
            
            halls= this is a dictionary whose structure is 
            {hall name=> {class name=> [class members]}}  i.e its keys are 
            other dictionaries that represent that represent the hall names 
            whose values are key that represent class names who is set to a 
            value of a list of class members 
            e.g {'MaryHALL':{ 'Jss1':['James Okoli','Jude Nnenna'],
                                'Jss2':['Jam Oli','Ude Nna']},
                 'AnHall':{ 'Ss1':['Ade Oko'],
                            'SS2':['Jam Oli']}} 
            However this hall is initially empty containing just the names of 
            hall and class but not the members of this class
            
            total_students= this is a list of the names of all the students 
            irrespective of their classes
            
            hall_limits= this is a list of the the maximum number of students 
            required for each hall. It is computed by the floor division of 
            the total number of  students by the number of halls used. The sum
            of the numbers in the list represents the number of students that 
            have been assigned to halls. since it was a floor division there 
            may be a remainder that is always less than the total number of 
            halls

            totalhallsize()
            
Functions:
            hallsize(hall_name)
            
            def remainder()
            """
#Temporary list for data manipulation
classes = [students_by_class[key][:] for key in students_by_class.keys()]

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
while True:
    response = input("Do you want to define the hall limits yourself? [Y/N]: ")
    if response == "Y":
        hall_limits = []
        while sum(hall_limits) != len(total_students):
            hall_limits = []
            num_not_assigned = len(total_students)
            print("Total number of Students: {}".format(num_not_assigned))
            for ihall in range(len(hall_names)):
                hall_limit = int(vi(input(f"Tell me the hall limit of {hall_names[ihall]}: ").strip()))
                hall_limits.append(hall_limit)
                num_not_assigned-= hall_limit; 
                if num_not_assigned > 0: print("Number of students left: {}\n".format(num_not_assigned))
                elif num_not_assigned < 1: print("Number of students left: 0\n")
            if sum(hall_limits) != len(total_students):
                print(f'''Your input does not match the total number of the students.
                Here are what you inputted:
                    Total = {sum(hall_limits)}
                    Total no of students = {len(total_students)}''')
                if sum(hall_limits) < len(total_students): 
                    print("Your hall limits were {} less than the Total number of students! \n".format(abs(num_not_assigned)))
                elif sum(hall_limits) > len(total_students): 
                    print("Your hall limits were {} more than the Total number of students! \n".format(abs(num_not_assigned)))
                for ihall in range(len(halls)):
                    print(hall_names[ihall]," = ", hall_limits[ihall])
                print("TRY AGAIN!!\n")
        break
    elif response == "N":
        break
    else:
        print("Invalid input!. Type [Y/N]")

#Splits the students randomly in halls
import random
jclas = 0
for ihall in range(len(hall_names)):
    while hallsize(hall_names[ihall]) < hall_limits[ihall]:
        if len(classes[jclas]) > 0 and hallsize(hall_names[ihall]) < hall_limits[ihall]:
            selected = random.choice(classes[jclas])
            # print(class_names[jclas])
            # print(classes[jclas])
            classes[jclas].remove(selected)
            # print(classes[jclas])
            halls[hall_names[ihall]][class_names[jclas]].append(selected)
            halls[hall_names[ihall]][class_names[jclas]].sort()
        jclas=jclas+1
        if jclas == len(class_names): jclas = 0

# Deals with the remainder
for ihall in range(len(hall_names)):
    if remainder() == 0:
        break
    else:
        random_class = random.choice(classes)
        jclas = classes.index(random_class)
        while len(random_class) == 0:
            random_class = random.choice(classes)
            jclas = classes.index(random_class)
        selected = random.choice(random_class)
        halls[hall_names[ihall]][class_names[jclas]].append(selected)
        halls[hall_names[ihall]][class_names[jclas]].sort()
        random_class.remove(selected)

from tabulate import*
# Saving to file
students_data = [{"name":member,"class":classname,"hall":hallname} 
                 for hallname in halls.keys() 
                 for classname,classmembers in halls[hallname].items() 
                 if len(classmembers) != 0 for member in classmembers ]
students_by_hall_name_and_class = {}
students_by_hall_name_only = {}

def check_sorted_name_hall_index(studentsname,hallname):
    students_by_hall_name_only[hallname].sort()
    for imember in range(len(students_by_hall_name_only[hallname])):
        if studentsname == students_by_hall_name_only[hallname][imember]:
            index = imember
            break
    return index

while True:
    askresponse = input("""How do you want your table to be? 
                        Strictly alphabetical (type: s) or by class (type: c): """)
    if askresponse.lower() in ("s","c"):
        break      
    elif askresponse.lower() not in ("s","c"):
        print("Invalid response! (type s or c)")
for istddata in range(len(students_data)):
    hall = students_data[istddata]["hall"]
    if hall not in students_by_hall_name_and_class:
        students_by_hall_name_and_class[hall] = []
    if hall not in students_by_hall_name_only:
        students_by_hall_name_only[hall] = [] 
    students_by_hall_name_only[hall].append(students_data[istddata]["name"]) 
            
    if askresponse.lower() == "s":  
        alphabetical_order = check_sorted_name_hall_index(studentsname=students_data[istddata]["name"],hallname=hall)    
        students_by_hall_name_and_class[hall].insert(alphabetical_order,[students_data[istddata]["name"],students_data[istddata]["class"]])
    elif askresponse.lower() =="c":
        students_by_hall_name_and_class[hall].append([students_data[istddata]["name"],students_data[istddata]["class"]])
# print(students_by_hall_name_and_class)

hall_file = "hall_placement.xlsx"
with pd.ExcelWriter(hall_file) as xfile:
    for hallname,studentnameclasses in students_by_hall_name_and_class.items():
        d = {"Name": [nameclass[0].title() for nameclass in studentnameclasses ], "Class": [nameclass[1] for nameclass in studentnameclasses]}
        # print(d)
        sheet = pd.DataFrame(d, index=(i+1 for i in range(len(studentnameclasses))) )
        # print(sheet)
        sheet.to_excel(xfile, sheet_name=hallname + " Hall")
