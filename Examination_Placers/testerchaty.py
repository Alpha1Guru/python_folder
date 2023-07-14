import numpy as np
import pandas as pd
import random

class HallPlacement:
    def __init__(self):
        self.hall_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        self.class_names = ["JSS1", "JSS2", "JSS3", "SS1A", "SS1B", "SS2A", "SS2B", "SS3A", "SS3B"]
        self.students_by_class = {
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
        self.class_file = "class.xlsx"
        self.halls = {}
        self.total_students = []
        self.hall_limits = []
        self.hall_remainder = 0

    def get_hall_names(self):
        pass

    def hall_size(self, hall_name):
        return sum(len(class_members) for class_members in self.halls[hall_name].values())

    def total_hall_size(self):
        return sum(self.hall_size(hall_name) for hall_name in self.hall_names)

    def remainder(self):
        return len(self.total_students) - self.total_hall_size()

    def assign_hall_limits(self):
        while sum(self.hall_limits) != len(self.total_students):
            self.hall_limits = []
            num_not_assigned = len(self.total_students)
            print("Total number of Students: {}".format(num_not_assigned))
            for ihall in range(len(self.hall_names)):
                hall_limit = int(input(f"Tell me the hall limit of {self.hall_names[ihall]}: ").strip())
                self.hall_limits.append(hall_limit)
                num_not_assigned -= hall_limit
                if num_not_assigned > 0:
                    print("Number of students left: {}\n".format(num_not_assigned))
                elif num_not_assigned < 1:
                    print("Number of students left: 0\n")
            if sum(self.hall_limits) != len(self.total_students):
                print(f'''Your input does not match the total number of the students.
                Here are what you inputted:
                    Total = {sum(self.hall_limits)}
                    Total no of students = {len(self.total_students)}''')
                if sum(self.hall_limits) < len(self.total_students):
                    print("Your hall limits were {} less than the Total number of students! \n".format(
                        abs(num_not_assigned)))
                elif sum(self.hall_limits) > len(self.total_students):
                    print("Your hall limits were {} more than the Total number of students! \n".format(
                        abs(num_not_assigned)))
                for ihall in range(len(self.hall_names)):
                    print(self.hall_names[ihall], " = ", self.hall_limits[ihall])
                print("TRY AGAIN!!\n")
    
    def assign_halls(self):
        classes = [class_members[:] for class_members in self.students_by_class.values()]
        jclas = 0
        for ihall in range(len(self.hall_names)):
            while self.hall_size(self.hall_names[ihall]) < self.hall_limits[ihall]:
                if len(classes[jclas]) > 0 and self.hall_size(self.hall_names[ihall]) < self.hall_limits[ihall]:
                    selected = random.choice(classes[jclas])
                    classes[jclas].remove(selected)
                    self.halls[self.hall_names[ihall]][self.class_names[jclas]].append(selected)
                    self.halls[self.hall_names[ihall]][self.class_names[jclas]].sort()
                jclas += 1
                if jclas == len(self.class_names):
                    jclas = 0
    
    def assign_remaining_students(self):
        for ihall in range(len(self.hall_names)):
            if self.remainder() == 0:
                break
            else:
                random_class = random.choice(self.students_by_class.values())
                jclas = list(self.students_by_class.values()).index(random_class)
                while len(random_class) == 0:
                    random_class = random.choice(self.students_by_class.values())
                    jclas = list(self.students_by_class.values()).index(random_class)
                selected = random.choice(random_class)
                self.halls[self.hall_names[ihall]][self.class_names[jclas]].append(selected)
                self.halls[self.hall_names[ihall]][self.class_names[jclas]].sort()
                random_class.remove(selected)
    
    def generate_hall_placement(self):
        self.total_students = [student for students_list in self.students_by_class.values() for student in students_list]
        self.hall_limits = [len(self.total_students) // len(self.hall_names) for hall in self.hall_names]
        self.hall_remainder = len(self.total_students) % len(self.hall_names)

        self.assign_hall_limits()
        self.assign_halls()
        self.assign_remaining_students()

    def save_hall_placement_to_excel(self):
        hall_file = "hall_placement.xlsx"
        with pd.ExcelWriter(hall_file) as xfile:
            for hall_name, student_name_classes in self.halls.items():
                data = {"Name": [name_class[0].title() for name_class in student_name_classes],
                        "Class": [name_class[1]