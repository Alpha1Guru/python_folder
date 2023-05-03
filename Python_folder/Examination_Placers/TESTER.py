# Mr Ifeanyi's code for examanatuon distribution

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
hall_limit = [len(total_students)//len(hall_names) for hall in hall_names]
print("hall limit: ", hall_limit)


#To get hall remainder for each hall
hall_remainder = len(total_students)%len(hall_names)
print("hall remainder: ", hall_remainder)

#To get class limits for each class
class_limits = [len(classe)//len(hall_names) for classe in classes]
print("class limits: ", class_limits)

#To get class limits for each class
class_remainders = [len(classe)%len(hall_names) for classe in classes]
print("class remainders", class_remainders)

def hallsize(hall_name):
    sums = 0
    for class_name, classe in halls[hall_name].items():
        sum = len(classe)
        sums += sum
    return sums

def totalhallsize():
    total = 0
    for hall_name in hall_names:
        sums = hallsize(hall_name)
        total += sums
    return total
def remainder():
    return len(total_students) - totalhallsize()
print("A:",hallsize("A"))
halls["A"]["JSS1"].extend(["james","micheal","helen"])
print(halls["A"])
print(hallsize("A"))
print("B:",hallsize("B"))
halls["B"]["JSS1"].extend(["james","micheal","helen"])
print(halls["B"])
print(hallsize("B"))

print(halls)
print(totalhallsize())
print(remainder())