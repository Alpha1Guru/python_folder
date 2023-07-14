import unittest
import pandas as pd
from your_module import assign_students_to_halls, generate_students_data, save_hall_data_to_excel

class HallPlacementTest(unittest.TestCase):
    def setUp(self):
        self.hall_names = ["A", "B", "C", "D", "E"]
        self.class_names = ["JSS1", "JSS2", "JSS3", "SS1A", "SS1B"]
        self.students_by_class = {
            "JSS1": ["John", "Jane", "Alice"],
            "JSS2": ["Bob", "Emily"],
            "JSS3": ["Sam", "Sara", "Peter"],
            "SS1A": ["Tom", "Lisa", "Mike"],
            "SS1B": ["Kate", "David"]
        }
    
    def test_assign_students_to_halls(self):
        halls = assign_students_to_halls(self.hall_names, self.class_names, self.students_by_class)
        
        # Ensure all students are assigned to a hall
        total_students = sum(len(class_members) for class_members in self.students_by_class.values())
        assigned_students = sum(len(hall) for hall in halls.values() for hall in hall.values())
        self.assertEqual(total_students, assigned_students)
        
        # Ensure hall size limit is not exceeded
        hall_limits = [2, 2, 3, 3, 3]  # Example hall size limits
        for hall_name in self.hall_names:
            for class_name in self.class_names:
                class_size = len(halls[hall_name][class_name])
                self.assertLessEqual(class_size, hall_limits[self.hall_names.index(hall_name)])
    
    def test_generate_students_data(self):
        students_by_hall_name_and_class = {}
        generate_students_data(self.hall_names, self.class_names, students_by_hall_name_and_class)
        
        # Ensure all students are included in the generated data
        total_students = sum(len(class_members) for class_members in self.students_by_class.values())
        generated_students = sum(len(data) for data in students_by_hall_name_and_class.values())
        self.assertEqual(total_students, generated_students)
        
        # Ensure each student's class is correct
        for hall_name, data in students_by_hall_name_and_class.items():
            for student_data in data:
                student_name = student_data[0]
                student_class = student_data[1]
                self.assertIn(student_name, self.students_by_class[student_class])
    
    def test_save_hall_data_to_excel(self):
        hall_file = "hall_placement.xlsx"
        students_by_hall_name_and_class = {
            "Hall A": [["John", "JSS1"], ["Jane", "JSS2"]],
            "Hall B": [["Bob", "JSS3"], ["Emily", "SS1A"]],
            "Hall C": [["Sam", "SS1B"]]
        }
        
        save_hall_data_to_excel(hall_file, self.hall_names, students_by_hall_name_and_class)
        
        # Load the saved Excel file and check the data
        df = pd.read_excel(hall_file, sheet_name=None)
        for hall_name, data in students_by_hall_name_and_class.items():
            sheet_name = hall_name + " Hall"
            self.assertIn(sheet_name, df.keys())
            sheet_data = df[sheet_name]
            for i, student_data in enumerate(data):
                self.assertEqual(student_data[0].title(), sheet_data.loc[i+1, "Name"])
                self.assertEqual(student_data[1], sheet_data.loc[i+1, "Class"])

if __name__ == '__main__':
    unittest.main()
