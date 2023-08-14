# Mr Ifeanyi's code for examanation distribution

#Creating the names of the halls and names of class names
hall_names = ["A","B","C" ,"D","E","F","G","H","I","J","K","L","M"]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B","SS3A","SS3B"]

# Permanent list  of the students by their class divisions
__JSS1 = ["jss1", "john", "fatia","mujeeb","helen","absolom",]
__JSS2 = ["jss2"]
__JSS3 = ["jss3","geoferry","taiwo",]
__SS1A = ["ss1a","horla","olaf", "rati","jarimat",]
__SS1B = ["ss1b","yemi","alade","okoli","micheal","henry","gloria","peace","magarita","toyin"]
__SS2A = ["ss2a","emmma","latifa","baba","tola"]
__SS2B = ["ss2b", "marvellous"]
__SS3A = ["ss3a","bolu","kante","tochi","kosi",]
__SS3B = ["ss3b","bade","xenox","kuma"]

#Temporal list for data manipulation
JSS1 = __JSS1[:]
JSS2 = __JSS2[:]
JSS3 = __JSS3[:]
SS1A = __SS1A[:]
SS1B = __SS1B[:]
SS2A = __SS2A[:]
SS2B = __SS2B[:]
SS3A = __SS3A[:]
SS3B = __SS3B[:]

classes = [JSS1, JSS2, JSS3, SS1A, SS1B, SS2A, SS2B, SS3A, SS3B]
print("classes: ", classes)
##dictionary method 
       #Waste of time. It is dependent on the list method
students_d = {}
for i in range(len(class_names)):
    students_d[class_names[i]] = classes[i][:]
    
# Creating halls and their class divisions for students
halls = {}
for hall in hall_names:
    halls[hall] ={}
    for classe in class_names:
        halls[hall].update({classe:[]})
        
#print(students,"\n\n", students_d, "\n\n", halls)

#To get the total number of students
total_students = JSS1 + JSS2 + JSS3 + SS1A + SS1B + SS2A + SS2B + SS3A + SS3B
print("total_students: ",len(total_students))

#To get hall limits for each hall
hall_limits = [len(total_students)//len(hall_names) for hall in hall_names]
print("hall limit: ", hall_limits)


#To get hall remainder for each hall
hall_remainder = len(total_students)%len(hall_names)
print("hall remainder: ", hall_remainder)

#To get class limits for each class
class_limits = [len(classe)//len(hall_names) for classe in classes]
print("class limits: ", class_limits)

#To get class limits for each class
class_remainders = [len(classe)%len(hall_names) for classe in classes]
print("class remainders", class_remainders)

# Functions used for checking the state of the halls 
def hallsize(hall_name): # returns the number of students assigned in a specified hall 
    sums = 0
    for class_name, classe in halls[hall_name].items(): # starting from the first class in a hall to the last 
        sum = len(classe) #get the length of the class
        sums += sum #add it the sum move to the next class
    return sums #return the sum

def totalhallsize(): # returns the total number of students assingned in all halls
    total = 0
    for hall_name in hall_names: # adds the hall size of each halls together
        sums = hallsize(hall_name)
        total += sums
    return total

def remainder(): # returns the total number of students NOT assigned to any hall
    return len(total_students) - totalhallsize()

import random
for i in range(len(hall_names)):
    while hallsize(hall_names[i]) < hall_limits[i]:
        for j in range(len(class_names)):
            if len(classes[j]) > 0 and hallsize(hall_names[i]) < hall_limits[i]:
                selected = random.choice(classes[j])
                print(classes[j])
                classes[j].remove(selected)
                print(classes[j])
                halls[hall_names[i]][class_names[j]].append(selected)
    print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
print("remainder",remainder(),"\t")

for i in range(len(hall_names)):
    if remainder() == 0:
        break
    else:
        random_class = random.choice(classes)
        j = classes.index(random_class)
        while len(random_class) == 0:
            random_class = random.choice(classes)
            j = classes.index(random_class)
        selected = random.choice(random_class)
        print(random_class)
        halls[hall_names[i]][class_names[j]].append(selected)
        random_class.remove(selected)
        print(random_class)
    print(hall_names[i],halls[hall_names[i]]);print(hallsize(hall_names[i]))
print("remainder",remainder())
print(halls)