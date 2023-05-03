
teacher_names = ["ifeanyi","oyebiyi","inyang","victor","segun"]
teacher_no_periods = [24, 5, 6, 7, 8]
teacher_pays = [28238, 37336666, 263, 373,234]
teacher_serial_no= [1,2,3,4,5]
n=len(teacher_names)
#print(n)

#A dictionary containing teachers data
teachers_data={}
for i in range(n):
    teachers_data[i] = {
                                      'serial_no' : teacher_serial_no[i],
                                      'name' : teacher_names[i],
                                      'period' : teacher_no_periods[i],
                                      'payment' : teacher_pays[i] 
                                      }
                                      
title_columns=[]
for k,v in teachers_data[0].items():
    title_columns.append(k)
#print(title_columns)    

#to find the max of all columns
maxs=[]
for j in range(len(title_columns)):
    maxi=[]
    for i in range(n):
        
        mx=teachers_data[i][title_columns[j]]
        maxi.append(len(str(mx)))
    #print (maxi)
    maxs.append(max(maxi))
     
#print(maxs) 
                                      
# Checking if the titles are longer than the largest data in a column
for j in range(len(maxs)):
    if maxs[j] < len(str(title_columns[j])):
        maxs[j] = len(str(title_columns[j]))
#print(maxs)  

# To Design the Title headings
r_padding = " "*2 #right padding space
l_padding = " "*2 #left padding space
r_border = "|" #character for right border lines
l_border = "|" #character for left border lines
t_hline = "=" #character for title horizontal lines
n_hline = "+" #character for normal horizontal lines

# Creating the title row i.e the one with all the headings
title_row=""
for j in range(len(title_columns)):
    extra=maxs[j] - len(str(title_columns[j]))
    spaces=" " * extra  
    title_word=str(title_columns[j]).title()+ spaces
    if  title_columns[j] == title_columns[-1]:
        title_cell= l_border + l_padding +title_word + r_padding + r_border
    else:
        title_cell= l_border + l_padding +title_word + r_padding     
    title_cell_block = title_cell
    title_row += title_cell_block
    
title_block= t_hline*len(title_row)
title_row += "\n" + n_hline*len(title_row)
title_block+="\n" + title_row
#print(title_block)

# Creating the table for the data
rows="\n" +title_block
for i in range(n):
    row= ""
    for j in range(len(title_columns)):
       #To get extra spaces
       #subract the value of the present column from it's biggest vertical column
       extra=maxs[j] - len(str(teachers_data[i][title_columns[j]]))
       spaces=" " * extra
       word =spaces + str(teachers_data[i][title_columns[j]]).title()
       if  teachers_data[i][title_columns[j]] == teachers_data[i][title_columns[-1]]:
           cell= l_border + l_padding +word + r_padding + r_border
       else:
           cell= l_border + l_padding +word + r_padding 
       cell_block = cell
       row+=cell_block
    row += "\n" + n_hline*len(row)
    #print(row)  
    rows+="\n"+row
#print(rows)
    
#Table heading
table_heading = "lesson teachers' reports".title()

#To build full table
full_table = "\n" + table_heading
full_table +=  rows
#print(full_table)

#Date and Time of operation
import time
date = "Date: " + time.strftime("%A %B %d, %Y")
#print(date)
time = "Time: " + time.strftime("%I:%M:%S %p")
#print(time)

#full page
full_page = "\n" + date +"\n" + time +"\n" + full_table
print(full_page)

#copying full page to a file
file= "C:/Users/hp/Documents/Python_folder/text_files_folder/mrifeanyi.txt"
with open( file,'w') as text_file:
    text_file.write(full_page)
    