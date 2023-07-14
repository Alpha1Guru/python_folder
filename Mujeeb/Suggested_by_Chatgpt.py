from random import choice
import pandas as pd

# Output file path
output_file = "exam_formation.xlsx"

# Stored data file path
stored_file = "classes_data.xlsx"

def get_class_name(existing_classes):
    while True:
        class_name = input("\n\t\t.....WHAT CLASS IS THIS?.....: ").upper()
        if class_name in existing_classes:
            return class_name
        else:
            print(f"\n!!!The class '{class_name}' you entered does not match the one in our database!!!.")
            response = input(f"\nDO YOU WANT TO CREATE AND ADD {class_name} TO YOUR DATABASE?. [Y/n]:    ")
            if response == "Y":
                existing_classes[class_name] = []
                return class_name
            elif response == "n":
                continue
            else:
                print("INVALID INPUT, TRY AGAIN. ")

def get_students(class_name):
    class_limit = int(input(f"\n\t\t   |*| HOW MANY STUDENTS ARE IN {class_name}:  "))
    students = []
    for _ in range(class_limit):
        student_name = input(f"\n\t\t\t[*]  GIVE ME ALL {class_name} STUDENTS NAME, ONE AFTER THE OTHER.:    ")
        students.append(student_name)
    return students

def store_classes_data(classes, file_path):
    with pd.ExcelWriter(file_path) as writer:
        for class_name, students in classes.items():
            df = pd.DataFrame(students, columns=[class_name])
            df.to_excel(writer, sheet_name=class_name, index=False)

def generate_hall_arrangement(classes, hall_db_filename):
    halls = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': []}

    def get_hall_limit(hall):
        while True:
            hall_limit = int(input(f"\n\t\t~~~~~WHAT'S HALL {hall} LIMIT?~~~~~:    "))
            all_students = sum(len(class_students) for class_students in classes.values())
            if hall_limit > all_students:
                print(f" Your hall limit '{hall_limit}', is greater than the number of students '{all_students}' left. ".upper())
            else:
                return hall_limit

    for hall in halls:
        hall_limit = get_hall_limit(hall)
        while len(halls[hall]) < hall_limit:
            for class_name, students in classes.items():
                if students:
                    random_student = choice(students)
                    halls[hall].append([random_student, class_name])
                    students.remove(random_student)
                    if len(halls[hall]) == hall_limit:
                        break

    return halls

def sort_students_by_class(student):
    return student[1]

def write_output_to_excel(halls, hall_db_filename, sort_by_class):
    with pd.ExcelWriter(hall_db_filename) as writer:
        for hall, students in halls.items():
            if sort_by_class:
                sorted_students = sorted(students, key=sort_students_by_class)
            else:
                sorted_students = students
            df = pd.DataFrame(sorted_students, columns=["Name", "Class"])
            df.index += 1
            sheet_name = "Hall " + hall
            df.to_excel(writer, sheet_name=sheet_name, index=True)

def StoreDB(hall_db_filename):
    existing_classes = {'JSS1': ['Chukwujekwu Pius', 'Akintoye Tolu', 'Adefisoye Sam', 'Ofoke Max', 'Ofoke James', '16', '17', '18', '19', '110', '111', '112', '113', '114'],
                        'JSS2': ['21', '22', '23', '24', '25', '26', '27', '28', '29', '210', '211', '212', '213', '214'],
                        'JSS3': ['31', '32', '33', '34', '35', '36', '37', '38', '39', '310', '311', '312', '313', '314'],
                        'SS1A': ['1A1', '1A2', '1A3', '1A4', '1A5', '1A6', '1A7', '1A8', '1A9', '1A10', '1A11', '1A12', '1A13', '1A14'],
                        'SS1B': ['1B1', '1B2', '1B3', '1B4', '1B5', '1B6', '1B7', '1B8', '1B9', '1B10', '1B11', '1B12', '1B13', '1B14'],
                        'SS2A': ['2A1', '2A2', '2A3', '2A4', '2A5', '2A6', '2A7', '2A8', '2A9', '2A10', '2A11', '2A12', '2A13', '2A14'],
                        'SS2B': ['2B1', '2B2', '2B3', '2B4', '2B5', '2B6', '2B7', '2B8', '2B9', '2B10', '2B11', '2B12', '2B13', '2B14'],
                        'SS3A': ['3A1', '3A2', '3A3', '3A4', '3A5', '3A6', '3A7', '3A8', '3A9', '3A10', '3A11', '3A12', '3A13', '3A14'],
                        'SS3B': ['3B1', '3B2', '3B3', '3B4', '3B5', '3B6', '3B7', '3B8', '3B9', '3B10', '3B11', '3B12', '3B13', '3B14']}

    all_class = verify(input("    ___HOW MANY CLASS ARE PRESENTLY WRITING THIS EXAM___?:  "))

    for _ in range(all_class):
        class_name = get_class_name(existing_classes)
        students = get_students(class_name)
        existing_classes[class_name] = students

    user_response = input("\n\nDO YOU WANT TO SAVE THE INFORMATION PROVIDED ABOUT ALL CLASS AND STUDENT [Y/n]:     ")

    if user_response == "Y":
        store_classes_data(existing_classes, stored_file)
    elif user_response == "n":
        print("Okay. \n INFO NOT SAVED.")

    halls = generate_hall_arrangement(existing_classes, hall_db_filename)

    while True:
        user_input = input(f"""  HOW DO WANT TO ARRANGE YOUR OUTPUT?
                    A) ACCORDING TO NAME ALPHABETICAL ORDER
                    B) ACCORDING TO CLASS ORDER
                    ENTER:  """)

        if user_input == "A":
            write_output_to_excel(halls, hall_db_filename, sort_by_class=False)
            print("Your output has been stored in an Excel file in your present working directory/path.")
            break
        elif user_input == "B":
            write_output_to_excel(halls, hall_db_filename, sort_by_class=True)
            print("Your output has been stored in an Excel file in your present working directory/path.")
            break
        else:
            print("\n\t[*] Your input does not correspond to required input; 'TRY AGAIN' [*]")

StoreDB(output_file)
