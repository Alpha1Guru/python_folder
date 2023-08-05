import numpy as np
import pandas as pd
import random
from tabulate import tabulate

def get_hall_names():
    pass

def hallsize(hall_name, halls):
    return sum(len(classe) for classe in halls[hall_name].values())

def totalhallsize(hall_names, halls):
    return sum(hallsize(hall_name, halls) for hall_name in hall_names)

def remainder(total_students, hall_names, halls):
    return len(total_students) - totalhallsize(hall_names, halls)

def check_sorted_name_hall_index(students_name, hall_name, students_by_hall_name_only):
    students_by_hall_name_only[hall_name].sort()
    for imember in range(len(students_by_hall_name_only[hall_name])):
        if students_name == students_by_hall_name_only[hall_name][imember]:
            index = imember
            break
    return index

def assign_students_to_halls(hall_names, class_names, students_by_class):
    halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}
    total_students = [student for students_list in students_by_class.values() for student in students_list]
    hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
    hall_remainder = len(total_students) % len(hall_names)
    classes = [students_by_class[key][:] for key in students_by_class.keys()]

    jclas = 0
    for ihall in range(len(hall_names)):
        while hallsize(hall_names[ihall], halls) < hall_limits[ihall]:
            if len(classes[jclas]) > 0 and hallsize(hall_names[ihall], halls) < hall_limits[ihall]:
                selected = random.choice(classes[jclas])
                classes[jclas].remove(selected)
                halls[hall_names[ihall]][class_names[jclas]].append(selected)
                halls[hall_names[ihall]][class_names[jclas]].sort()
            jclas = (jclas + 1) % len(class_names)
    
    for ihall in range(len(hall_names)):
        if remainder(total_students, hall_names, halls) == 0:
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
    
    return halls

def generate_students_data(hall_names, class_names, students_by_hall_name_and_class):
    students_by_hall_name_only = {}

    for hall_name in hall_names:
        students_by_hall_name_only[hall_name] = []

    for istddata in range(len(students_data)):
        hall = students_data[istddata]["hall"]
        students_by_hall_name_only[hall].append(students_data[istddata]["name"])
        
        if ask_response.lower() == "s":
            alphabetical_order = check_sorted_name_hall_index(students_name=students_data[istddata]["name"], hall_name=hall)
            students_by_hall_name_and_class[hall].insert(alphabetical_order, [students_data[istddata]["name"], students_data[istddata]["class"]])
        elif ask_response.lower() == "c":
            students_by_hall_name_and_class[hall].append([students_data[istddata]["name"], students_data[istddata]["class"]])

def save_hall_data_to_excel(hall_file, hall_names, students_by_hall_name_and_class):
    with pd.ExcelWriter(hall_file) as xfile:
        for hall_name, student_name_classes in students_by_hall_name_and_class.items():
            data = {"Name": [name_class[0].title() for name_class in student_name_classes], 
                    "Class": [name_class[1] for name_class in student_name_classes]}
            sheet = pd.DataFrame(data, index=(i+1 for i in range(len(student_name_classes))))
            sheet.to_excel(xfile, sheet_name=hall_name + " Hall")

hall_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
class_names = ["JSS1", "JSS2", "JSS3", "SS1A", "SS1B", "SS2A", "SS2B", "SS3A", "SS3B"]
students_by_class = {
    "JSS1": ["jss1", "john", "fatima", "mujeeb", "helen", "absalom"],
    "JSS2": ["jss2"],
    "JSS3": ["jss3", "geoffrey", "taiwo"],
    "SS1A": ["ss1a", "horla", "olaf", "rati", "jarimat"],
    "SS1B": ["ss1b", "yemi", "alade", "okoli", "micheal", "henry", "gloria", "peace", "magarita", "toyin"],
    "SS2A": ["ss2a", "emmma", "latifa", "baba", "tola"],
    "SS2B": ["ss2b", "marvellous"],
    "SS3A": ["ss3a", "bolu", "kante", "tochi", "kosi"],
    "SS3B": ["ss3b", "bade", "xenox", "kuma"]
}

halls = assign_students_to_halls(hall_names, class_names, students_by_class)

students_data = [{"name": member, "class": classname, "hall": hallname} 
                 for hallname in halls.keys() 
                 for classname, classmembers in halls[hallname].items() 
                 if len(classmembers) != 0 
                 for member in classmembers]

students_by_hall_name_and_class = {}
generate_students_data(hall_names, class_names, students_by_hall_name_and_class)

hall_file = "hall_placement.xlsx"
save_hall_data_to_excel(hall_file, hall_names, students_by_hall_name_and_class)
