from verifier import verify
# Mr Ifeanyi's code for examanatuon distribution

#Creating the names of the halls and names of class names
hall_names = ["A","B","C" ,"D","E","F","G","H","I","J","K","L","M"]
class_names = ["JSS1","JSS2","JSS3","SS1A","SS1B","SS2A","SS2B"]

#names of the students by their class divisions
JSS1 = ["jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20",\
"jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"]

JSS2 = ["jss2","jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"]

JSS3 = ["jss3""jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"]

SS1A = ["ss1a""jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"] 

SS1B = ["ss1b""jss1","lius","pius","jacob","kate","kanyi",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"]

SS2A = ["ss2a""jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20",\
"jss1","lius","pius","jacob","kate","kanyi","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius17","pius18","pius19","pius20"]

SS2B = ["ss2b""jss1","lius","pius","jacob","kate","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20",\
"jss1","lius","pius","kanyi","pius1","pius2",\
"pius3","pius4","pius5","pius6","pius7","pius8","pius9","pius10","pius11",\
"pius12","pius13","pius14","pius15","pius16","pius17","pius18","pius19","pius20"]

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
#print("total_students: ",total_students)
print("Total number of students: ", len(total_students))
#To get hall limits for each hall
hall_limits = [len(total_students)//len(hall_names) for hall in hall_names]
print("hall limits: ", hall_limits)

#To get class limits for eacb class
class_limits = [len(classe)//len(hall_names) for classe in students]
print("class limits: ", class_limits)

#To get hall remainder for each hall
hall_remainder = len(total_students)%len(hall_names)
print("hall remainder: ", hall_remainder)

#To get class limits fir eacb class
class_remainders = [len(classe)%len(hall_names) for classe in students]
print("class remainders", class_remainders)


# User defined inputs

while True:
    response = input("Do you want to define the hall limits your self? [Y/N]: ")
    if response == "Y":
        hall_limits = []
        while sum(hall_limits) != len(total_students):
            for i in range(len(hall_names)):
                hall_limit = int(verify(input(f'''Tell me the hall limit of {hall_names[i]}: ''')))
                hall_limits.append(hall_limit)
            if sum(hall_limits) != len(total_students):
                print(f'''Your input does not match yhe total number of the students.
                Here are what you inputted:
                    Total = {sum(hall_limits)}
                    Total no of students = {len(total_students)}''')
                for i in range(len(halls)):
                    print(hall_names[i]," = ", hall_limits[i])
                hall_limits = []
                print("TRY AGAIN!!")
        break
        
    elif response == "N":
        break
    else:
        print("Not allowed. Type [Y/N]")
        
#Functiin for getting hallsize
def hallsize(hall_name):
    sum = 0
    for students in halls[hall_name].values():
        sum += (len (students))
    return sum
# import random module
import random
   

print(halls)            