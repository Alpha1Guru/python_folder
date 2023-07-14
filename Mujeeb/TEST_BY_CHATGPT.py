import unittest
import pandas as pd
from your_module import StoreDB, loadDB

class HallPlacementTest(unittest.TestCase):
    def setUp(self):
        self.CLASSES = {
            'JSS1': ['Chukwujekwu Pius', 'Akintoye Tolu', 'Adefisoye Sam', 'Ofoke Max', 'Ofoke James', '16', '17', '18', '19', '110', '111', '112', '113', '114'],
            'JSS2': ['21', '22', '23', '24', '25', '26', '27', '28', '29', '210', '211', '212', '213', '214'],
            'JSS3': ['31', '32', '33', '34', '35', '36', '37', '38', '39', '310', '311', '312', '313', '314'],
            'SS1A': ['1A1', '1A2', '1A3', '1A4', '1A5', '1A6', '1A7', '1A8', '1A9', '1A10', '1A11', '1A12', '1A13', '1A14'],
            'SS1B': ['1B1', '1B2', '1B3', '1B4', '1B5', '1B6', '1B7', '1B8', '1B9', '1B10', '1B11', '1B12', '1B13', '1B14'],
            'SS2A': ['2A1', '2A2', '2A3', '2A4', '2A5', '2A6', '2A7', '2A8', '2A9', '2A10', '2A11', '2A12', '2A13', '2A14'],
            'SS2B': ['2B1', '2B2', '2B3', '2B4', '2B5', '2B6', '2B7', '2B8', '2B9', '2B10', '2B11', '2B12', '2B13', '2B14'],
            'SS3A': ['3A1', '3A2', '3A3', '3A4', '3A5', '3A6', '3A7', '3A8', '3A9', '3A10', '3A11', '3A12', '3A13', '3A14'],
            'SS3B': ['3B1', '3B2', '3B3', '3B4', '3B5', '3B6', '3B7', '3B8', '3B9', '3B10', '3B11', '3B12', '3B13', '3B14']
        }
        self.halls = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': []}
        self.hall_db_filename = "test_hall_placement.xlsx"
        self.class_db_filename = "test_classes_data.xlsx"

    def test_StoreDB(self):
        def count_students(classes):
            return sum(len(students) for students in classes.values())

        # Store the data
        StoreDB(self.hall_db_filename)

        # Load the stored data
        df_classes = pd.read_excel(self.class_db_filename, sheet_name=None)
        stored_classes = {}
        for class_name, sheet in df_classes.items():
            stored_classes[class_name] = sheet.iloc[:, 0].tolist()

        # Check if the stored data matches the original data
        self.assertDictEqual(self.CLASSES, stored_classes)

        # Check if all students are assigned to a hall
        total_students = count_students(self.CLASSES)
        assigned_students = sum(len(hall) for hall in self.halls.values())
        self.assertEqual(total_students, assigned_students)

    def test_loadDB(self):
        # Create a test data file
        with pd.ExcelWriter(self.class_db_filename) as writer:
            for class_name, students in self.CLASSES.items():
                df = pd.DataFrame(students, columns=[class_name])
                df.to_excel(writer, sheet_name=class_name, index=False)

        # Modify the stored data
        loadDB(self.class_db_filename)

        # Check if the modified data is updated
        df_classes = pd.read_excel(self.class_db_filename, sheet_name=None)
        modified_classes = {}
        for class_name, sheet in df_classes.items():
            modified_classes[class_name] = sheet.iloc[:, 0].tolist()

        # Check if the modified data matches the expected data
        expected_classes = {
            'JSS1': ['Chukwujekwu Pius', 'Akintoye Tolu', 'Adefisoye Sam', 'Ofoke Max', 'Ofoke James', '16', '17', '18', '19', '110', '111', '112', '113', '114'],
            'JSS2': ['21', '22', '23', '24', '25', '26', '27', '28', '29', '210', '211', '212', '213', '214'],
            'JSS3': ['31', '32', '33', '34', '35', '36', '37', '38', '39', '310', '311', '312', '313', '314'],
            'SS1A': ['1A1', '1A2', '1A3', '1A4', '1A5', '1A6', '1A7', '1A8', '1A9', '1A10', '1A11', '1A12', '1A13', '1A14'],
            'SS1B': ['1B1', '1B2', '1B3', '1B4', '1B5', '1B6', '1B7', '1B8', '1B9', '1B10', '1B11', '1B12', '1B13', '1B14'],
            'SS2A': ['2A1', '2A2', '2A3', '2A4', '2A5', '2A6', '2A7', '2A8', '2A9', '2A10', '2A11', '2A12', '2A13', '2A14'],
            'SS2B': ['2B1', '2B2', '2B3', '2B4', '2B5', '2B6', '2B7', '2B8', '2B9', '2B10', '2B11', '2B12', '2B13', '2B14'],
            'SS3A': ['3A1', '3A2', '3A3', '3A4', '3A5', '3A6', '3A7', '3A8', '3A9', '3A10', '3A11', '3A12', '3A13', '3A14'],
            'SS3B': ['3B1', '3B2', '3B3', '3B4', '3B5', '3B6', '3B7', '3B8', '3B9', '3B10', '3B11', '3B12', '3B13', '3B14']
        }
        self.assertDictEqual(expected_classes, modified_classes)

if __name__ == '__main__':
    unittest.main()
