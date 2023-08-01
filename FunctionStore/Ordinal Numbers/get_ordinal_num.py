numbers = [1,2,3,4,5,56,77,10,34,22,13,]
def getOrdinalNum(number):
    if str(number)[-1] in ("1","2","3") and number not in range(10,20):
        if str(number)[-1] == "1":
            ordnum = str(number) + "st"
        elif str(number)[-1] == "2":
            ordnum = str(number) + "nd"
        elif str(number)[-1] == "3":
            ordnum = str(number) + "rd"
    else:
        ordnum = str(number) + "th"
    return ordnum
for number in numbers:
    print(getOrdinalNum(number))