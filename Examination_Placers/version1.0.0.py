# Mr Ifeanyi's code for examanatuon distribution

#Creating the names of the halls and names of class names
hall_names = ["A","B","C" ,"D","E","F","G","H","I","J","K","L","M"];
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B"]

#names of the students by their class divisions
JSS1 = ["jss1"]
JSS2 = ["jss2"]
JSS3 = ["jss3"]
SS1A = ["ss1a"]
SS1B = ["ss1b"]
SS2A = ["ss2a"]
SS2B = ["ss2b"]

#full students list
##list method
students = [JSS1, JSS2, JSS3, SS1A, SS1B, SS2A, SS2B]
##dictionary method 
       #Waste of time. It is dependent on the list method
students_d = {}
for i in range(len(class_names)):
    students_d[class_names[i]] = students[i][:]
    
# Creating halls and their class divisions for students
halls = {}
for hall in hall_names:
    halls[hall] ={}
    for classe in class_names:
        halls[hall].update({classe:[]})
        
#print(students,"\n\n", students_d, "\n\n", halls)

#To get the total number of students
total_students = JSS1 + JSS2 + JSS3 + SS1A + SS1B + SS2A + SS2B  
print("total_students: ",total_students)

#To get hall limits for each hall
hall_limit = len(total_students)//len(hall_names)
print("hall limit: ", hall_limit)

#To get class limits fir eacb class
class_limits = [len(classe)//len(hall_names) for classe in students]
print("class limits: ", class_limits)

#To get hall remainder for each hall
hall_remainder = len(total_students)%len(hall_names)
print("hall remainder: ", hall_remainder)

#To get class limits fir eacb class
class_remainders = [len(classe)%len(hall_names) for classe in students]
print("class remainders", class_remainders)
