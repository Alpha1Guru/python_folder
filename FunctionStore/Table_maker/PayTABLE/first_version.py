

teacher_names = ["ifeanyi","oyebiyi","inyang","victor","segun"]
teacher_no_periods = [24, 5, 6, 7, 8]
teacher_pays = [28238, 3733, 263, 373,234]
teacher_serial_no= [1,2,3,4,5]
n=len(teacher_names)
print(n)

#A dictionary containing teachers data
teachers_data={}
for i in range(n):
    teachers_data[i] = {'serial_no' : teacher_serial_no[i],
                                      'name' : teacher_names[i],
                                      'period' : teacher_no_periods[i],
                                      'payment' : teacher_pays[i],
                                      }
print(teachers_data)

title_columns=[]
for k,v in teachers_data[0].items():
    title_columns.append(k)
print(title_columns)    

#to find the max of all columns
maxs=[]
for j in range(len(title_columns)):
    maxi=[]
    for i in range(n):
        
        mx=teachers_data[i][title_columns[j]]
        maxi.append(len(str(mx)))
    print (maxi)
    maxs.append(max(maxi))
     
print(maxs) 
 
for i in range(n):
    row= ""
    for j in range(len(title_columns)):
       #To get extra spaces
       #subract the value of the present column from it's biggest vertical column
       extra=maxs[j]-len(str(teachers_data[i][title_columns[j]]))
       spaces=""
       for num in range(extra):
           spaces+=" "
       word=" " + str(teachers_data[i][title_columns[j]]).title()+ spaces+" "
       cell= word +"|"
       row+=cell
    print(row)  
    