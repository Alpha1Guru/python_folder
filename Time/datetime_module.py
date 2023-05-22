
#Example 1: Python get today's date

from datetime import date

today = date.today()
print("Today's date:", today)


from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)



#Get the current date and time in Python

#If we need to get the current date and time, you can use the datetime class of the datetime module.

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
#Here, we have used datetime.now() to get the current date and time.

#Then, we used strftime() to create a string representing date and time in another format.
