def MakeMultiplicationTable(rownum , columnum,startrow=1,startcolumn=1):
    import tabulate
    table = {}
    table[1]= [1*j for j in range(startcolumn,columnum+1) ]
    """Even if startrow is equal to one(1) the multiplication table for one(1)
       is not duplicated because python  automatically removes  duplicates from a dictinary
    """
    for i in range(startrow,rownum+1):
        list = []
        for j in range(startcolumn,columnum+1):
            list.append(i*j)
        table[i]= list
    # print(table)
    Multitable = tabulate.tabulate(table, headers= "keys", tablefmt= "simple")
    with open("C:/Users/hp/Documents/Github/python_folder/Table_maker/Multitable.txt","w") as file:
        file.write(Multitable)
    print(Multitable)
MakeMultiplicationTable(94,12,startcolumn=1,startrow=80)