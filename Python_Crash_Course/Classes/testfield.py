class Class:
    """A simple attempt to model a class"""
    """A class should contain members
    """
    name_of_initiated_class = []
    school = "Secondary School"
    def __init__(self, name, members):
        """_summary_
        Initialize name and members attributes

        Args:
            name (str): name of the class
            members (list): list of class members
        """
        self.name = name
        self.members = members
        self.name_of_initiated_class.append(self.name)
    def len(self):
        return len(self.members)
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
for class_name, members in students_by_class.items():
    students_by_class[class_name] = Class(class_name,members=members)
for class_name in students_by_class:
    print(students_by_class[class_name].len())
print(Class.name_of_initiated_class)