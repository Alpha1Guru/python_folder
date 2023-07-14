from random import choice
from verify import verify
import pandas as pd
import os

# output_file holds the path the programs output will be stored
output_file = "exam_formation.xlsx"

# Data provided is stored in stored_file
stored_file = "classes_data.xlsx"

def StoreDB(hall_db_filename):

    # CLASSES holds information about the school class and student.
    CLASSES = {'JSS1':['Chukwujekwu Pius','Akintoye Tolu','Adefisoye Sam','Ofoke Max','Ofoke James','16','17','18','19','110','111','112','113','114'],
            'JSS2':['21','22','23','24','25','26','27','28','29','210','211','212','213','214'],
            'JSS3':['31','32','33','34','35','36','37','38','39','310','311','312','313','314'],
            'SS1A':['1A1','1A2','1A3','1A4','1A5','1A6','1A7','1A8','1A9','1A10','1A11','1A12','1A13','1A14'],
            'SS1B':['1B1','1B2','1B3','1B4','1B5','1B6','1B7','1B8','1B9','1B10','1B11','1B12','1B13','1B14'],
            'SS2A':['2A1','2A2','2A3','2A4','2A5','2A6','2A7','2A8','2A9','2A10','2A11','2A12','2A13','2A14'],
            'SS2B':['2B1','2B2','2B3','2B4','2B5','2B6','2B7','2B8','2B9','2B10','2B11','2B12','2B13','2B14'],
            'SS3A':['3A1','3A2','3A3','3A4','3A5','3A6','3A7','3A8','3A9','3A10','3A11','3A12','3A13','3A14'],
            'SS3B':['3B1','3B2','3B3','3B4','3B5','3B6','3B7','3B8','3B9','3B10','3B11','3B12','3B13','3B14']}

    # halls holds where random student will be stored.
    halls = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],'K':[],'L':[],'M':[]}


    print(f'''
            THE TOTAL NUMBER OF CLASS YOU WILL BE GIVING SHOULD INCLUDE THE *A,B,& ...* OF THE CLASSES;
                                SO COUNT THEM ALL TOGETHER.
                                \n\n\n''')


    ''' Getting names of class writing exam'''
    def get_class_name():
        class_name = input(f"\n\t\t.....WHAT CLASS IS THIS?.....: ").upper()
        if class_name in CLASSES:
            return class_name
        else:
            print(f"\n!!!The class '{class_name}' you entered does not match the one in our database!!!.")
            response = input(f"\nDO YOU WANT TO CREATE AND ADD {class_name} TO YOUR DATABASE?. [Y/n]:    ")
            if response == "Y":
                CLASSES[class_name] = list()
                return class_name
            elif response == "n":
                return get_class_name()
            else:
                print("INVALID INPUT, TRY AGAIN. ")
                return get_class_name()

    ''' Getting students in each class'''
    def get_students(class_name):
        class_limit = verify(input(f"\n\t\t   |*| HOW MANY STUDENTS ARE IN {class_name}:  "))
        for i in range(class_limit):
            CLASSES[class_name].append(input(f"\n\t\t\t[*]  GIVE ME ALL {class_name} STUDENTS NAME, ONE AFTER THE OTHER.:    "))

    ''' Storing the class data "Class name & It's students". '''
    def class_data():
        class_name = get_class_name()
        get_students(class_name)

    ''' Getting the total number of the class writing the exam'''
    all_class = verify(input(f"    ___HOW MANY CLASS ARE PRESENTLY WRITING THIS EXAM___?:  "))

    ''' Gathering data for each class '''
    for klass in range(all_class):
        class_data()

    # This function will be used to store the CLASSES parmanently as a database.
    def store_classes_data(_CLASSES):
        with pd.ExcelWriter(stored_file) as writer:
            for Class, Students in _CLASSES.items():
                df = pd.DataFrame(Students, columns = [Class]) 
                sheet_name= Class
                df.to_excel(writer, sheet_name=sheet_name, index=False)

    user_response = input("\n\nDO YOU WANT TO SAVE THE INFORMATION PROVIDED ABOUT ALL CLASS AND STUDENT [Y/n]:     ")

    while True:
        if user_response == "Y":
            store_classes_data(CLASSES)
            break
        elif user_response == "n":
            print("Okay. \n INFO NOT SAVED.")
            break
        else:
            print("Response provided does not correspond; TRY AGAIN. ")
            user_response = input("\n\nDO YOU WANT TO SAVE THE INFORMATION PROVIDED ABOUT ALL CLASS AND STUDENT [Y/n]:     ")

    ''' Getting hall limit and also checking if it greater than total students left.'''
    def h_lim():
        hall_limit = verify(input(f"\n\t\t~~~~~WHAT'S HALL {hall} LIMIT?~~~~~:    "))
        all_students = sum([len(CLASSES[clas[:]]) for clas in CLASSES])
        if hall_limit > all_students:
            print(f" Your hall limit '{hall_limit}', is greater than the number of students '{all_students}' left. ".upper())
            return h_lim()

        else:
            return hall_limit

    # Generating the tabulated output
    for hall in halls:
        hall_limit = h_lim()
        ''' Randomly spliting all students to their hall'''
        while len(halls[hall]) < hall_limit:
            for clas in CLASSES:
                if len(CLASSES[clas[:]]) > 0:
                    random_student = choice(CLASSES[clas[:]])
                    rnd_student_detail = random_student,clas
                    halls[hall].append(list(rnd_student_detail))
                    CLASSES[clas[:]].remove(random_student)
                    if len(halls[hall]) == hall_limit:
                        break

                else:
                    pass
            r = sum([len(CLASSES[clas[:]]) for clas in CLASSES])
        print("\nThe total number of students left is:   ",  r,"\n")

    # Sorting student by class
    def sort_by_class(student):
        return student[1]

    # Sorting the output and writing the output to an Excel file.
    while True:
        user_input = input(f"""  HOW DO WANT TO ARRANGE YOUR OUTPUT?
                    A) ACCORDING TO NAME ALPHABETICAL ORDER
                    B) ACCORDING TO CLASS ORDER
                    ENTER:  """)

        if user_input == "A":
            # Writing the output to Excel with different sheets for each hall
            with pd.ExcelWriter(hall_db_filename) as writer:
                for hall, students in halls.items():
                    df = pd.DataFrame(sorted(students), columns = ["Name", "Class"])
                    # Reset index to start from 1
                    df = df.reset_index(drop=True)
                    df.index += 1
                    # Write the DataFrame to Excel
                    sheet_name = "Hall " + hall
                    df.to_excel(writer, sheet_name=sheet_name, index=True)

            print("Your output has been stored in an Excel file in your present working directory/path.")
            break
        elif user_input == "B":
            # Writing the output to Excel with different sheets for each hall
            with pd.ExcelWriter(hall_db_filename) as writer:
                for hall, students in halls.items():
                    sorted_students = sorted(students, key= sort_by_class)
                    df = pd.DataFrame(sorted_students, columns = ["Name", "Class"])
                    # Reset index to start from 1
                    df = df.reset_index(drop=True)
                    df.index += 1
                    # Write the DataFrame to Excel
                    sheet_name = "Hall " + hall
                    df.to_excel(writer, sheet_name=sheet_name, index=True)

            print("Your output has been stored in an Excel file in your present working directory/path.")
            break
        else:
            print("\n\t[*] Your input does not correspond to required input; 'TRY AGAIN' [*]")

