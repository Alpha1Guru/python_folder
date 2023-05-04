hall_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B"]

students = {
    "JSS1": ["jss1", "john", "fatia","mujeeb","helen","absolom"],
    "JSS2": ["jss2"],
    "JSS3": ["jss3","geoferry","taiwo"],
    "SS1A": ["ss1a","horla","olaf", "rati","jarimat"],
    "SS1B": ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace","magarita","toyin"],
    "SS2A": ["ss2a","emmma","latifa","baba","tola"],
    "SS2B": ["ss2b", "marvellous"],
    "SS3A": ["ss3a","bolu","kante","tochi","kosi"],
    "SS3B": ["ss3b","bade","xenox","kuma"]
}

halls = {hall_name: {classe: [] for classe in class_names} for hall_name in hall_names}

total_students = [student for students_list in students.values() for student in students_list]
hall_limits = [len(total_students) // len(hall_names) for hall in hall_names]
hall_remainder = len(total_students) % len(hall_names)
class_limits = [len(students[classe]) // len(hall_names) for classe in class_names]
class_remainders = [len(students[classe]) % len(hall_names) for classe in class_names]

def hallsize(hall_name):
    return sum(len(classe) for classe in halls[hall_name].values())

def totalhallsize():
    return sum(hallsize(hall_name) for hall_name in hall_names)

def remainder():
    return len(total_students) - totalhallsize()

while True:
    response = input("Do you want to define the hall limits yourself? [Y/N]: ")
    if response == "Y":
        hall_limits = []
        while sum(hall_limits) != len(total_students):
            hall_limits = []
            for i in range(len(hall_names)):
                hall_limit = int(input(f"Tell me the hall limit of {hall_names[i]}: "))
                hall_limits.append(hall_limit)
            if sum(hall_limits) != len(total_students):
                print(f'''Your input does not match the total number of the students.
                Here are what you inputted:
                    Total = {sum(hall_limits)}
                    Total no of students = {len(total_students)}''')
                for i in range(len(halls)):
                    print(hall_names[i]," = ", hall_limits[i])
                print("TRY AGAIN!!")
        break
    elif response == "N":
        break
    else:
        print("Not allowed. Type [Y/N]")

for i in range(len(hall_names)):
    while hallsize(hall_names[i]) < hall_limits[i]:
        for classe in class_names:
            if hallsize(hall_names[i]) < hall_limits[i]:
                hall_remainder_slots = hall_limits[i] - hallsize(hall_names[i])
                class_remainder_slots = class_remainders[class_names.index(classe)]
                if halls[hall_names
