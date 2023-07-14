import numpy as np
import pandas as pd
import random

def get_hall_names():
    pass

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
        self.hall_file = "hall_placement.xlsx"
        self.students_by_hall_name_and_class = {}
        self.students_by_hall_name_only = {}

    def hallsize(self, hall_name):
        return sum(len(classe) for classe in self.halls[hall_name].values())

    def totalhallsize(self):
        return sum(self.hallsize(hall_name) for hall_name in self.hall_names)

    def remainder(self):
        return len(self.total_students) - self.totalhallsize()

    def check_sorted_name_hall_index(self, students_name, hall_name):
        self.students_by_hall_name_only[hall_name].sort()
        for imember in range(len(self.students_by_hall_name_only[hall_name])):
            if students_name == self.students_by_hall_name_only[hall_name][imember]:
                return imember
        return -1

    def assign_halls(self):
        classes = [self.students_by_class[key][:] for key in self.students_by_class.keys()]
        self.halls = {hall_name: {class_name: [] for class_name in self.class_names} for hall_name in self.hall_names}
        total_students = [student for students_list in self.students_by_class.values() for student in students_list]
        hall_limits = [len(total_students) // len(self.hall_names) for _ in self.hall_names]
        hall_remainder = len(total_students) % len(self.hall_names)

        jclas = 0
        for ihall in range(len(self.hall_names)):
            while self.hallsize(self.hall_names[ihall]) < hall_limits[ihall]:
                if len(classes[jclas]) > 0 and self.hallsize(self.hall_names[ihall]) < hall_limits[ihall]:
                    selected = random.choice(classes[jclas])
                    classes[jclas].remove(selected)
                    self.halls[self.hall_names[ihall]][self.class_names[jclas]].append(selected)
                    self.halls[self.hall_names[ihall]][self.class_names[jclas]].sort()
                jclas += 1
                if jclas == len(self.class_names):
                    jclas = 0

        for ihall in range(len(self.hall_names)):
            if self.remainder() == 0:
                break
            else:
                random_class = random.choice(classes)
                jclas = classes.index(random_class)
                while len(random_class) == 0:
                    random_class = random.choice(classes)
                    jclas = classes.index(random_class)
                selected = random.choice(random_class)
                self.halls[self.hall_names[ihall]][self.class_names[jclas]].append(selected)
                self.halls[self.hall_names[ihall]][self.class_names[jclas]].sort()
                random_class.remove(selected)

    def prepare_data(self):
        students_data = []
        for hall_name in self.halls.keys():
            for class_name, class_members in self.halls[hall_name].items():
                if len(class_members) != 0:
                    for member in class_members:
                        students_data.append({"name": member, "class": class_name, "hall": hall_name})

        for istd_data in range(len(students_data)):
            hall = students_data[istd_data]["hall"]
            if hall not in self.students_by_hall_name_and_class:
                self.students_by_hall_name_and_class[hall] = []
            if hall not in self.students_by_hall_name_only:
                self.students_by_hall_name_only[hall] = []
            self.students_by_hall_name_only[hall].append(students_data[istd_data]["name"])

            if ask_response.lower() == "s":
                alphabetical_order = self.check_sorted_name_hall_index(
                    students_name=students_data[istd_data]["name"], hall_name=hall
                )
                self.students_by_hall_name_and_class[hall].insert(
                    alphabetical_order,
                    [students_data[istd_data]["name"].title(), students_data[istd_data]["class"]],
                )
            elif ask_response.lower() == "c":
                self.students_by_hall_name_and_class[hall].append(
                    [students_data[istd_data]["name"].title(), students_data[istd_data]["class"]]
                )

    def create_excel_sheets(self):
        with pd.ExcelWriter(self.class_file) as xfile:
            for class_name, class_members in self.students_by_class.items():
                data = {class_name.upper(): [name.title() for name in class_members]}
                sheet = pd.DataFrame(data)
                sheet.to_excel(
                    xfile,
                    sheet_name=class_name.upper() + " Class",
                    index=[i + 1 for i in range(len(class_members))],
                )

        with pd.ExcelWriter(self.hall_file) as xfile:
            for hall_name, student_name_classes in self.students_by_hall_name_and_class.items():
                data = {
                    "Name": [name_class[0] for name_class in student_name_classes],
                    "Class": [name_class[1] for name_class in student_name_classes],
                }
                sheet = pd.DataFrame(data, index=[i + 1 for i in range(len(student_name_classes))])
                sheet.to_excel(xfile, sheet_name=hall_name + " Hall")

    def run(self):
        self.assign_halls()
        self.prepare_data()
        self.create_excel_sheets()


if __name__ == "__main__":
    hall_placement = HallPlacement()
    ask_response = input(
        "How do you want your table to be? Strictly alphabetical (type: s) or by class (type: c): "
    )
    hall_placement.run()