clas_dict = {}
clas_list = []

def loadDB(class_db_filename):
    df_Excel = pd.read_excel(class_db_filename, sheet_name=None)
    clas = input("WHICH CLASS DO YOU WANT TO MODIFY?:   ").upper()
    while True:
        if clas not in df_Excel.keys():
            print(f"\n.....'{clas}' CLASS IS NOT PRESENT IN YOUR STORED CLASS..... ")
            clas = input("\n.....SO WHICH CLASS DO YOU WANT TO MODIFY?.....:   ").upper()
        else:
            print(f"""WHAT DO YOU WANT TO DO T0 "{clas}" CLASS?
                1) DELETE CLASS
                2) REMOVE STUDENT
                3) ADD STUDENT
                4) ADD CLASS
                  """)
            reply = input("  ENTER HERE ===>:    ")
            if reply == "1":
                del(df_Excel[clas])
                print(df_Excel)
                break
            elif reply == "2":
                print("\n", df_Excel[clas])
                name_index = int(input(f"\n USING THE PERSON S/N \n WHO DO YOU WANT TO REMOVE?: "))
                located = df_Excel[clas].iloc[name_index]
                del(located)
                print("Getting deleted: ", df_Excel[clas])                
                break

            elif reply == "3":
                pass
            elif reply == "4":
                pass




StoreDB(output_file)
# loadDB(stored_file)



















# response = input("""DO YOU WANT TO MAKE US THE STORED DATA TO GENERATE THE HALL ARRANGEMENT OR MODIFY THE DATA?
#                     [M] Modify
#                     [Y] Yes
#                     [N] No
#                     ENTER ==>:  """)
# if os.path.exists(stored_file):
#     if response == "Y":
#         loadDB(stored_file)
#     elif response == "N":
#         pass
#     elif response == "M":
#         pass     
#     else:
#         print("INVALID INPUT.")
    












 